from tkinter import *
from tkinter import ttk
from winsound import *
import random
import time


NOPPAKUVAT = [ "1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif","map.gif" ]

LARGE_FONT = ("Verdana", 12)
XL_FONT = ("Verdana", 30)

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

        #Sivun otsikko
        label = Label(self, text="Risk Dices", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #Soittaa muusikin kerran ja jättää sen soimaan taustalle
        play = lambda: PlaySound('music.wav', SND_ASYNC)

        sivu3 = lambda: controller.show_frame(Musasivu)

        #Yhdistetään toiminnot jotta voidaan kustsua ne samaan aikaan
        def combine_funcs(play,sivu3):
            def combined_func(*args, **kwargs):
                for f in play,sivu3:
                    f(*args, **kwargs)

            return combined_func

        button = ttk.Button(self, text="Aloita",
                         command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Poistu", command=quit)

        button2.pack()

        button3 = ttk.Button(self,text="Risk II intro musiikki",
                             command= combine_funcs(play, sivu3))
        button3.pack()

class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.__sotilaat = 0
        self.__sotilaat1 = 0

        #Haetaan taustakuva ja noppiin liittyvät kuvat
        self.__noppakuvat = []
        for kuvatiedosto in NOPPAKUVAT:
            kuva = PhotoImage(file=kuvatiedosto)
            self.__noppakuvat.append(kuva)

        # Tuodaan taustakuva sivulle
        background_image = PhotoImage(file="map.gif")
        background_label = Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        label = Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home Page",
                         command=lambda: controller.show_frame(StartPage),
                             style="TButton",padding=6)
        button1.pack()

        self.__heitäButton = ttk.Button(self, text="Hyökkää",
                                        command=self.heitä, style="TButton",
                                        padding=6)
        self.__heitäButton.pack()

        ttk.Button(self, text="Uusi hyökkäys", command=self.alusta_peli,
               style="TButton",padding=6).pack()

        Label(self, text="Syötä hyökkääjien määrä").pack()
        self.__hyökkääjän_pisteet = Entry(self)
        self.__hyökkääjän_pisteet.pack()

        Label(self, text="Syötä puolustajien määrä").pack()
        self.__puolustajan_pisteet = Entry(self)
        self.__puolustajan_pisteet.pack()

        self.__noppakuvalabelit = []
        for i in range(NOPPIEN_LKM):
            uusi_label = Label(self, bg="brown")
            if i <= 2:
                uusi_label.pack(side=RIGHT)
            else:
                uusi_label.pack(side=LEFT)

            self.__noppakuvalabelit.append(uusi_label)

        self.__pistelabelit = []
        uusi_label = Label(self,text= '0', bg="brown", font=XL_FONT)
        uusi_label.pack(pady=10, padx=10,side=RIGHT)
        self.__pistelabelit.append(uusi_label)

        self.__pistelabelit1 = []
        uusi_label1 = Label(self,text='0', bg="brown", font=XL_FONT)
        uusi_label1.pack(pady=10, padx=10,side=LEFT)
        self.__pistelabelit1.append(uusi_label1)


        self.alusta_peli()

    def alusta_peli(self):

        # Talletetaan tieto, että noppia ei ole lukittu
        self.__nopat_käytössä = [True] * NOPPIEN_LKM

        # Tallennetaan myös noppien silmäluvut ohjelman laskentaa varten
        self.__silmäluvut = [1] * NOPPIEN_LKM

        # Nopat
        for label in self.__noppakuvalabelit:
            label.configure(image=self.__noppakuvat[0])

        self.päivitä_käyttöliittymän_tekstit()


    def päivitä_käyttöliittymän_tekstit(self):
        # Päivitetään kaikkien pelaajien pistemäärät näytölle
        for i in range(len(self.__pistelabelit)):
            self.__pistelabelit[i].configure(text= self.__sotilaat)

        for i in range(len(self.__pistelabelit1)):
            self.__pistelabelit1[i].configure(text=self.__sotilaat1)


    def heitä(self):
        """ Heittää kaikkia noppia."""
        lukulista1 = []     #
        lukulista2 = []
        laskuri_H = 0
        laskuri1_P = 0

        hyökkääjät = self.__hyökkääjän_pisteet.get()
        puolustajat = self.__puolustajan_pisteet.get()

        for i in range(10):
            for arvo in self.__noppakuvalabelit:
                nro = random.randint(1, 6)
                arvo.configure(image=self.__noppakuvat[nro - 1])
            self.update_idletasks()
            time.sleep(0.05)

        for i in range(NOPPIEN_LKM):
            if self.__nopat_käytössä[i] == True and i < 3:
                luku = random.randint(1, 6)
                lukulista1.append(luku)

            elif self.__nopat_käytössä[i] == True and i >= 3:
                luku1 = random.randint(1, 6)
                lukulista2.append(luku1)

        if max(lukulista1) > max(lukulista2):
            del lukulista1[lukulista1.index(max(lukulista1))]
            del lukulista2[lukulista2.index(max(lukulista2))]
            laskuri1_P += 1
            if max(lukulista1) > max(lukulista2):
                laskuri1_P += 1
            else:
                laskuri_H += 1
        else:
            laskuri_H += 1

        time.sleep(0.05)

        self.__sotilaat = str(int(hyökkääjät) - laskuri_H)
        self.__sotilaat1 = str(int(puolustajat) - laskuri1_P)

        self.päivitä_käyttöliittymän_tekstit()


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