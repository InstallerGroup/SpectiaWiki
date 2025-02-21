// Cloudflare Worker script for transforming image URLs
// This script acts as a proxy between Notion and Cloudflare Images
// Replace this with your actual worker script

// Example URL format:
// Input: https://notionimage.kring.com/images/<image_id>/_5OKbt1LGRngtcb5j60bCA.png
// Output: https://imagedelivery.net/_5OKbt1LGRngtcb5j60bCA/<image_id>/public 


export default {
    async fetch(request) {
      const url = new URL(request.url);
  
      // Extract path segments from the incoming URL
      const pathParts = url.pathname.split('/').filter(Boolean); // Removes empty segments
  
      // Validate the path structure
      if (pathParts.length !== 3) {
        return new Response("Invalid URL format. Expected: /images/<image_id>/<account_id>.ext", { status: 400 });
      }
  
      // Extract components
      const [_, imageId, accountHashWithExtension] = pathParts; // The first part is "images"
      const accountHash = accountHashWithExtension.split('.')[0]; // Remove the ".ext" (e.g., ".png")
  
      // Construct the Cloudflare Images delivery URL
      const cloudflareImageUrl = `https://imagedelivery.net/${accountHash}/${imageId}/public`;
  
      // Fetch the image from Cloudflare Images
      return fetch(cloudflareImageUrl);
    }
  };
  