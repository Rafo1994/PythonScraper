import requests
import yaml

with open('config.yaml') as f:
    config = yaml.load(stream=f, Loader=yaml.FullLoader)

api_key = str(config['api_key'])
url = str(config['url_to_scrape'])

payload = {'api_key': api_key, 'url': url}

r = requests.post('http://api.scraperapi.com', params=payload)

file = open("scraped.txt", "w+")

file.write(r.text)