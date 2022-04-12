# newspeak-shortlink

Configure your shortlink on the `newspeak.link` domain.
This service uses the rebrand.ly API to automatically sync the `shortlink.csv`.


## Adding your shortlink
---

Follow these steps if you want a shortlink added or edited.

`git clone https://github.com/clementbriens/newspeak-shortlink`

`git checkout -b your_branch`

Edit the `shortlinks.csv` file by adding your `slashtag` and `url`.

`git add shortlinks.csv`

`git commit -m "your commit message"`

`git push`

Open a pull request. Upon review, your branch will be merged and the shortlink system will be updated with the latest .csv file.

## Installation
---

Follow these steps if you want to run this service.

`git clone https://github.com/clementbriens/newspeak-shortlink`

`virtualenv env -p python3 && source env/bin/activate`

`pip install -r requirements.txt`

`mv config.ini.sample config.ini`

## Configuration
---

Add your Rebrandly API key and domain to `config.ini`. Alternatively, pass your domain and API Key as arguments.

## Usage

`python sync.py domain api_key`

## Github Action

The `update-shortlinks` action

## Attribution

This project is based on [go.talent.c4nada.ca](https://github.com/patcon/go.talent.c4nada.ca). Massive thanks to @patcon for the help and inspiration.
Check out these links for further info on shortlinks:

* [Shortlinks as common infrastructure](https://hackmd.io/@patcon/shortlinks-about)
* [spreadsheet2shortlinks](https://github.com/hyphacoop/spreadsheet2shortlinks)
* https://hackmd.io/@patcon/r1XKh-OJS
