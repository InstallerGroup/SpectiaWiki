import os
from pathlib import Path
from notion_client import Client
from dotenv import load_dotenv
import markdown
import re
import mimetypes
import requests
from urllib.parse import quote, unquote
import uuid

# Load environment variables
load_dotenv()
notion = Client(auth=os.getenv("NOTION_API_KEY"))
CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_KEY")
CLOUDFLARE_ACCOUNT_ID = "70f8c9ddb377d2d463bf2f9e2a8669f8"  # Replace with your account ID

# The target page ID where we'll create our database
PAGE_ID = "1859cdb8b868808aadc7c16e13a718f7"

def clean_title(title):
    """Clean the title to be Notion-friendly"""
    # First decode any URL-encoded characters
    title = unquote(title)
    # Replace hyphens with spaces and clean up extra spaces
    title = title.replace('-', ' ').strip()
    # Remove any other problematic characters
    title = re.sub(r'[^\w\s-]', ' ', title)
    # Clean up multiple spaces
    title = re.sub(r'\s+', ' ', title)
    return title

def read_order_file(path):
    """Read .order file if it exists"""
    order_path = path / '.order'
    if order_path.exists():
        with open(order_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    return []

def read_markdown_file(file_path):
    """Read and parse markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove any null bytes that might cause issues
            content = content.replace('\x00', '')
            return content
    except UnicodeDecodeError:
        # Try with a different encoding if UTF-8 fails
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()
            return content

def upload_to_cloudflare(file_path):
    """Upload a file to Cloudflare Images and return the URL"""
    try:
        headers = {
            'Authorization': f'Bearer {CLOUDFLARE_API_KEY}'
        }
        
        with open(file_path, 'rb') as f:
            files = {
                'file': f
            }
            
            response = requests.post(
                f'https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/images/v1',
                headers=headers,
                files=files
            )
            
            print(f"Cloudflare response: {response.text}")  # Debug output
            
            if response.status_code == 200:
                result = response.json()
                if result.get('success'):
                    image_id = result['result']['id']
                    # Use the Cloudflare worker proxy URL format
                    image_url = f"https://notionimage.kring.com/images/{image_id}/_5OKbt1LGRngtcb5j60bCA.png"
                    print(f"Using proxy URL: {image_url}")
                    return image_url
            
            print(f"Cloudflare API Error: {response.text}")
            return None
            
    except Exception as e:
        print(f"Failed to upload file to Cloudflare: {str(e)}")
        return None

def upload_file_to_notion(file_path):
    """Upload a file to Cloudflare and return the URL for Notion"""
    return upload_to_cloudflare(file_path)

def find_image_path(markdown_file_path, image_ref):
    """Find the actual image path from a markdown reference"""
    # Remove any URL encoding
    image_ref = unquote(image_ref)
    
    # Handle absolute paths (starting with /.attachments)
    if image_ref.startswith('/.attachments/'):
        image_ref = image_ref[1:]  # Remove the leading slash
    
    # List of possible locations to check
    possible_paths = [
        # Direct reference from workspace root
        Path(image_ref),
        # Direct reference from file location
        Path(markdown_file_path).parent / image_ref,
        # In root .attachments (without the .attachments prefix if it's already there)
        Path('.attachments') / image_ref.replace('.attachments/', ''),
        # In root .attachments (with just the filename)
        Path('.attachments') / Path(image_ref).name,
        # In Wiki/.attachments
        Path('Wiki/.attachments') / Path(image_ref).name,
    ]
    
    for path in possible_paths:
        if path.exists():
            print(f"✅ Found image at: {path}")
            return path
    
    print(f"❌ Could not find image at any of these locations:")
    for path in possible_paths:
        print(f"  - {path}")
    return None

def process_markdown_images(content, markdown_file_path):
    """Process markdown content and convert image references to Notion URLs"""
    blocks = []
    
    # Regular expression for markdown images
    image_pattern = r'!\[(.*?)\]\((.*?)\)'
    last_end = 0
    
    for match in re.finditer(image_pattern, content):
        # Add text before the image as a paragraph
        text_before = content[last_end:match.start()].strip()
        if text_before:
            blocks.extend(markdown_to_notion_blocks(text_before))
        
        # Process the image
        alt_text = match.group(1)
        image_ref = match.group(2)
        
        # Find the actual image file
        image_path = find_image_path(markdown_file_path, image_ref)
        
        if image_path:
            # Upload image to Cloudflare
            image_url = upload_file_to_notion(image_path)
            if image_url:
                # Create a simpler image block structure
                image_block = {
                    "type": "image",
                    "image": {
                        "type": "external",
                        "external": {
                            "url": image_url
                        }
                    }
                }
                
                # Only add caption if there is alt text
                if alt_text:
                    image_block["image"]["caption"] = [
                        {
                            "type": "text",
                            "text": {
                                "content": alt_text
                            }
                        }
                    ]
                
                blocks.append(image_block)
            else:
                print(f"⚠️ Failed to upload image: {image_path}")
                blocks.append({
                    "type": "callout",
                    "callout": {
                        "rich_text": [{
                            "type": "text",
                            "text": {
                                "content": f"⚠️ Failed to include image: {Path(image_ref).name}"
                            }
                        }],
                        "icon": {"emoji": "⚠️"}
                    }
                })
        else:
            print(f"⚠️ Could not find image: {image_ref}")
            blocks.append({
                "type": "callout",
                "callout": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": f"⚠️ Image not found: {Path(image_ref).name}"
                        }
                    }],
                    "icon": {"emoji": "⚠️"}
                }
            })
        
        last_end = match.end()
    
    # Add remaining text
    remaining_text = content[last_end:].strip()
    if remaining_text:
        blocks.extend(markdown_to_notion_blocks(remaining_text))
    
    return blocks

def markdown_to_notion_blocks(content):
    """Convert markdown content to Notion blocks"""
    if not content.strip():
        return [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": ""}}]
            }
        }]
    
    blocks = []
    # Split content into lines and process
    lines = content.split('\n')
    current_block = None
    
    for line in lines:
        # Basic block creation - you might want to expand this for more markdown features
        if line.strip():
            if line.startswith('#'):
                # Handle headers
                level = len(re.match(r'^#+', line).group())
                text = line.lstrip('#').strip()
                header_type = f"heading_{level}" if level <= 3 else "heading_3"
                blocks.append({
                    "object": "block",
                    "type": header_type,
                    header_type: {
                        "rich_text": [{"type": "text", "text": {"content": text}}]
                    }
                })
            else:
                # Regular paragraph
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": line}}]
                    }
                })
    
    return blocks if blocks else [{
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"type": "text", "text": {"content": ""}}]
        }
    }]

def create_notion_page(parent_id, title, content, file_path=None, is_child=True):
    """Create a new page in Notion"""
    page_properties = {
        "title": {"title": [{"text": {"content": clean_title(title)}}]},
    }
    
    try:
        # First create the page without content
        page = notion.pages.create(
            parent={"page_id": parent_id} if is_child else {"database_id": parent_id},
            properties=page_properties,
        )
        
        # Convert markdown content to Notion blocks, handling images if present
        if file_path:
            blocks = process_markdown_images(content, file_path)
        else:
            blocks = markdown_to_notion_blocks(content)

        # Add content blocks in smaller batches (25 instead of 50) to be safer
        for i in range(0, len(blocks), 25):
            batch = blocks[i:i + 25]
            try:
                notion.blocks.children.append(
                    block_id=page['id'],
                    children=batch,
                    request_kwargs={
                        "headers": {
                            "Accept": "application/json",
                            "Notion-Version": "2022-06-28"
                        }
                    }
                )
            except Exception as e:
                print(f"Error adding batch of blocks to page {title}: {str(e)}")
                # Print the failing batch for debugging
                print("Failing batch content:")
                for block in batch:
                    if block.get("type") == "image":
                        print(f"Image URL: {block['image']['external']['url']}")
                print("Continuing with next batch...")
        
        return page
    except Exception as e:
        print(f"Error creating page {title}: {str(e)}")
        if "Invalid image url" in str(e):
            print("Image URL validation failed. URL format must be incorrect.")
        return None

def process_directory(path, parent_id, is_root=False):
    """Process a directory and its contents"""
    print(f"\nProcessing directory: {path}")
    order = read_order_file(path)
    items = set(os.listdir(path))
    
    # Remove special files
    for special in ['.order', '.git', '.env', '.gitignore', '.attachments']:
        if special in items and special in items:
            items.remove(special)
    
    # Process items in order
    for item in order:
        if item in items:
            items.remove(item)
            process_item(path / item, parent_id)
    
    # Process remaining items
    for item in sorted(items):
        if item.startswith('.'):
            continue
        process_item(path / item, parent_id)

def process_item(path, parent_id):
    """Process a single item (file or directory)"""
    path = Path(path)
    if path.is_file() and path.suffix.lower() == '.md':
        # Create page for markdown file
        title = path.stem
        content = read_markdown_file(path)
        print(f"Creating page: {title}")
        page = create_notion_page(parent_id, title, content, file_path=path)
        if page:
            print(f"✅ Created page: {title}")
        else:
            print(f"❌ Failed to create page: {title}")
        
    elif path.is_dir():
        # Create a page for the directory
        title = path.name
        print(f"Creating section: {title}")
        page = create_notion_page(parent_id, title, "")
        if page:
            print(f"✅ Created section: {title}")
            # Process directory contents
            process_directory(path, page['id'])
        else:
            print(f"❌ Failed to create section: {title}")

def main():
    try:
        print("Starting wiki upload to Notion...")
        print(f"Target page ID: {PAGE_ID}")
        
        # Verify page access
        notion.pages.retrieve(page_id=PAGE_ID)
        
        # Start processing from the Wiki directory
        wiki_path = Path('Wiki')
        if not wiki_path.exists():
            print("❌ Error: Wiki directory not found!")
            return
        
        # Create the root page
        root_page = create_notion_page(
            PAGE_ID,
            "Azure DevOps Wiki",
            "Imported wiki content",
            is_child=True
        )
        
        if not root_page:
            print("❌ Error: Failed to create root page!")
            return
            
        print("✅ Created root page")
        process_directory(wiki_path, root_page['id'], is_root=True)
        print("\n✅ Upload complete!")
        print(f"You can view your wiki at: https://notion.so/{root_page['id'].replace('-', '')}")
        
    except Exception as e:
        print(f"\n❌ Error during upload: {str(e)}")

if __name__ == "__main__":
    main() 