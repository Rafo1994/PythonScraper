import requests
from dotenv import dotenv_values

config = dotenv_values()

api_key = config['API_KEY']
url = config['URL_TO_SCRAPE']

payload = {'api_key': api_key, 'url': url}

r = requests.post('http://api.scraperapi.com', params=payload)

file = open("../scraped.txt", "w+")

file.write(r.text)

file.close()