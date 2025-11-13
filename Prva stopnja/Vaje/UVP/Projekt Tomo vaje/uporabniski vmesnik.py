## Ugani število
#
# 1. naloga
# Sestavite funkcijo `ugibanje(a, b)`, ki si izmisli naravno število med `a` in `b`,
# nato pa uporabnika sprašuje po tem številu tako dolgo, da ga ta ugane.
# Program naj deluje tako kot je prikazano na primeru.
# 
#     >>> ugibanje(1, 20)
#     Izmislil sem si število med 1 in 20. Ugani ga!
#     Vnesi število: 12
#     Ne, nimam tega števila v mislih. Poskusi znova!
#     Vnesi število: 15
#     Ne, nimam tega števila v mislih. Poskusi znova!
#     Vnesi število: 7
#     Bravo! Uganil si v 3. poskusu.
#
import random as r
def ugibanje(a, b):
    i = 1
    number = str(r.randint(a, b))
    print('Izmislil sem si število med {0} in {1}. Ugani ga!'.format(a, b))
    while True:
        attempt = input('Katero število sem si izmislil?')
        if attempt != number:
            print('Ne, nimam tega števila v mislih. Poskusi znova!')
            i += 1
        else:
            print('Bravo! Uganil si v {}. poskusu.'.format(i))
            break
#
# 2. naloga
# Sestavite funkcijo `ugibaj(a, b)`, ki bo dopolnitev prejšnje funkcije.
# Uporabniku naj v primeru neuspeha pove, ali je njegovo število preveliko ali premajhno.
# Ali je zdaj kaj lažje ugibati?
# 
#     >>> ugibaj(1, 100)
#     Izmislil sem si število med 1 in 100. Ugani ga!
#     Vnesi število: 50
#     Ne, tvoje število je premajhno. Poskusi znova!
#     Vnesi število: 75
#     Ne, tvoje število je preveliko. Poskusi znova!
#     Vnesi število: 62
#     Ne, tvoje število je premajhno. Poskusi znova!
#     Vnesi število: 67
#     Bravo! Uganil si v 4. poskusu.
#
def ugibaj(a, b):
    i = 1
    number = str(r.randint(a, b))
    print('Izmislil sem si število med {0} in {1}. Ugani ga!'.format(a, b))
    while True:
        attempt = input('Katero število sem si izmislil?')
        if attempt != number:
            i += 1
            if attempt < number:
                print('Ne, tvoje število je premajhno. Poskusi znova!')
            elif attempt > number:
                print('Ne, tvoje število je preveliko. Poskusi znova!')
        else:
            print('Bravo! Uganil si v {}. poskusu.'.format(i))
            break



## Semafor
#
# 1. naloga
# Sestavi preprosto aplikacijo Semafor, ki ima tri gumbe "zelena",
# "rumena" in "rdeča" ter eno področje, ki se obarva s primerno barvo,
# ko pritisnemo na dani gumb, [glej video](http://vimeo.com/34579738).
#
import tkinter as tk
#Make the model: This class contains all of the basic operations for the
#stats of your programe (in this case the light's colour)

RDECA, ZELENA, RUMENA = 'rdeca', 'zelena', 'rumena'
#These variables won't change, so you can use them without (m)any problems
class Model:
    def __init__(self):
        self.barva = RDECA

    def daj_na_zeleno(self):
        self.barva = ZELENA
        
    def daj_na_rumeno(self):
        self.barva = RUMENA

    def daj_na_rdeco(self):
        self.barva = RDECA

#Simple enough, these all just change the "state" of your traffic light, but don't
#do anything on the screen.

class Trafficlight:
    def __init__(self):
        self.semafor = Model()
        window = tk.Tk()
        self.light = tk.Canvas(window, width=150, height=200)
        gumb_zel = tk.Button(window, command=self.daj_na_zeleno, text='zelena')
        gumb_rde = tk.Button(window, command=self.daj_na_rdeco, text='rdeca')
        gumb_rum = tk.Button(window, command=self.daj_na_rumeno, text='rumena')
        self.light.pack()
        gumb_zel.pack()
        gumb_rde.pack()
        gumb_rum.pack()
        self.refresh()
        window.mainloop

    def daj_na_zeleno(self):
        self.semafor.daj_na_zeleno()
        self.refresh()

    def daj_na_rdeco(self):
        self.semafor.daj_na_rdeco()
        self.refresh()
        
    def daj_na_rumeno(self):
        self.semafor.daj_na_rumeno()
        self.refresh()

    def refresh(self):
        ime_barve = {RDECA : 'red', RUMENA : 'yellow', ZELENA : 'green'}
        self.light.delete('all')
        self.light.create_oval(25,25, 125, 125, fill=ime_barve[self.semafor.barva])



Trafficlight()



## Pretvornik iz € v $
#
# 1. naloga
# Sestavite preprost pretvornik iz evrov v dolarje, kot to prikazuje
# [video](http://vimeo.com/34579993).
#
import tkinter as tk
class Denar:
    def __init__(self, vrednost):
        if (vrednost * 0) == 0:
            self.value = vrednost
            
    def pretvori(self):
        return self.value * 1.2
def pretvorba():
    vrednost = int(vhod.get())
    denar = Denar(vrednost)
    izhod.configure(text = str(denar.pretvori()))
   
okno = tk.Tk()
################################################################################
left_frame = tk.Frame(okno)
vhod = tk.Entry(left_frame)
euro = tk.Label(left_frame, text = '€')
je_enako = tk.Label(left_frame, text = '=')
####################################################################################
right_frame = tk.Frame(okno)
izhod = tk.Label(right_frame, width= 20, text = '0')
dolar = tk.Label(right_frame, text='$')
gumb = tk.Button(right_frame, text='Pretvori', command = pretvorba)
####################################################################################
left_frame.grid(row = 5, column = 2)
right_frame.grid(row = 5, column = 6)
izhod.grid(row = 5, column = 5)
gumb.grid(row = 5, column = 8)
vhod.grid(row = 5, column = 2)
euro.grid(row = 5, column = 3)
je_enako.grid(row = 5, column = 4)
dolar.grid(row = 5, column = 6)
#####################################################################################
okno.mainloop()


## Prostoročno risanje
#
# 1. naloga
# Sestavi preprosto aplikacijo za prostoročno risanje,
# [glej video](http://vimeo.com/34579801).
#
import tkinter as tk
    
##def draw(event):
##    x = event.x
##    y = event.y
##    if old_x != None and old_y != None:
##        canvas.create_line(old_x, old_y, x, y)
##    old_x = x
##    old_y = y

class Paint:
    def __init__(self):
        self.x = None
        self.y = None
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, height = 500, width = 500)
        self.canvas.pack()
        self.window.bind('<B1-Motion>', self.draw)
        self.window.bind('<ButtonRelease-1>', self.end_line)
        #window.mainloop()

    def draw(self, event):
        x = event.x
        y = event.y
        if self.x != None and self.y != None:
            self.canvas.create_line(self.x, self.y, x, y)
        self.x = x
        self.y = y

    def end_line(self, event):
        self.x = None
        self.y = None

Paint()

