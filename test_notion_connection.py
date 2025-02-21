import os
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Notion client
notion = Client(auth=os.getenv("NOTION_API_KEY"))

# The target page ID
PAGE_ID = "1859cdb8b868808aadc7c16e13a718f7"

def test_connection():
    try:
        # Try to retrieve the page to verify access
        page = notion.pages.retrieve(page_id=PAGE_ID)
        print("✅ Successfully connected to Notion!")
        print(f"Page title: {page['properties'].get('title', {}).get('title', [{}])[0].get('text', {}).get('content', 'Untitled')}")
        
        # Create a test block to verify write permissions
        test_block = notion.blocks.children.append(
            block_id=PAGE_ID,
            children=[{
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Test connection successful! This block will be removed."
                        }
                    }],
                    "icon": {"emoji": "✅"}
                }
            }]
        )
        
        print("✅ Successfully created a test block!")
        
        # Clean up by removing the test block
        notion.blocks.delete(block_id=test_block['results'][0]['id'])
        print("✅ Successfully cleaned up test block!")
        
        return True
        
    except Exception as e:
        print("❌ Error:", str(e))
        return False

if __name__ == "__main__":
    print("Testing Notion connection...")
    test_connection() 