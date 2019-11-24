import news
from datetime import datetime
from UI import UI
from tkinter import Tk, Text, BOTH, W, N, E, S
import spotify

def main():
    # Get API keys
    news_api = news.News()
    news_data = news_api.getNews(datetime.today())
    news_words = news_api.get_words()
    print(news_words)

    # Get spotify playlist
    playlist = spotify.addWords(news_words)

    # Load in UI
    root = Tk()
    root.geometry("800x800+800+800")

    # Congifure user interface
    app = UI()
    app.render_news(news_data)
    app.render_playlist(playlist)
    root.mainloop()

if __name__ == '__main__':
    main()
