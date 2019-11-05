import news
from datetime import datetime

def main():
    # Get API keys
    news_data = news.News()
    print(news_data.getNews(datetime.today()))

if __name__ == '__main__':
    main()
