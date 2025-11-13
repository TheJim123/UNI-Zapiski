## Zajec
#
# Jože goji zajce. V zadnjih letih so se tako
# namnožili, da si Jože enostavno ne more več zapomniti vseh. Zato
# potrebuje primeren informacijski sistem. V pomoč mu sestavite razred,
# ki bo vseboval vse potrebne podatke o vsakem zajcu.
#
# 1. naloga
# Sestavite razred `Zajec` s konstruktorjem `__init__(self, teza, starost)`,
# ki predstavlja zajca z dano težo in starostjo. Vrednosti shranite v
# atributa z imenoma `teza` in `starost`.
#
class Zajec:
    def __init__(self, teza, starost):
        self.teza = teza
        self.starost = starost
#
# 2. naloga
# Sestavite metodo `nahrani(self, hrana)`, kjer je argument `hrana` teža
# hrane, ki jo damo zajcu. Pri hranjenju se teža zajca poveča za 30 %
# teže hrane, ki jo zajec poje. Zgled:
# 
#     >>> z = Zajec(5, 2)
#     >>> z.nahrani(2)
#     >>> z.teza
#     5.6
#
    def nahrani(self, hrana):
        self.teza += 0.3 * hrana
#
# 3. naloga
# Sestavite metodo `__str__(self)`, ki vrne predstavitev razreda `Zajec`
# z nizom oblike `'Zajec težak X kg, star Y let.'`.
# 
# Primer:
# 
#     >>> z = Zajec(5, 2)
#     >>> print(z)
#     'Zajec težak 5 kg, star 2 let.'
# 
# _Opomba_: Funkcija `print` na svojem argumentu pokliče metodo `__str__`
# in izpiše niz, ki ga ta metoda vrne. Metoda `__str__` običajno vrne
# razumljiv opis objekta, ki naj bi ga razumeli tudi ne-programerji.
#
    def __str__(self):
        return 'Zajec težak {0} kg, star {1} let.'.format(self.teza, self.starost)
#
# 4. naloga
# Sestavite še metodo `__repr__(self)`, ki vrne predstavitev razreda
# `Zajec` kot niz oblike `'Zajec(X, Y)'`, kjer je `X` teža, `Y` pa starost
# zajca.
# 
# Primer:
# 
#     >>> z = Zajec(5, 2)
#     >>> z
#     Zajec(5, 2)
# 
# _Opomba_: Če v interaktivni konzoli pokličemo nek objekt, se izpiše niz,
# ki ga vrne klic metode `__repr__` na tem objektu. Priporočilo je, da je
# niz, ki ga vrne metoda `__repr__`, veljavna programska koda v Pythonu, ki
# ustvari identično kopijo objekta.
#
    def __repr__(self):
        return 'Zajec({0}, {1})'.format(self.teza, self.starost)
#
# 5. naloga
# Sestavite metodo `__lt__(self, drugi)`, ki dva zajca primerja med sabo.
# Metoda naj vrne `True`, če je prvi zajec manjši od drugega in `False` sicer.
# 
# Manjši zajec je tisti, ki je lažji. Če pa imata zajca enako maso, je manjši
# tisti, ki je mlajši (tj. ima manjše število let).
# 
#     >>> Zajec(5, 3) < Zajec(6, 2)
#     True
#     >>> Zajec(3, 1) < Zajec(2, 2)
#     False
#     >>> Zajec(4, 3) < Zajec(4, 2)
#     False
#
    def __lt__(self, drugi):
        return (self.teza < drugi.teza) or ((self.teza == drugi.teza) and (self.starost < drugi.starost))
#
# 6. naloga
# Sestavite funkcijo `uredi(teze, starosti)`. Argumenta `teze` in `starosti`
# sta enako dolga seznama števil, kjer $i$-ti element predstavlja težo oz.
# starost $i$-tega zajca. Funkcija `uredi` naj ne bo znotraj razreda `Zajec`,
# saj ni objektna metoda, ampak je čisto običajna funkcija.
# 
# Funkcija naj ustvari seznam ustreznih primerkov razreda `Zajec`, ga uredi
# po velikosti glede na zgoraj opisano relacijo in ta seznam vrne kot rezultat.
# 
#     >>> l = uredi([5, 4, 4], [3, 2, 3])
#     >>> for z in l:
#     ...     print(z)
#     ...
#     Zajec težak 4 kg, star 2 let.
#     Zajec težak 4 kg, star 3 let.
#     Zajec težak 5 kg, star 3 let.
#
def uredi(teze, starosti):
    combos = []
    result = []
    for i in range(len(teze)):
        z = Zajec(teze[i], starosti[i])
        combos.append(z)
    return sorted(combos)
        
