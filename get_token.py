"""
get_token.py - fetches a fresh Adobe access token automatically.
OPTIONAL: only needed for the fully-unattended setup (scheduled runs).
If you use the OAuth login in VS Code, you do NOT need this file.

Setup (one time):
1. Ask your Adobe admin for an "OAuth Server-to-Server" credential
   (Adobe Developer Console → your project → Credentials).
2. Fill in the three values below.
3. NEVER share or commit this file once filled in.

Uses only Python's built-in libraries - nothing to install.
"""
import json
import urllib.request
import urllib.parse

CLIENT_ID     = "<YOUR_CLIENT_ID>"
CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
SCOPES        = "openid,AdobeID,additional_info.projectedProductContext"

def get_token():
    data = urllib.parse.urlencode({
        "grant_type":    "client_credentials",
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope":         SCOPES,
    }).encode()
    req = urllib.request.Request(
        "https://ims-na1.adobelogin.com/ims/token/v3",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["access_token"]

if __name__ == "__main__":
    token = get_token()
    print(token)
    # Optional: write it straight into mcp.json's Authorization header
    # so the scheduled run always has a fresh token.
