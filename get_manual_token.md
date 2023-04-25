# Getting a token the manual way, for testing

1. Go to https://developer.adobe.com/console/projects
2. Click "Create new project"
3. Click "Add to project" / "API"
4. Select "Lightroom Services" ("Requires Adobe review" = if you want to support non-test users)
5. Click "Next"
6. Select "Oauth 2.0 / Web App"
7. Enter "https://adobeioruntime.net" as "Default redirect URI"
8. Enter "https://adobeioruntime\\.net" as "Redirect URI pattern *" (with \\)
9. Click "Save configured API"
10. You should now be on a dashboard page for your key, with "Get started", etc...
11. Copy the Client ID from there to the side
12. Click "Retrieve client secret" and copy the client secret to the side
13. Go to https://adobeioruntime.net/api/v1/web/io-solutions/adobe-oauth-playground/oauth.html
14. Copy your client ID and client secret into the fields
15. Enter "openid,lr_partner_apis,lr_partner_rendition_apis" into "Scopes"
16. Click "Generate Tokens"
17. Confirm approval
18. Congrats. You now have an access token! It's valid about a day. :-/

Into the .env file, copy them all:

```text
LR_CLIENT_ID="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
LR_CLIENT_SECRET="XXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
LR_ACCESS_TOKEN="SUPER_LONG_ACCESS_TOKEN_HERE"
```

Now you're all set (for a day).