#More elegant way:
#def uredi(teze, starosti):
#    zajci = [Zajec(teze[i], starosti[i]) for i in range(len(teze))]
#    zajci.sort()
#    return zajci
    


## Bitni cekini
#
# Trenutno je na spletu zelo popularna digitalna valuta
# [Bitcoin](http://en.wikipedia.org/wiki/Bitcoin).
# Osnova za pošteno uporabo take valute so zapleteni kriptografski
# protokoli, mi pa bomo ubrali malo bolj poenostavljeno varianto ter
# sestavili razred `BitniCekin`, s katerim bomo predstavili račun nekega
# lastnika te valute.
#
# 1. naloga
# Sestavite razred `BitniCekin` s konstruktorjem `__init__(self, stanje)`,
# ki sprejme začetno stanje na računu uporabnika (v valuti Bitcoin).
# Atribut, v katerega shranite stanje, naj bo poimenovan `stanje`.
# 
# Argument `stanje` naj bo neobvezen in v primeru, ko ni podan, naj bo
# začetno stanje enako nič.
#
class BitniCekin:
    def __init__(self, stanje=0):
        self.stanje = stanje
#
# 2. naloga
# Sestavite metodo `__str__(self)`, ki predstavi stanje na računu v obliki:
# `'Število bitnih cekinov na računu: X'`
# 
# Primer:
# 
#     >>> racun = BitniCekin(6)
#     >>> print(racun)
#     Število bitnih cekinov na računu: 6
#
    def __str__(self):
        return 'Število bitnih cekinov na računu: {}'.format(self.stanje)
#
# 3. naloga
# Sestavite še metodo `__repr__(self)`, ki predstavi objekt z nizom
# oblike `'BitniCekin(X)'`, kjer je `X` stanje na računu.
# 
# Primer:
# 
#     >>> racun = BitniCekin(6)
#     >>> racun
#     BitniCekin(6)
#
    def __repr__(self):
        return 'BitniCekin({})'.format(self.stanje)
#
# 4. naloga
# Sestavite metodi `dvig(self, koliko)` in `polog(self, koliko)`, ki 
# dvigneta oz. položita ustrezno količino bitnih cekinov na račun.
# Predpostavimo, da bo vrednost argumenta `koliko` vedno nenegativno
# celo število.
# 
# Pri metodi `dvig` upoštevajte, da stanje na računu ne sme biti negativno.
# V takšnem primeru se dvig ne sme izvesti.
# 
# Metoda `dvig` naj vrne `True`, če je dvig uspel in `False`, če ni.
# Metoda `polog` naj vrne stanje na računu po pologu.
#
    def dvig(self, koliko):
        if koliko <= self.stanje:
            self.stanje -= koliko
            return True
        else:
            return False

    def polog(self, koliko):
        self.stanje += koliko
        return self.stanje
#
# 5. naloga
# Sestavite funkcijo `prenesi(racun1, racun2, koliko)`, ki iz računa `racun1`
# prenese `koliko` cekinov na račun `racun2`. Funkcija `prenesi` naj ne bo
# znotraj razreda `BitniCekin`, saj ni objektna metoda, ampak je čisto običajna
# funkcija.
# 
# Če na računu `racun1` ni dovolj denarja, se transakcija ne sme 
# izvršiti, torej mora stanje na obeh računih ostati nespremenjeno.
# Funkcija naj vrne uspešnost transakcije (`True`, če je transakcija uspela,
# in `False`, če ni).
#
def prenesi(racun1, racun2, koliko):
    if koliko > racun1.stanje:
        return False
    else:
        racun1.dvig(koliko)
        racun2.polog(koliko)
        return True


