# Azure DevOps Wiki to Notion Importer

This tool imports an Azure DevOps wiki into Notion, preserving the structure, content, and images. It handles markdown content, hierarchical organization, and image uploads through Cloudflare Images with a custom image proxy.

## Setup

1. Create a `.env` file with your API keys:
```env
NOTION_API_KEY=your_notion_integration_token
CLOUDFLARE_API_KEY=your_cloudflare_api_token
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How It Works

### Main Script (`upload_to_notion.py`)

The script performs the following:

1. Reads the Azure DevOps wiki structure from the local filesystem
2. Maintains hierarchy using `.order` files
3. Processes markdown content and converts it to Notion blocks
4. Handles image uploads through Cloudflare Images
5. Creates pages in Notion with proper parent-child relationships

### Image Handling

The process for handling images involves:

1. Images are uploaded to Cloudflare Images via their API
2. A custom Cloudflare Worker (`cloudflare-worker.js`) transforms the image URLs
3. Images are served through a proxy that makes them compatible with Notion's requirements

#### Image URL Flow:
1. Original image in wiki: `/.attachments/image-123.png`
2. Uploaded to Cloudflare Images: `https://imagedelivery.net/_5OKbt1LGRngtcb5j60bCA/<image_id>/public`
3. Transformed by worker: `https://notionimage.kring.com/images/<image_id>/_5OKbt1LGRngtcb5j60bCA.png`

### Cloudflare Worker

The Cloudflare Worker (`cloudflare-worker.js`) acts as a proxy that:
1. Receives requests in Notion-compatible format
2. Transforms URLs to fetch from Cloudflare Images
3. Serves images with proper headers and format

## Usage

1. Export your Azure DevOps wiki to a local directory
2. Update the `PAGE_ID` in the script with your target Notion page ID
3. Run the script:
```bash
python upload_to_notion.py
```

## Requirements

- Python 3.7+
- Notion API access
- Cloudflare account with:
  - Images enabled
  - API token with Images permissions
  - Workers enabled for custom image proxy

## Files

- `upload_to_notion.py`: Main import script
- `cloudflare-worker.js`: Cloudflare Worker script for image proxy
- `requirements.txt`: Python dependencies
- `.env`: Configuration file for API keys

## Notes

- The script handles URL-encoded characters in titles
- Images are processed in batches to respect API limits
- Failed uploads are marked with ⚠️ in Notion
- Progress is logged to console with ✅ for success and ❌ for failures 