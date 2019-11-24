import requests
import json
import os
from newsapi import NewsApiClient
import datetime
import random
import string

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

	# Display news data within column
    def get_words(self):
        relevant_words = []
        for article in self.articles:
            words = list(article['title'].split(' '))
            while True:
                word = random.choice(words)
                if len(word) > 3:
                    word.translate(str.maketrans('', '', string.punctuation))
                    relevant_words.append(word)
                    break
        
        return relevant_words
            