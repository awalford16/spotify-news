import news
from datetime import datetime
from UI import UI
from tkinter import Tk, Text, BOTH, W, N, E, S

def main():
    # Get API keys
    news_api = news.News()
    news_data = news_api.getNews(datetime.today())

    # Load in UI
    root = Tk()
    root.geometry("800x800+800+800")

    # Congifure user interface
    app = UI()
    app.render_news(news_data)
    root.mainloop()

if __name__ == '__main__':
    main()
