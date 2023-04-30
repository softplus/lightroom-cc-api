This HTML is served from https://oauth-generic-lander.glitch.me/

The OAuth server sends the user to this page after authenticating.
The URL includes a ?code=parameter with the authentication code.
We grab this from the URL and put it into a text box.
When the user clicks into the text box, it selects the full text and copies it into the clipboard.

Some Oauth providers have pages like this, Adobe doesn't, so we made our own.

The page does not include any external JavaScript, images, or references.
(Glitch may be injecting more though, YMMV).

The auth-code only works for your Client-ID, so even if it's leaked, it's not useful for others.

Uses default Glitch.com CSS.

MIT licensed.
