# lightroom-cc-api
A Python implementation of Adobe's [Creative Cloud Lightroom API](https://www.adobe.io/apis/creativecloud/lightroom/apidocs.html).

This is a fork from https://github.com/lou-k/lightroom-cc-api.
Original API is (c) Lou Kratz, GPLv3 Licensed.

Example code is (c) John Mueller, MIT Licensed.

## Disclaimer
This project is new and needs a lot of work. Use with caution.

## Pre-Requisities
You'll need two things:

* A Lightroom integration API key
* A token for your user.

See the Lightroom's [getting started](https://www.adobe.io/apis/creativecloud/lightroom/docs.html#!quickstart/integration.md) walks you through this, but it's not very inutitive.

[get_manual_token.md](get_manual_token.md) as a short guide for getting an Oauth2 token (valid for a day).

## Installation

The Python package can be installed via pip/git:
```
pip install git+https://github.com/softplus/lightroom-cc-api.git
```

In addition, you'll need libmagic. Install via:
* OSX: `brew install libmagic`
* Ubuntu: `sudo apt-get install libmagic`

## API Usage

The `Lightroom` API object has the `health`, `account`, and `catalog` endpoints.
It also provides catalog API:
```python

from lightroom import Lightroom
lr_api = Lightroom(api_key, token)
catalog = lr_api.catalog_api()
```

The catalog API contains all of of the `assets` and `albums` calls.

```python
# get the assets in the catalog
catalog.assets()
...
```

The catalog API also has two higher-level functions to help you add media to your Lightroom account:
```
# Uploads an image to lightroom
catalog.upload_image_file(path_to_image)

# Uploads an image to lightroom if it's not already in there.
catalog.upload_image_file_if_not_exists(path_to_image)
```

## Usage of sample script

Pull the whole repo, set up venv, install the requisites,
make your .env file, and run.
You will need to get a Lightroom API key to run the sample.
To get them, check out (get_manual_tokens.md).

```bash
git clone https://github.com/softplus/lightroom-cc-api
cd lightroom-cc-api

# setup virtualenv -- recommended
virtualenv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-sample.txt
cp .env.example .env
code .env # or your favorite editor
# add your client_id and client_secret
python3 sample_oauth.py
# done
deactivate
```

## Changes from original

I didn't want to be pushy with changes to the original, so I forked this
and wanted to use it to play around. This brought to light an annoying
bug in the Adobe Lightroom API, which hasn't had updates since 2021.
(The bug is that captureDate isn't used, which means all new images don't
have a date associated with them. Lightroom doesn't use EXIF either, so
you can't assign any dates.)

Changes:

* removed all "revision" functions & requests. This isn't documented in the
public API, so I assume it might not last. (But also, no updates since 2021,
so who really knows.)
* added support for image timestamp & capture date. Timestamp is shown in the
Lightroom UI, but capture date is lost on upload.
* added a sample script
* added a doc for getting a token
* add a sample script to use oauth2 to get a token

Todo:

* document the code more
