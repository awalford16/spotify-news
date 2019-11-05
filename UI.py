#!/usr/bin/env python3

from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from tkcalendar import Calendar, DateEntry


class Example(Frame):

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


        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=1,padx=5, sticky=E+W+S+N)

        area2 = Text(self)
        area2.grid(row=1, column=2, columnspan=2, rowspan=1,padx=5, sticky=E+W+S+N)


        
        hbtn = Button(self, text="Quit")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="Save Playlist")
        obtn.grid(row=5, column=3)


def main():

    root = Tk()
    root.geometry("800x800+800+800")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
