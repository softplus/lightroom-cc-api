# Using a custom oauth2 landing page

We'll use https://oauth-generic-lander.glitch.me/ - the page used by `sample_oauth.py`.
Copy this page and make your own ideally.
Or just use that page, it doesn't contain any 3rd party scripts (but please double-check).

0. Copy .env.example as .env
1. Go to https://developer.adobe.com/console/projects
2. Click "Create new project"
3. Click "Add to project" / "API"
4. Select "Lightroom Services" ("Requires Adobe review" = if you want to support non-test users)
5. Click "Next"
6. Select "Oauth 2.0 / Web App"
7. Enter "https://oauth-generic-lander.glitch.me/" as "Default redirect URI"
8. Enter "https://oauth-generic-lander\.glitch\.me/" as "Redirect URI pattern *" (with \.'s)
9. Click "Save configured API"
10. You should now be on a dashboard page for your key, with "Get started", etc...
11. Copy the Client ID from there to the .env file
12. Click "Retrieve client secret" and copy the client secret to the .env file

The .env file should then contain something like this:

```text
LR_CLIENT_ID="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
LR_CLIENT_SECRET="XXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

Now you're all set! Run the sample script using:

```bash
virtualenv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-sample.txt
# make sure to have the .env file configured
python3 sample_oauth.py
# done
deactivate
```

The HTML & CSS for https://oauth-generic-lander.glitch.me/ is in `/sample_html`.
I hosted it on https://glitch.com/, but any web hosting will work (static hosting is fine).

Advanced apps that run on a local workstation can use `http://localhost/` as a redirect address, and pick up the code there.
This requires running a local webserver, which might no be suited for all use-cases (eg, headless, chat-bot).
