from tkinter import *
from tkinter import ttk
import random
import time



NOPPAKUVAT = [ "1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif","map.gif" ]

PELAAJIEN_LKM = 2
NOPPIEN_LKM = 5
HEITTOVUOROJA = 2


class Noppapeli:
    def __init__(self):
        self.__ikkuna = Tk()
        self.__ikkuna.title("Noppapeli")

        background_image = PhotoImage(file="map.gif")
        background_label = Label(self.__ikkuna, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        self.__pelivuoro = 0
        self.__pelaajien_pisteet = [0] * PELAAJIEN_LKM

        self.__dicti = {}


        self.__noppakuvat = []
        for kuvatiedosto in NOPPAKUVAT:
            kuva = PhotoImage(file=kuvatiedosto)
            self.__noppakuvat.append(kuva)

        # Nämä tekstit vain asetetaan käyttöliittymään. Niitä ei tarvitse
        # muokata pelin aikana, joten ei talleteta olion kenttiin.
        for i in range(PELAAJIEN_LKM):
            Label(self.__ikkuna, text="Pelaajan "+str(i+1)+" pistetilanne:",bg="brown")\
            .grid(row=i+5, column=3, sticky=E)

        self.__infoLabel = Label(self.__ikkuna,bg="brown")
        self.__infoLabel.grid(row=7, column=3, columnspan=2)

        self.__pistelabelit = []
        for i in range(PELAAJIEN_LKM):
            uusi_label = Label(self.__ikkuna,bg="brown")
            uusi_label.grid(row=i+5, column=4, sticky=E)
            self.__pistelabelit.append(uusi_label)

        self.__noppakuvalabelit = []
        for i in range(NOPPIEN_LKM):
            uusi_label = Label(self.__ikkuna,bg="brown")
            if i < 3:
                uusi_label.grid(row=0, column=2+i)
            else:
                uusi_label.grid(row=3, column=0+i)

            self.__noppakuvalabelit.append(uusi_label)

        self.__heitäButton = ttk.Button(self.__ikkuna, text="Hyökkää", command=self.heitä,style="TButton", padding=6)
        self.__heitäButton.grid(row=0, column=NOPPIEN_LKM+3)
        self.__lopetavuoroButton = Button(self.__ikkuna, text="lopeta hyökkäys", command=self.lopeta_vuoro,bg="brown")
        self.__lopetavuoroButton.grid(row=1, column=NOPPIEN_LKM+3)

        Button(self.__ikkuna, text="uusi hyökkäys", command=self.alusta_peli,bg="brown")\
            .grid(row=2, column=NOPPIEN_LKM+3)
        Button(self.__ikkuna, text="Poistu", command=self.__ikkuna.destroy,bg="brown")\
            .grid(row=4, column=NOPPIEN_LKM+3)

        self.alusta_peli()

    def alusta_peli(self):
        self.__pelivuoro = 0
        self.__heittokertoja = HEITTOVUOROJA
        self.__pelaajien_pisteet = [0] * PELAAJIEN_LKM
        self.__pelitilanneteksti = "Hyökkäys nro. "+str(self.__pelivuoro + 1)

        # Talletetaan tieto, että noppia ei ole lukittu
        self.__nopat_käytössä = [True] * NOPPIEN_LKM

        # Tallennetaan myös noppien silmäluvut ohjelman laskentaa varten
        self.__silmäluvut = [1] * NOPPIEN_LKM

        # Asetetaan kaikkien noppakuvien kohdalle ykkönen

        #Nopat
        for label in self.__noppakuvalabelit:
            label.configure(image=self.__noppakuvat[0],anchor=E)

        self.päivitä_käyttöliittymän_tekstit()




    def päivitä_käyttöliittymän_tekstit(self):
        # Päivitetään kaikkien pelaajien pistemäärät näytölle
        for i in range(len(self.__pistelabelit)):
            self.__pistelabelit[i].configure(text=self.__pelaajien_pisteet[i])

        # Päivitetään pelitilanneteksti näytölle
        self.__infoLabel.configure(text=self.__pelitilanneteksti)

    def lopeta_vuoro(self):
        if self.__pelivuoro < len(self.__pelaajien_pisteet)-1:
            self.__pelivuoro += 1
        else:
            self.__pelivuoro = 0
        self.__pelitilanneteksti = "Hyökkäys nro. "+str(self.__pelivuoro + 1)
        self.päivitä_käyttöliittymän_tekstit()

    def heitä(self):
        """ Heittää kaikkia noppia."""
        lukulista = []
        lukulista1 = []
        pelaajien_pisteet = 0
        lista = []
        a = 0
        summa = 0
        for i in range(10):
            for arvo in self.__noppakuvalabelit:
                nro = random.randint(1,6)
                arvo.configure(image=self.__noppakuvat[nro-1])
            self.__ikkuna.update_idletasks()
            time.sleep(0.05)
        for i in range(NOPPIEN_LKM):
            if self.__nopat_käytössä[i] == True and i < 3:
                luku = random.randint(1, 6)
                lukulista.append(luku)
                self.__silmäluvut[i - 1] = luku
                self.__noppakuvalabelit[i].configure(image=self.__noppakuvat[luku-1])
            elif self.__nopat_käytössä[i] == True and i >= 3:
                luku = random.randint(1, 6)
                lukulista1.append(luku)

                summa = sum(lukulista)

        self.__ikkuna.update_idletasks()
        time.sleep(0.05)


        self.__pelaajien_pisteet[self.__pelivuoro] += summa

        self.päivitä_käyttöliittymän_tekstit()

    def kaynnista(self):
        self.__ikkuna.mainloop()

def main():
    käli = Noppapeli()
    käli.kaynnista()


main()
