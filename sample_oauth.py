# Copyright 2023, John Mueller
# This code is MIT License; the API is GPG licensed.
# SPDX-FileCopyrightText: 2023 John Mueller
# SPDX-License-Identifier: MIT
# https://github.com/softplus/lightroom-cc-api
#
# Sample usage of Lighthouse library / API
#
# Note:
# - You must set https://oauth-generic-lander.glitch.me/ as redirect URI
# - Save client ID & client secret to the .env file
#

import requests
from dotenv import dotenv_values
from lightroom import Lightroom
from datetime import datetime
from urllib.parse import urlencode, quote_plus

# get IDs & TOKEN, activate API
config = dotenv_values(".env")

# do oauth bounce
page_url = "https://oauth-generic-lander.glitch.me/"
authorization_url = "https://ims-na1.adobelogin.com/ims/authorize?"
params = {
    "client_id" : config["LR_CLIENT_ID"],
    "scope" : "openid,lr_partner_apis,lr_partner_rendition_apis",
    "response_type" : "code",
    "redirect_uri" : page_url
}
querystring = urlencode(params, quote_via=quote_plus)
url = authorization_url + querystring
print(f"To authenticate, please visit: {url}")
print()
access_code = input("Copy the access token here: ")
if not access_code:
    print("Needs access token.")
    quit()

# get actual token
print("Authenticating ...")
url = "https://ims-na1.adobelogin.com/ims/token"
params = {
    "grant_type" : "authorization_code",
    "client_id" : config["LR_CLIENT_ID"],
    "client_secret" : config["LR_CLIENT_SECRET"],
    "code" : access_code
}
data_form = urlencode(params, quote_via=quote_plus)
headers = {"Content-Type": "application/x-www-form-urlencoded"}
r = requests.post(url, data=data_form, headers=headers)
config["LR_ACCESS_TOKEN"] = r.json()["access_token"]
# You can cache the access token -- it's valid for up to a day

# try login
try:
    lr_api = Lightroom(config["LR_CLIENT_ID"], config["LR_ACCESS_TOKEN"])
    catalog = lr_api.catalog_api()
except Exception as e:
    print("Lightroom API request failed:")
    print(e)
    quit()

# we're in!
print("Authenticated!")

# File to upload
image_filename = "sample.jpg"
mime_type = lr_api.__get_mime_type_mapped__(image_filename)

# check we can access the API
print("Lightroom API health: " + str(lr_api.health()))

# create new asset (before uploading -> need asset_id)
asset_id = catalog.create_new_asset_from_file(image_filename, "image", 
                                              capture_date=datetime.utcnow())
print(f"New asset-id: {asset_id}")

# upload the image
with open(image_filename, "rb") as f:
    catalog.put_master(asset_id, f, mime_type)

# done!
print("Uploaded file.")

# check that we can access it ...
asset_data = catalog.asset(asset_id)
print("Asset data:")
print(asset_data)

# done
