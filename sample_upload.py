# Copyright 2023, John Mueller
# This code is MIT License; the API is GPG licensed.
# SPDX-FileCopyrightText: 2023 John Mueller
# SPDX-License-Identifier: MIT
# https://github.com/softplus/lightroom-cc-api
#
# Sample usage of Lighthouse library / API

from dotenv import dotenv_values
from lightroom import Lightroom
from datetime import datetime

# get IDs & TOKEN, activate API
config = dotenv_values(".env")  
lr_api = Lightroom(config["LR_CLIENT_ID"], config["LR_ACCESS_TOKEN"])
catalog = lr_api.catalog_api()

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
