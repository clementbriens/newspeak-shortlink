import requests
import pandas as pd
import json
import configparser
import sys


class LinkSync():

    def __init__(self):
        print('[*] LinkSync started')
        try:
            self.config = configparser.ConfigParser()
            self.config.read('config.ini')
            self.domain = self.config['config']['domain']
            self.api_key = self.config['config']['api_key']
        except:
            self.config = False
            self.domain = sys.argv[1]
            self.api_key = sys.argv[2]

        self.url = 'https://api.rebrandly.com/v1'
        self.headers = {
          "Content-type": "application/json",
          "apikey": self.api_key
        }

    def list_all_links(self):
        all_links = dict()
        paginate = True
        id = ""
        while paginate:
            try:
                r = requests.get(self.url + "/links?limit=25&last={}".format(id),
                headers=self.headers)

                data = r.json()
                for d in data:
                    if d['slashtag'] not in all_links.keys():
                        all_links[d['slashtag']] = {'url' : d['destination'], 'date_added' : d['createdAt'], 'id' : d['id']}
                id = d['id']
                if len(data) != 25:
                    paginate = False
            except:
                print('[!] Could not fetch links from service. Configure your API creds.')
                sys.exit()
        return all_links


    def add_link(self, slashtag, url):
        if not url.startswith('https://') and not url.startswith('http://'):
            url = 'https://' + url
        payload = {
        'title' : url,
        'destination' : url,
        'domain' : {'fullName' : self.domain},
        'slashtag' : slashtag
        }
        r = requests.post(self.url + '/links/', data = json.dumps(payload), headers = self.headers)
        if r.status_code == 200:
            print('[*] Added /{} with {}'.format(slashtag, url))
        else:
            print('[!] {} Could not add link.'.format(r.status_code))

    def update_link(self, slashtag, url, id):
        if not url.startswith('https://') and not url.startswith('http://'):
            url = 'https://' + url
        payload = {
        'id' : id,
        'title' : url,
        'destination' : url,
        'shortUrl' : self.domain + '/'+ slashtag
        }
        r = requests.post(self.url + '/links/' + id, data = json.dumps(payload), headers = self.headers)
        if r.status_code == 200:
            print('[*] Updated /{} with {}'.format(slashtag, url))
        else:
            print('[!] {} Could not update link.'.format(r.status_code))

    def delete_link(self, id, slashtag):
        r = requests.delete(self.url + '/links/' + id, headers = self.headers)
        if r.status_code == 200:
            print('[*] Deleted {}'.format(slashtag))
        else:
            print('[!] {} Could not delete link.'.format(r.status_code))

    def export_csv(self, links):
        all_data = list()
        for slashtag in links.keys():
            data = dict()
            data['slashtag'] = slashtag
            for key in links[slashtag].keys():
                if key != 'id':
                    data[key] = links[slashtag][key]
            all_data.append(data)
        df = pd.DataFrame(all_data)
        df.to_csv('shortlinks.csv')


    def sync(self):
        changes = False
        links = self.list_all_links()
        df = pd.read_csv('shortlinks.csv')
        for index, row in df.iterrows():
            if not row['url'].startswith('https://') and not row['url'].startswith('http://'):
                row['url'] = 'https://' + row['url']
            if row['slashtag'] in links.keys() and row['url'] != links[row['slashtag']]['url']:
                print('[*] Updating', row['slashtag'], 'with', row['url'])
                self.update_link(row['slashtag'], row['url'], links[row['slashtag']]['id'])
                changes = True
            if row['slashtag'] not in links.keys():
                print('[*] Adding', row['slashtag'], 'with', row['url'])
                self.add_link(row['slashtag'], row['url'])
                changes = True
        for slashtag in links.keys():
            if slashtag not in df['slashtag'].unique():
                print('[*] Deleting {}'.format(slashtag))
                self.delete_link(links[slashtag]['id'], slashtag)
                changes = True
        if changes:
            links = self.list_all_links()
            self.export_csv(links)
        print('[*] Done.')

if __name__ == '__main__':
    ls = LinkSync()
    ls.sync()
