# newspeak-shortlink

Configure your shortlink on the `newspeak.link` domain.
This service uses the rebrand.ly API to automatically sync the `shortlink.csv`.


## Adding your shortlink

Follow these steps if you want a shortlink added or edited.

`git clone https://github.com/clementbriens/newspeak-shortlink`

`git checkout -b your_branch`

Edit the `shortlinks.csv` file by adding your `slashtag` and `url`.

`git add shortlinks.csv`

`git commit -m "your commit message"`

`git push`

Open a pull request. Upon review, your branch will be merged and the shortlink system will be updated with the latest .csv file.

## Installation

Follow these steps if you want to run this service.

`git clone https://github.com/clementbriens/newspeak-shortlink`

`virtualenv env -p python3 && source env/bin/activate`

`pip install -r requirements.txt`

`mv config.ini.sample config.ini`

## Configuration

Add your Rebrandly API key and domain to `config.ini`.


## Attribution
Huge thanks to @patcon. This repo is a pale imitation of https://github.com/patcon/go.talent.c4nada.ca.

* https://github.com/g0v-network/link.g0v.network
* https://hackmd.io/@patcon/shortlinks-about
