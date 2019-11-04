import requests
import json
import os

class News:
    def __init__(self):
        with open(os.path.join('config', 'keys.json')) as config_file:
            config = json.load(config_file)

        self.key = config['news']

    # Get latest news for the day
    def getNews(self, date):
        url = ('https://newsapi.org/v2/top-headlines?'
                'country=gb&'
                'sortBy=popularity&'
                f'from={date}&'
                f'apiKey={self.key}')
        
        return requests.get(url)