## Ulomki
#
# 1. naloga
# Izven razreda sestavite funkcijo `gcd(m, n)`, ki izračuna največji skupni
# delitelj števil `m` in `n`. Zgled:
# 
#     >>> gcd(35, 63)
#     7
#
#ne deluje dobro pri 2. podnalogi, zato bom uporabil uradno verzijo
##def gcd(m, n):
##    dividers = []
##    for i in range(1, max(m, n) + 1):
##        if (m % i == 0) and (n % i == 0):
##            dividers.append(i)
##    return max(dividers)
def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
def lcm(m, n):
    return m * n // gcd(m, n)
#
# 2. naloga
# Definirajte razred `Ulomek`, s katerim predstavimo ulomek. Števec in
# imenovalec sta celi števili, pri čemer je morebiten negativen predznak
# vedno v števcu. Ulomki naj bodo vedno okrajšani. Atributa naj se
# imenujeta `st` in `im`.
# 
# Najprej definirajte konstruktor `__init__(self, st, im)`. Zgled:
# 
#     >>> u = Ulomek(5, 20)
#     >>> u.st
#     1
#     >>> u.im
#     4
#
class Ulomek:
    def __init__(self, st, im):
        if im < 0:
            st = -st
            im = -im
        k = gcd(st, im)
        self.st = (st // k)
        self.im = (im // k)
#
# 3. naloga
# Definirajte metodo  `__str__(self)`, ki predstavi ulomek z nizom
# oblike `'st/im'`. Zgled:
# 
#     >>> u = Ulomek(5, 20)
#     >>> print(u)
#     1/4
#
    def __str__(self):
        return '{0}/{1}'.format((self.st), (self.im))
#
# 4. naloga
# Definirajte še metodo  `__repr__(self)`, ki predstavi ulomek z nizom
# oblike `'Ulomek(st, im)'`. Zgled:
# 
#     >>> u = Ulomek(5, 20)
#     >>> u
#     Ulomek(1, 4)
#
    def __repr__(self):
        return 'Ulomek({}, {})'.format(self.st, self.im)
#
# 5. naloga
# Definirajte metodo  `__eq__(self, other)`, ki vrne `True` če sta dva
# ulomka enaka, in `False` sicer. Zgled:
# 
#     >>> Ulomek(1, 3) == Ulomek(2, 3)
#     False
#     >>> Ulomek(2, 3) == Ulomek(10, 15)
#     True
#
# is apparently causing errors in the next task, so I'll use the official one
##    def __eq__(self, other):
##        return (self.st * other.im == other.st * self.im)
    def __eq__(self, other):
        return self.st == other.st and self.im == other.im
# =====================================================================@001736=
# 6. naloga
# Definirajte metodo  `__add__(self, other)`, ki vrne vsoto dveh ulomkov.
# Ko definirate to metodo, lahko ulomke seštevate kar z operatorjem `+`.
# Na primer:
# 
#     >>> Ulomek(1, 6) + Ulomek(1, 4)
#     Ulomek(5, 12)
#
    def __add__(self, other):
        return Ulomek(((self.st * other.im) + (other.st * self.im)),
                      self.im * other.im)
#
# 7. naloga
# Definirajte metodo  `__sub__(self, other)`, ki vrne razliko dveh ulomkov.
# Ko definirate to metodo, lahko ulomke odštevate kar z operatorjem `-`.
# Na primer:
# 
#     >>> Ulomek(1, 4) - Ulomek(1, 6)
#     Ulomek(1, 12)
#
    def __sub__(self, other):
        return Ulomek(((self.st * other.im) - (other.st * self.im)),
                      self.im * other.im)
#
# 8. naloga
# Definirajte metodo  `__mul__(self, other)`, ki vrne zmnožek dveh ulomkov.
# Ko definirate to metodo, lahko ulomke množite kar z operatorjem `*`.
# Na primer:
# 
#     >>> Ulomek(1, 3) * Ulomek(1, 2)
#     Ulomek(1, 6)
#
    def __mul__(self, other):
        return Ulomek(self.st * other.st, self.im * other.im)
#
# 9. naloga
# Definirajte metodo  `__truediv__(self, other)`, ki vrne kvocient dveh
# ulomkov. Ko definirate to metodo, lahko ulomke delite kar z operatorjem
# `/`. Na primer:
# 
#     >>> Ulomek(1, 6) / Ulomek(1, 4)
#     Ulomek(2, 3)
#
    def __truediv__(self, other):
        return Ulomek(self.st * other.im, self.im * other.st)
#
# 10. naloga
# Izven razreda `Ulomek` definirajte funkcijo `priblizek(n)`, ki vrne
# vsoto $$\frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + … + \frac{1}{n!}.$$
# Funkcija naj uporablja razred `Ulomek`. Zgled:
# 
#     >>> priblizek(5)
#     Ulomek(163, 60)
# 
# Ali je izračunana vrednost blizu števila $e$?
#
def fac(n):
    fakulteta = 1
    for i in range(n+1):
        if i == 0:
            fakulteta = fakulteta
        else:
            fakulteta *= i
    return fakulteta

def priblizek(n):
    vsota = Ulomek(0,1)
    for i in range(n+1):
        vsota += Ulomek(1, fac(i))
    return vsota


## Datumi
#
# Koledar, ki ga trenutno uporabljamo v krščanskem (zahodnem) svetu, se
# imenuje [gregorijanski koledar](http://sl.wikipedia.org/wiki/Gregorijanski_koledar).
# Pri tej nalogi bomo implementirali razred `Datum`, ki bo omogočal
# predstavitev datumov v gregorijanskem koledarju in računanje z njimi.
#
# 1. naloga
# Sestavite funkcijo `je_prestopno(leto)`, ki preveri, ali je dano `leto`
# prestopno (po gregorijanskem koledarju). Zgled:
# 
#     >>> je_prestopno(2004)
#     True
#     >>> je_prestopno(1900)
#     False
#
def je_prestopno(leto):
    if leto % 400 == 0:
        return True
    elif leto % 100 == 0:
        return False
    elif leto % 4 == 0:
        return True
    else:
        return False
# raje: def je_prestopno(leto):
# return leto % 4 == 0 and leto % 100 != 0 or leto % 400 == 0
        
#
# 2. naloga
# Sestavite funkcijo `stevilo_dni(leto)`, ki vrne število dni v danem letu.
# Zgled:
# 
#     >>> stevilo_dni(2015)
#     365
#     >>> stevilo_dni(2016)
#     366
# 
# _Nasvet_: Uporabite funkcijo `je_prestopno`.
#
def stevilo_dni(leto):
    if je_prestopno(leto):
        return 366
    else:
        return 365
#
# 3. naloga
# Sestavite funkcijo `dolzine_mesecev(leto)`, ki vrne seznam dolžine 12,
# ki ima za elemente števila dni po posameznih mesecih v danem letu.
# Zgled:
# 
#     >>> dolzine_mesecev(2015)
#     [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
def dolzine_mesecev(leto):
    if je_prestopno(leto):
        k = 29
    else:
        k = 28
    return [31, k, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# 4. naloga
# Definirajte razred `Datum`, s katerim predstavimo datum.
# Najprej sestavite konstruktor `__init__(self, dan, mesec, leto)`.
# Nastali objekt naj ima atribute `dan`, `mesec` in `leto`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> d.dan
#     8
#     >>> d.mesec
#     2
#     >>> d.leto
#     1849
#
class Datum:
    def __init__(self, dan, mesec, leto):
        self.dan = dan
        self.mesec = mesec
        self.leto = leto
#
# 5. naloga
# Sestavite metodo `__str__(self)`, ki predstavi datum v obliki
# `'dan. mesec. leto'`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> print(d)
#     8. 2. 1849
#
    def __str__(self):
        return '{0}. {1}. {2}'.format(self.dan, self.mesec, self.leto)
#
# 6. naloga
# Sestavite še metodo `__repr__(self)`, ki vrne niz oblike
# `'Datum(dan, mesec, leto)'`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> d
#     Datum(8, 2, 1849)
#
    def __repr__(self):
        return 'Datum({0}, {1}, {2})'.format(self.dan, self.mesec, self.leto)
#
# 7. naloga
# Sestavite metodo `je_veljaven(self)`, ki preveri, ali je datum
# veljaven. Zgled:
# 
#     >>> d1 = Datum(8, 2, 1849)
#     >>> d1.je_veljaven()
#     True
#     >>> d2 = Datum(5, 14, 2014)
#     >>> d2.je_veljaven()
#     False
#
    def je_veljaven(self):
        if self.mesec > 12:
            return False
        elif self.dan <= dolzine_mesecev(self.leto)[self.mesec-1]:
            return True
        else:
            return False
#
# 8. naloga
# Sestavite metodo `__lt__(self, other)`, ki datum primerja z drugim
# datumom (metoda naj vrne `True`, če je prvi datum manjši, in `False`,
# če ni).
# 
# Ko definirate to metodo, lahko datume primerjate kar z operatorjema
# `<` in `>`. Na primer:
# 
#     >>> Datum(31, 12, 1999) < Datum(1, 1, 2000)
#     True
#
    def __lt__(self, other):
        if self.leto < other.leto:
            return True
        elif self.leto == other.leto:
            if self.mesec < other.mesec:
                return True
            elif self.mesec == other.mesec:
                if self.dan < other.dan:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
# making life easier:
# def __lt__(self, other):
#     # Uporabimo kar Pythonovo vgrajeno leksikografsko primerjavo.
#     return (self.leto, self.mesec, self.dan) \
#         < (other.leto, other.mesec, other.dan)
#
# 9. naloga
# Sestavite metodo `__eq__(self, other)`, ki datum primerja z drugim
# datumom (metoda naj vrne `True`, če sta datuma enaka, in `False`,
# če nista).
# 
# Ko definirate to metodo, lahko datume primerjate kar z operatorjema
# `==` in `!=`. Na primer:
# 
#     >>> Datum(31, 12, 1999) != Datum(1, 1, 2000)
#     True
#
    def __eq__(self, other):
        return (self.leto, self.mesec, self.dan) == (other.leto, other.mesec, other.dan)
#
# 10. naloga
# Sestavite metodo `dan_v_letu(self)`, ki izračuna, koliko dni je minilo
# od začetka leta do danega datuma. Zgled:
# 
#     >>> d = Datum(1, 11, 2014)
#     >>> d.dan_v_letu()
#     305
# 
# _Nasvet_: Ali si lahko kako pomagate s funkcijo `dolzine_mesecev`?
#
    def dan_v_letu(self):
        meseci = dolzine_mesecev(self.leto)
        return self.dan + sum(meseci[:self.mesec - 1])
#
# 11. naloga
# Sestavite metodo `razlika(self, other)`, ki kot argument dobi še en
# objekt razreda `Datum` in vrne število dni med datumoma. Zgled:
# 
#     >>> d1 = Datum(1, 11, 2014)
#     >>> d2 = Datum(14, 10, 2014)
#     >>> d1.razlika(d2)
#     18
#
#zaradi lenobe uporabil uradno
    def razlika(self, other):
        if self < other:
            return -other.razlika(self)
        else:
            # Najprej preštejemo število dni med začetkoma let.
            razlika = sum(stevilo_dni(l) for l in range(other.leto, self.leto))
            # Nato upoštevamo še dni v posameznem letu.
            razlika += self.dan_v_letu()
            razlika -= other.dan_v_letu()
            return razlika
        def dni_od_zacetka(self):
            def stevilo_prestopnih_let(leto):
                return leto // 4 - leto // 100 + leto // 400
            return self.dan + sum(dolzine_mesecev(self.leto)[:self.mesec - 1]) + 365 * (self.leto - 1) + stevilo_prestopnih_let(self.leto - 1)
        # Alternativna rešitev
        #def razlika_alt(self, other):
         #   return self.dni_od_zacetka() - other.dni_od_zacetka()
#
# 12. naloga
# Sestavite metodo `dan_v_tednu(self)`, ki vrne številko dneva v tednu
# (1 = ponedeljek, 2 = torek, …, 7 = nedelja). Lahko si pomagate z
# [Zellerjevim obrazcem](http://en.wikipedia.org/wiki/Zeller's_congruence).
# Druga možnost je, da izračunate razliko med datumom `self` in nekim
# fiksnim datumom, za katerega že poznate dan v tednu. Zgled:
# 
#     >>> d = Datum(1, 11, 2014)
#     >>> d.dan_v_tednu()
#     6
#
# h = ((self.dan + (13(self.mesec +1)//5)+ (self.leto % 100) + ((self.leto % 100)//4) + 5 - (self.leto//100)) % 7)
    def dan_v_tednu(self):
        q = self.dan
        m = self.mesec
        if self.mesec == 1:
            m = 13
            self.leto -= 1
        elif self.mesec == 2:
            m = 14
            self.leto -= 1
        k = (self.leto % 100)
        j = (self.leto // 100)
        h = ((q + ((13 * (m + 1) // 5) + k + (k // 4) + (j // 4) + (5 * j)) % 7))
        d = ((h + 5) % 7) + 1
        return d
            
#
# 13. naloga
# Sestavite metodo `teden_v_letu(self)`, ki vrne številko tedna v letu.
# Nov teden se vedno začne s ponedeljkom. Prvi teden v letu lahko traja
# le en dan (če se začne na nedeljo) ali pa 7 dni (če se začne na
# ponedeljek). Zgled:
# 
#     >>> d = Datum(3, 11, 2014)
#     >>> d.teden_v_letu()
#     45
#
    def teden_v_letu(self):
        poslednja_nedelja = self.dan_v_letu() - self.dan_v_tednu()
        if poslednja_nedelja % 7 != 0:
            k = 1
        else:
            k = 0
        pretekle_nedelje = poslednja_nedelja // 7 + k
        return pretekle_nedelje + 1        
        
#
# 14. naloga
# Izven razreda `Datum` sestavite še funkcijo `datum(leto, dan)`,
# ki za parametra dobi leto in številko dneva v letu ter sestavi in
# vrne ustrezen datum. Zgled:
# 
#     >>> datum(2014, 305)
#     Datum(1, 11, 2014)
#
def datum(leto, dan):
    meseci = dolzine_mesecev(leto)
    mesec = 1
    for x in meseci:
        if dan - x > 0:
            dan -= x
            mesec += 1
        else:
            break
    return Datum(dan, mesec, leto)

# Uradno:
# def datum(leto, dan):
#     dolzine = dolzine_mesecev(leto)
#     mesec = 1
#     while dan > dolzine[mesec - 1]:
#         dan -= dolzine[mesec - 1]
#         mesec += 1
#     return Datum(dan, mesec, leto)
#
# While zanka je ocitno boljsa opcija, ne vem zakaj sem probal s for zanko,
# ki je po funkcionalnosti identicna while zanki


            

## Polinomi
#
# Definirajte razred `Polinom`, s katerim predstavimo polinom v
# spremenljivki $x$. Polinom predstavimo s seznamom njegovih koeficientov,
# kjer je $k$-ti element seznama koeficient pri $x^k$.
# 
# Na primer, polinom $x^3 + 2x + 7$ predstavimo s `Polinom([7, 2, 0, 1])`.
# Razmislite, kaj predstavlja `Polinom([])`. Zadnji koeficient v seznamu
# mora biti neničelen.
# 
# 1. naloga
# Sestavite konstruktor `__init__(self, koef)`, ki nastavi objektu
# nastavi atribut `koef` (koeficienti polinoma). Zgled:
# 
#     >>> p = Polinom([7, 2, 0, 1])
#     >>> p.koef
#     [7, 2, 0, 1]
# 
# _Pozor_: Če kasneje spremenimo seznam, ki smo ga kot argument podali
# konstruktorju, se koeficienti polinoma ne smejo premeniti. Seznama,
# ki smo ga podali kot argument, konstruktor prav tako ne sme spremeninjati.
# Zgled:
# 
#     >>> l = [2, 0, 1]
#     >>> p = Polinom(l)
#     >>> l.append(3)
#     >>> p.koef
#     [2, 0, 1]
#

#
# 2. naloga
# Sestavite metodo `stopnja(self)`, ki vrne stopnjo polinoma. Zgled:
# 
#     >>> p = Polinom([7, 2, 0, 1])
#     >>> p.stopnja()
#     3
# 
# _Opomba_: Za razpravo glede stopnje ničelnega polinoma glejte [članek
# na Wikipediji](http://en.wikipedia.org/wiki/Degree_of_a_polynomial#Degree_of_the_zero_polynomial).
#

#
# 3. naloga
# Sestavite metodo `__repr__(self)`, ki vrne niz oblike
# `'Polinom([a_0, …, a_n])'`, kjer so `a_0, …, a_n` koeficienti polinoma.
# Zgled:
# 
#     >>> p = Polinom([5, 0, 1])
#     >>> p
#     Polinom([5, 0, 1])
#

#
# 4. naloga
# Sestavite metodo `__eq__(self, other)` za primerjanje polinomov. Zgled:
# 
#     >>> Polinom([3, 2, 0, 1]) == Polinom([3, 2])
#     False
#     >>> Polinom([3, 2, 1, 0]) == Polinom([3, 2, 1])
#     True
#

#
# 5. naloga
# Sestavite metodo `__call__(self, x)`, ki izračuna in vrne vrednost
# polinoma v `x`. Pri izračunu vrednosti uporabite Hornerjev algoritem.
# Če definiramo metodo `__call__`, objekt postane "klicljiv" (tj. lahko
# ga kličemo, kakor da bi bil funkcija). Zgled:
# 
#     >>> p = Polinom([3, 2, 0, 1])
#     >>> p(1)
#     6
#     >>> p(-3)
#     -30
#     >>> p(0.725)
#     4.8310781249999994
#

#
# 6. naloga
# Sestavite metodo `__add__(self, other)` za seštevanje polinomov. Metoda
# naj sestavi in vrne nov objekt razreda `Polinom`, ki bo vsota polinomov
# `self` in `other`. Zgled:
# 
#     >>> Polinom([1, 0, 1]) + Polinom([4, 2])
#     Polinom([5, 2, 1])
# 
# _Pozor_: Pri seštevanju se lahko zgodi, da se nekateri koeficienti
# pokrajšajo: $(x^3 + 2x + 7) + (-x^3 - 2x + 10) = 17$.
#

#
# 7. naloga
# Sestavite metodo `__mul__(self, other)` za množenje polinomov. Metoda
# naj sestavi in vrne nov objekt razreda `Polinom`, ki bo produkt polinomov
# `self` in `other`. Zgled:
# 
#     >>> Polinom([1, 0, 1]) * Polinom([4, 2])
#     Polinom([4, 2, 4, 2])
#

#
# 8. naloga
# Sestavite metodo `odvod(self, k)`, sestavi in vrne nov polinom, ki bo
# $k$-ti odvod polinoma `self`. Argument `k` naj ima privzeto vrednost 1.
# Zgled:
# 
#     >>> p = Polinom([5, 1, 4, -3, 5, -1])
#     >>> p.odvod()
#     Polinom([1, 8, -9, 20, -5])
#     >>> p.odvod(2)
#     Polinom([8, -18, 60, -20])
#

#
# 9. naloga
# Sestavite metodo `__str__(self)`, ki predstavi polinom v čitljivi obliki,
# kot kaže primer:
# 
#     >>> p = Polinom([5, 1, 4, -3, 5, -1])
#     -x^5 + 5x^4 - 3x^3 + 4x^2 + x + 5
# 
# Za niz, ki ga funkcija vrne, naj velja naslednje:
# 
# * Polinom je sestavljen iz monomov oblike `ax^k`, kjer je `a` ustrezen
#   koeficient.
# * Monomi so med seboj povezani z znaki `+`; pred in za plusom je po en
#   presledek.
# * Namesto `x^1` bomo pisali samo `x`, `x^0` pa bomo izpustili in pisali
#   samo koeficient.
# * Če je koeficient 1, bomo namesto `1x^k` pisali `x^k`. Če je -1, bomo
#   namesto `-1x^k` pisali `-x^k`. To ne velja za prosti člen.
# * Če je koeficient negativen, bomo pri združevanju monomov uporabili
#   znak `-` namesto znaka `+`. Torej, namesto `ax^m + -bx^n` bomo pisali
#   `ax^m - bx^n`. To ne velja za vodilni člen.
# * Če je koeficient 0, bomo monom izpustili. To pravilo ne velja za
#   ničelni polinom.
#


