from tkinter import *
from tkinter import ttk
from winsound import *
import random
import time


NOPPAKUVAT = [ "1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif","map.gif","battle.gif" ]

LARGE_FONT = ("Times", 30, "bold")
MEDIUM_FONT = ("Verdana", 12)

NOPPIEN_LKM = 5

class Noppapeli(Tk):

    def __init__(self):

        Tk.__init__(self)

        Tk.iconbitmap(self, default="icon.ico")
        Tk.wm_title(self,"Risk dices")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, Musasivu):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def gf(string):
    print(string)

class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        background_image = PhotoImage(file="battle.gif")
        background_label = Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image


        label = Label(self, text="Risk Dices", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        play = lambda: PlaySound('music.wav', SND_ASYNC)
        sivu3 = lambda: controller.show_frame(Musasivu)

        def combine_funcs(play,sivu3):
            def combined_func(*args, **kwargs):
                for f in play,sivu3:
                    f(*args, **kwargs)

            return combined_func

        button = ttk.Button(self, text="Aloita",
                         command=lambda: controller.show_frame(PageOne))
        button.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Musa Intro",
                             command=combine_funcs(play, sivu3))
        button2.pack(pady=10, padx=10)

        button3 = ttk.Button(self, text="Poistu",
                             command=quit)
        button3.pack(pady=10, padx=10)

class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        #Haetaan taustakuva ja noppiin liittyvät kuvat
        noppakuvat = []
        for kuvatiedosto in NOPPAKUVAT:
            kuva = PhotoImage(file=kuvatiedosto)
            noppakuvat.append(kuva)

        # Tuodaan taustakuva sivulle
        background_image = PhotoImage(file="map.gif")
        background_label = Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        label = Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home Page",
                         command=lambda: controller.show_frame(StartPage))
        button1.pack()

class Musasivu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Risk II Intro", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home Page",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = Noppapeli()
app.mainloop()