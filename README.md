# Pepper
[![Build Status](https://travis-ci.org/geekyshacklebolt/pepper.svg?branch=master)](https://travis-ci.org/geekyshacklebolt/pepper)
[![codecov](https://codecov.io/gh/geekyshacklebolt/pepper/branch/master/graph/badge.svg)](https://codecov.io/gh/geekyshacklebolt/pepper)

An API to fetch profiles of facebook users using their PSID and associating messenger labels to them.

### Pre-requisites

* A facebook page (for utilizing messenger)
* A facebook app (to implement pepper API)
* A webhook setup (to get users PSIDs)

You may refer this [guide](https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start) to complete pre-requisites.

### Now get the pepper

* `git clone https://github.com/geekyshacklebolt/pepper.git`
* `cd pepper`
* `conda create -n pepper python==3.7.3 pip`
* `conda activate pepper`
* `pip install -r requirements/development.txt`

__NOTE__:
You are free to use any suitable tool for python virtual environment.

### Configure a bit

* `touch .env`

Please have a look at [.env.sample](./.env.sample), copy its content to `.env` file in the project root.

### Set it up

* `python manage.py migrate`
* `python manage.py check`
* `python manage.py run`

__NOTE__:
* You'll need to create a superuser to access API endpoints.

Creating a superuser is just one command

* `python manage.py superuser --username example_name --email example_email`

### Basic usage

Please explore [endpoints.md](docs/endpoints.md) to understand endpoints request/responses.

1. Once you create the page on facebook and get its `access_token` and `page_id`, then go the endpoint `/api/page` and feed your facebook page credentials

2. Then create a messenger label by accessing the endpoint `/api/label`

3. Send the list of PSIDs and a label identifier (which you want to associate with them) using endpoint `/api/psid`

__NOTE__:
An older version of the same API is available in branch [csv](https://github.com/GeekyShacklebolt/pepper/tree/csv) of this project that accepts PSID list from a `csv` file.

### Contributors

[Shiva Saxena](https://github.com/geekyshacklebolt)
