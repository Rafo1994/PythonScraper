import requests
from dotenv import dotenv_values

class ApiScraper:

    def __init__(self):
        config = dotenv_values()
        self.apiKey = config['API_KEY']
        self.url = config['URL_TO_SCRAPE']

    def getApiKey(self):
        config = dotenv_values()
        return config['API_KEY']
    def getRequestUrl(self):
        return {'api_key': self.apiKey, 'url': self.url}

    def sendRequest(self):
        file = open("./test/scraped.txt", "w+")
        r = requests.post('http://api.scraperapi.com', params=self.getRequestUrl()).text
        file.write(r)

        file.close()
        return r