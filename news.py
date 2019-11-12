import requests
import json
import os
from newsapi import NewsApiClient
import datetime

class News:
    def __init__(self):
        with open(os.path.join('config', 'keys.json')) as config_file:
            config = json.load(config_file)

        self.news_api = NewsApiClient(api_key=config['news'])

    # Get latest news for the day
    def getNews(self, date):
        last_week = date - datetime.timedelta(days=7)

        self.articles = self.news_api.get_everything(q='test',
                                                    language='en',
                                                    sort_by='popularity',
                                                    from_param=str(last_week),
                                                    to=str(date))['articles']
                            
        return self.articles