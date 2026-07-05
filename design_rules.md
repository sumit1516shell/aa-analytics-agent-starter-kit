{
  "_comment": "ALTERNATIVE: header-based auth. Copy over mcp.json ONLY if OAuth login doesn't work in your org. NEVER commit real values.",
  "servers": {
    "adobe-analytics": {
      "type": "http",
      "url": "https://aa-mcp.adobe.io/mcp",
      "headers": {
        "Authorization": "Bearer <PASTE_TOKEN_FROM_get_token.py>",
        "x-gw-ims-org-id": "<YOUR_ORG_ID>@AdobeOrg",
        "x-api-key": "<YOUR_API_KEY>",
        "x-global-company-id": "<YOUR_COMPANY_ID>"
      }
    }
  }
}
