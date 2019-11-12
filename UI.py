#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
# from tkcalendar import Calendar, DateEntry


class UI(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Spotify Playlist Creator")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        
        lbl = Label(self, text="News")
        lbl.grid(row=0, pady=4, padx=5)

        lb2 = Label(self, text="Playlist")
        lb2.grid(row=0, column=2,pady=4, padx=5)

        listBox = Listbox(self)
        listBox.grid(row=1, column=0, columnspan=2, rowspan=1, padx=5, sticky=E+W+S+N)
        self.news_list = listBox

        area2 = Text(self)
        area2.grid(row=1, column=2, columnspan=2, rowspan=1,padx=5, sticky=E+W+S+N)

        quit_btn = Button(self, text="Quit")
        quit_btn.grid(row=5, column=0, padx=5)

        save_btn = Button(self, text="Save Playlist")
        save_btn.grid(row=5, column=3)


    # Display news data within column
    def render_news(self, news):
        for article in news:
            self.news_list.insert(END, article['title'])
