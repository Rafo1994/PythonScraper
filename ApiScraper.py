import requests
from dotenv import dotenv_values

class ApiScraper:

    def __int__(self):
        config = dotenv_values()
        self.apiKey = config['API_KEY']
        self.urk = config['URL_TO_SCRAPE']

    def getRequestUrl(self):
        return {'api_key': self.api_key, 'url': self.url}

    def sendRequest(self):
        return requests.post('http://api.scraperapi.com', params=self.getRequestUrl())