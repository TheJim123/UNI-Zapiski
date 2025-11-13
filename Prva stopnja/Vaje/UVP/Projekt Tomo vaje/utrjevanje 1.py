## Razdalje med točkami
#
# 1. naloga
# Sestavite funkcijo `ravninska_razdalja(x1, y1, x2, y2)`, ki vrne
# razdaljo med točkama (`x1`, `y1`) in (`x2`, `y2`).
# 
#     >>> ravninska_razdalja(1, 2, 3, 4)
#     2.82842712475
#

def ravninska_razdalja(x1, y1, x2, y2):
    return ((x1 - x2)** 2 + (y1 - y2) ** 2) ** 0.5
  
#
# 2. naloga
# Sestavite funkcijo `polarna_razdalja(r1, fi1, r2, fi2)`, ki vrne
# razdaljo med točkama (`r1`, `fi1`) in (`r2`, `fi2`) v ravnini, pri
# čemer so koordinate v polarnem zapisu, koti pa so izraženi v stopinjah.
# 
#     >>> polarna_razdalja(1, 30, 4, 90)
#     3.60555127546
#

import math as m
def v_radiane(x):
    return x * m.pi / 180
def polarna_razdalja(r1, fi1, r2, fi2):
    psi1 = v_radiane(fi1)
    psi2 = v_radiane(fi2)
    x1 = r1 * m.cos(psi1)
    y1 = r1 * m.sin(psi1)
    x2 = r2 * m.cos(psi2)
    y2 = r2 * m.sin(psi2)
    return ravninska_razdalja(x1, y1, x2, y2)


## Delne vsote vrst
#
# 1. naloga
# Napišite funkcijo `vsota_potenc(n, k)`, ki izračuna vsoto
#    $$1^k + 2^k + ... + n^k$$
#

def vsota_potenc(n, k):
    vsota = 0
    for i in range(1, n+1):
        vsota += i ** k
    return vsota

#
# 2. naloga
# Sestavite funkcijo `vsota_harmonicne(n)`, ki izračuna delno vsoto
#    $$1 + 1 / 2 + 1 / 3 + ... + 1 / n$$
#

def vsota_harmonicne(n):
    return vsota_potenc(n, -1)

#
# 3. naloga
# Sestavite funkcijo `divergenca_harmonicne(n)`, ki izračuna število
# členov harmonične vrste, ki jih je treba sešteti, da bo njihova delna
# vsota večja od števila `n`.
#

def divergenca_harmonicne(n):
    i = 1
    while vsota_harmonicne(i) < n:
        i += 1
    return i

#
# 4. naloga
# Sestavite funkcijo `eksponentna(n)`, ki izračuna delno vsoto:
#    $$1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / n!$$
#

import math as m

def eksponentna(n):
    vsota = 0
    for i in range(n+1):
        vsota += (1 / m.factorial(i))
    return vsota

## Palindromi
#
# 1. naloga
# Sestavite funkcijo `palindrom(niz)`, ki vrne `True` kadar je `niz`
# palindrom, in `False` sicer.
#

def palindrom(niz):
    for i in range(len(niz)):
        if niz[i] != niz[-(i+1)]:
            return False
    return True

#
# 2. naloga
# Pravimo, da je beseda praktično palindrom, če ji je treba zbrisati natanko
# eno črko, da bi postala palindrom. Primer je beseda `kolo`, ki ji
# moramo zbrisati črko `k`, pa postane palindrom `olo`.
# 
# Sestavite funkcijo `prakticno_palindrom(niz)`, ki preveri, ali je `niz`
# priktično palindrom. Vse znake (tudi presledke) v besedi obravnavamo enako.
#

def prakticno_palindrom(niz):
    for znak in niz:
        indeks = niz.index(znak)
        brez_znaka = niz[:indeks] + niz[indeks+1:]
        if palindrom(brez_znaka):
            return True
    return False

#
# 3. naloga
# Pravimo, da je beseda skoraj palindrom, če ji je treba dodati ali 
# izbrisati natanko eno črko oziroma zamenjati natanko eno črko z drugo, 
# da bi postala palindrom. Primeri:
# 
# - `robot`, kjer moramo `t` zamenjati z `r`,
# - `jana`, kjer moramo na konec dodati `j`.
# 
# Sestavite funkcijo `skoraj_palindrom(niz)`, ki preveri, ali je `niz`
# skoraj palindrom. Vse znake (tudi presledke) v besedi obravnavamo enako.
#
def skoraj_palindrom(niz):
    znaki = []
    for znak in niz:
        if znak not in znaki:
            znaki.append(znak)
    if prakticno_palindrom(niz):
        return True
    else:
        for znak in niz:
            indeks = niz.index(znak)
            for x in znaki:
                zamenjavni_niz = niz[:indeks] + x + niz[indeks+1:]
                dodajalni_niz = niz[:indeks] + x + niz[indeks:]
                if palindrom(zamenjavni_niz):
                    return True
                elif palindrom(dodajalni_niz):
                    return True
        return False
        
#Kasneje sem spoznal, da prakticno_palidrom(niz) vrne isti rezultat ce moramo
#znak dodati ali pa odvzeti. Krajsa funkcija bi torej bla:

# def skoraj_palindrom(niz):
#     if prakticno_palindrom(niz):
#         return True
#     else:
#         znaki = []
#         for znak in niz:
#             if znak not in znaki:
#                 znaki.append(znak)
#         for znak in niz:
#             indeks = niz.index(znak)
#             for x in znaki:
#                 novi_niz = niz[:indeks] + x + niz[indeks+1:]
#                 if palindrom(novi_niz):
#                     return True
#         return False


## Ogrlice
#
# Takrat, ko je upokojenki Marti dolgčas, vzame svoji dve posodici z belimi
# in rdečimi kroglicami ter začne nizati ogrlice. Te ogrlice bomo
# predstavili z nizi, sestavljenimi iz znakov `B` in `R`.
# Na primer: `"BBRBBRB"` in `"RRBBBBB"` sta dve izmed 21 možnih ogrlic,
# sestavljenih iz petih belih in dveh rdečih kroglic.
#
# 1. naloga
# Sestavite funkcijo `je_ogrlica(niz, b, r)`, ki preveri, ali `niz`
# predstavlja ogrlico iz `b` belih in `r` rdečih kroglic. Na primer:
# 
#     >>> je_ogrlica("BBRBBRB", 5, 2)
#     True
#     >>> je_ogrlica("RRBBBBB", 5, 2)
#     True
#     >>> je_ogrlica("BBRBBRB", 2, 5)
#     False
#     >>> je_ogrlica("BBRBBRBBB", 5, 2)
#     False
#     >>> je_ogrlica("BBRBBRBXY", 5, 2)
#     False
#

def je_ogrlica(niz, b, r):
    return niz.count('B') == b and niz.count('R') == r and len(niz) == b + r

#Verjetno boljsa resitev:
# def je_ogrlica(niz, b, r):
#     for znak in niz:
#         if znak == 'B':
#             b -= 1
#         elif znak == 'R':
#             r -= 1
#         else:
#             return False
#     return b == 0 and r == 0

#
# 2. naloga
# Z $O(b, r)$ označimo število različnih ogrlic, sestavljenih iz natanko
# $b$ belih in $r$ rdečih kroglic. Če je eno od števil $b$ ali $r$ enako
# nič, potem je $O(b, r) = 1$. Na primer, $O(5, 0) = 1$, saj iz petih
# belih kroglic lahko sestavimo le ogrlico `"BBBBB"`.
# 
# V nasprotnem primeru pa velja $O(b, r) = O(b - 1, r) + O(b, r - 1)$,
# saj se vsaka izmed ogrlic iz $b$ belih in $r$ rdečih kroglic:
# 
# 1. bodisi začne z belo kroglico, preostalih $b - 1$ belih in $r$ rdečih
#    kroglic pa lahko sestavimo na $O(b - 1, r)$ načinov,
# 2. bodisi začne z rdečo kroglico, preostalih $b$ belih in $r - 1$ rdečih
#    kroglic pa lahko sestavimo na $O(b, r - 1)$ načinov.
# 
# Sestavite funkcijo `stevilo_ogrlic(b, r)`, ki izračuna število vseh
# možnih ogrlic, sestavljenih iz natanko `b` belih in `r` rdečih kroglic.
# Na primer:
# 
#     >>> stevilo_ogrlic(5, 0)
#     1
#     >>> stevilo_ogrlic(5, 2)
#     21
#     >>> stevilo_ogrlic(4, 2)
#     15
#     >>> stevilo_ogrlic(5, 1)
#     6
#

def stevilo_ogrlic(b, r):
    if b == 0 or r == 0:
        return 1
    else:
        return stevilo_ogrlic(b-1, r) + stevilo_ogrlic(b, r-1)

## Hilbertova krivulja
#
# [Hilbertova krivulja](http://sl.wikipedia.org/wiki/Hilbertova_krivulja)
# je sestavljena iz dveh zrcalnih sestavnih delov. Osnovni del je oglata
# črka U (tj. Hilbertova krivulja prvega reda):
# 
#     |      |
#     |      |
#     |______|
# 
# Narišemo jo lahko v nasprotni smeri urinega kazalca, začenši levo zgoraj
# (tip A) ali pa v smeri urinega kazalca, začenši desno zgoraj (tip B).
# Hilbertova krivulja prvega reda je črka U tipa A. Hilbertova krivulja
# drugega reda zgleda takole:
# 
#       __    __                                      __      __
#       __|  |__                                      __|    |__
#      |   __   |     oz. razstavljeno na U-je     |      __      | 
#      |__|  |__|       in povezovalne dele:         |__|    |__|
# 
# Narišemo jo tako, da se zavrtimo v desno za 90 stopinj, nato narišemo
# Hilbertovo krivuljo prvega reda tipa B, nato se pomaknemo za eno enoto,
# se zavrtimo v levo za 90 stopinj, narišemo Hilbertovo krivuljo prvega
# reda tipa A, se spet pomaknemo za eno enoto, ponovno narišemo Hilbertovo
# krivuljo prvega reda tipa A, se zavrtimo v levo za 90, pomaknemo za
# eno enoto in končno narišemo še eno Hilbertovo krivuljo prvega reda
# tipa B, na koncu pa se zavrtimo desno za 90 stopinj, da pridemo na isto
# orientacijo kot smo jo imeli na začetku. Tako dobimo Hilbertovo krivuljo
# drugega reda tipa A. Za tip B samo izmenjamo tipa A in B ter vrtenji v
# levo in desno. Za Hilbertovo krivuljo poljubnega reda ravnamo enako, le
# da rekurzivno rišemo ustrezne krivulje nižjega reda. Bodite pozorni na to,
# da se orientacija želve po klicu funkcije ne spremeni.
# 
# Posebnost Hilbertove krivulje je, da v limiti povsem zapolni začetni
# kvadrat. Hausdorffova dimenzija limitne krivulje je torej 2 (karkoli že to
# pomeni `:-)`).
#
# 1. naloga
# Sestavite funkciji `hilbertova_krivulja_A(n, d)` in
# `hilbertova_krivulja_B(n, d)`, ki narišeta Hilbertovo krivuljo reda $n$
# tipa A oz. tipa B, pri tem pa je `d` velikost najkrajših daljic.
# Za $n = 0$ naj funkciji ne naredita ničesar.
#

#
# 2. naloga
# Napisali bomo novo različico zgornjih dveh funkcij, tako da bo kot, za
# katerega se zavrti želva, parameter. Ker za želvo velja, da vrtenje v
# levo za negativni kot pomeni vrtenje v desno in obratno, lahko obe prejšnji
# funkciji združimo v eno samo.
# 
# Poimenujte to funkcijo `hilbertova_krivulja(n, d, fi=90)`, kjer je `fi`
# zgoraj omenjeni kot. Za vrednost `fi = 90` se naj funkcija obnaša tako kot
# `hilbertova_krivulja_A`, za kot `fi = -90` pa kot `hilbertova_krivulja_B`.
# Privzeta vrednost za `fi` naj bo `90`. Opazujte krivulje, ki jih dobite za
# različne vrednosti kota. Zanimive so predvsem vrednosti, ki so večje od 90.
#


## Blagajna
#
# Zaradi prepovedi pisanja blagajniških računov na roko so v lokalni prodajalni
# prisiljeni preiti na računalniško podprto blagajno.
# Bazo prodajnih artiklov so pripravili v obliki slovarja, kjer je ključ
# ime artikla, vrednost pa par, ki vsebuje maloprodajno ceno in stopnjo
# davka (v procentih), na primer takole:
# 
#     artikli = {
#         'ponev': (32.74, 22),
#         'knjiga': (18.60, 9.5),
#         'gugalnik': (153.22, 22),
#         'igrača': (12.18, 0),
#         'likalnik': (43.15, 9.5)
#     }
# 
# Tudi vsak izdan račun predstavimo v obliki slovarja. Ključ je ime
# kupljenega artikla, vrednost pa par, ki vsebuje količino (celo število)
# in popust (v procentih). Primeri:
# 
#     racun1 = {'igrača': (2, 0), 'ponev': (1, 20), 'knjiga': (5, 10)}
#     racun2 = {'likalnik': (1, 5), 'igrača': (1, 20)}
#     racun3 = {'knjiga': (1, 0), 'igrača': (1, 0), 'ponev': (2, 20)}
#
# 1. naloga
# Sestavite funkcijo `davcna_osnova(mpc, ddv)`, ki bo za dano maloprodajno
# ceno `mpc` in stopnjo davka `ddv` izračunala davčno osnovo, to je znesek,
# na katerega zaračunamo davek, da dobimo maloprodajno ceno. Izračunano
# davčno osnovo zaokrožite na dve decimalni mesti. Zgled:
# 
#     >>> davcna_osnova(244.13, 22)
#     200.11
#     >>> davcna_osnova(1683.76, 9.5)
#     1537.68
#

def davcna_osnova(mpc, ddv):
    return float('{0:.2f}'.format(mpc * 100/(100+ddv)))

#
# 2. naloga
# Sestavite funkcijo `znesek_racuna(artikli, racun)`, ki izračuna, koliko
# mora kupec plačati za kupljeno blago. Končni znesek zaokrožite na dve
# decimalni mesti. Zgled:
# 
#     >>> znesek_racuna(artikli, racun1)
#     134.25
# 
# Predpostavite, da so na računu le artikli, ki so v s slovarjem podani bazi `artikli`
#

def znesek_racuna(artikli, racun):
    vsota = 0
    for x, y in racun.items():
        for k, v in artikli.items():
            if k == x:
                cena_enega = v[0]
                kolicina = y[0]
                popust = y[1]
                znesek = cena_enega * kolicina *(1 - popust/100)
                vsota += znesek
    return float('{0:.2f}'.format(vsota))

# Lepse, krajse, rajse:
# def znesek_racuna(artikli, racun):
#     vsota = 0
#     for artikel in racun:
#         cena = artikli[artikel][0]
#         kolicina = racun[artikel][0]
#         popust = racun[artikel][1]
#         znesek = kolicina * cena * (1 - popust / 100)
#         vsota += znesek
#     return round(vsota, 2)

#
# 3. naloga
# Sestavite funkcijo `davcni_obracun(artikli, racun)`, ki sestavi
# specifikacijo davka za dani račun. Specifikacijo davka predstavimo
# s slovarjem, kjer so ključi davčne stopnje, vrednosti pa vsote
# davčnih osnov za kupljene artikle s takšno davčno stopnjo. Uporabite
# funkcijo `davcna_osnova` iz prve podnaloge! Končni zneski naj bodo
# zaokroženi na dve decimalni mesti. Zgled:
# 
#     >>> davcni_obracun(artikli, racun1)
#     {0: 24.36, 9.5: 76.44, 22: 21.47}
#

def davcni_obracun(artikli, racun):
    obracun = {}
    for artikel, (kolicina, popust) in racun.items():
        cena_enega, ddv = artikli[artikel]
        znesek = kolicina * cena_enega * (1 - popust / 100)
        osnova = davcna_osnova(znesek, ddv)
        obracun[ddv] = obracun.get(ddv, 0) + osnova
    return obracun

#Nisem vedel kak resit, tak da je resitev kr uradna.  

#
# 4. naloga
# Ob koncu delovnega dneva nas zanima, koliko katerega artikla smo prodali,
# ločeno po različnih popustih, ki smo jih priznavali. Takšen dnevni obračun
# predstavimo s slovarjem, kjer so ključi pari oblike `(artikel, popust)`,
# vrednosti pa ustrezne prodane količine tega artikla. Sestavite funkcijo
# `dnevni_obracun(artikli, racuni)`, ki bo za dani seznam računov sestavila
# takšen dnevni obračun. Zgled:
# 
#     >>> dnevni_obracun(artikli, [racun1, racun2, racun3])
#     {('ponev', 20): 3, ('likalnik', 5): 1, ('knjiga', 0): 1, ('igrača', 0): 3, ('knjiga', 10): 5, ('igrača', 20): 1}
#

def dnevni_obracun(artikli, racuni):
    obracun = {}
    for racun in racuni:
        for artikel, (kolicina, popust) in racun.items():
            kljuc = (artikel, popust)
            obracun[kljuc] = obracun.get(kljuc, 0) + kolicina
    return obracun


## Igra življenja
#
# [Igra življenja](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
# gre takole: Imamo matriko, katere elementi sta logični vrednosti `True`
# in `False`. Vrednost `True` pomeni, da je celica živa, vrednost `False`
# pa pomeni, da je celica mrtva. Celice (razen robnih) imajo po 8 sosedov:
# dva horizontalna, dve vertikalna in štiri diagonalne. Čas teče v
# diskretnih korakih. S trenutnim stanjem sveta je tudi stanje sveta
# v naslednjem koraku natanko določeno in sicer po naslednjih pravilih:
# 
# - Živa celica, ki ima manj kot 2 živa soseda, umre (zaradi osamljenosti).
# - Živa celica, ki ima 2 ali 3 žive sosede, preživi.
# - Živa celica, ki ima več kot 3 žive sosede, umre (zaradi prenaseljenosti).
# - Mrtva celica, ki ima natanko 3 žive sosede, oživi (reprodukcija).
# 
# Primeri matrik, ki predstavljajo stanje sveta:
# 
#     svet_1 = [
#         [False, False, False, False, False, False],
#         [False, False, False, True, False, False],
#         [False, True, False, False, True, False],
#         [False, True, False, False, True, False],
#         [False, False, True, False, False, False],
#         [False, False, False, False, False, False]
#     ]
# 
#     svet_2 = [
#         [False, False, False, False],
#         [False, True, True, False],
#         [False, True, True, False],
#         [False, False, False, False]
#     ]
# 
# Tukaj si lahko ogledate 
# [simulacijo](http://pmav.eu/stuff/javascript-game-of-life-v3.1.1/).
#
# 1. naloga
# Napišite funkcijo `zivi(svet, i, j)`, ki v svetu `svet` prešteje in
# vrne število živih sosedov celice v $i$-ti vrstici in $j$-tem stolpcu.
# Zgled (naj bo `svet_1` matrika, kot je definirana zgoraj):
# 
#     >>> zivi(svet_1, 2, 0)
#     2
# 
# _Opomba_: Kot je za Python običajno, se stolpci in vrstice začnejo
# številčiti pri 0.
#

#
# 2. naloga
# Napišite funkcijo `igra(svet)`, ki sestavi in vrne matriko, ki
# predstavlja novo stanje sveta. Štiri pravila, ki določajo novo stanje
# sveta, so opisana zgoraj.
# 
# Zgled (matrika `svet_1` naj bo enaka kot zgoraj):
# 
#     >>> igra(svet_1)
#     [[False, False, False, False, False, False],
#      [False, False, False, False, False, False],
#      [False, False, True, True, True, False],
#      [False, True, True, True, False, False],
#      [False, False, False, False, False, False],
#      [False, False, False, False, False, False]]
#

#
# 3. naloga
# Napišite funkcijo `populacija(svet, n)`, ki naredi `n` korakov igre
# življenje in na vsakem koraku prešteje število živih celic. Ta
# števila naj vrne v obliki seznama, ki ima $n + 1$ elementov – prvo
# število v seznamu naj bo število živih celic v začetnem svetu. Zgled
# (matrika `svet_1` naj bo enaka kot zgoraj):
# 
#     >>> populacija(svet_1, 3)
#     [6, 6, 6, 6]
# 
# Funkcijo bomo testirali še na naslednjih svetovih (poleg tistih dveh,
# ki sta podana zgoraj):
# 
#     svet_3 = [
#         [False, False, False, False, False, False],
#         [False, True, True, False, False, False],
#         [False, True, True, False, False, False],
#         [False, False, False, True, True, False],
#         [False, False, False, True, True, False],
#         [False, False, False, False, False, False]
#     ]
# 
#     svet_4 = [
#         [True, True, True],
#         [True, True, True],
#         [True, True, True]
#     ]
# 
# _Nasvet_: Najprej napišite pomožno funkcijo, ki prešteje število živih
# celic v matriki.
#


## Tabela v LaTeXu
#
# Tekač Marko ima v datoteki `tekaski_podatki.txt` spravljene podatke o
# svojih tekaških podvigih. Datoteka izgleda takole:
# 
#     09-04-2017,10,53
#     10-04-2017,12,1:01
#     12-04-2017,14,1:16
#     13-04-2017,8,39
# 
# V prvem stolpcu je shranjen podatek o datumu teka, drugi stopec vsebuje
# število pretečenih kilometrov, v tretjem stopcu pa je spravljen podatek
# o tem, koliko časa je tek vzel.
#
# 1. naloga
# Sestavite funkcijo `preberi_podatke(datoteka)`, ki prebere datoteko s podatki
# o teku in vrne slovar. Ključi naj bodo datumi tekov, vrednosti pa nabori,
# ki vsebujejo par `(dolzina, cas)`. Pri tem naj bo `cas` izražen v minutah.
# 
#     >>> preberi_podatke("tekaski_podatki.txt")
#     {'09-04-2017': (10.0, 53), '13-04-2017': (8.0, 39), '12-04-2017': (14.0, 76), '10-04-2017': (12.0, 61)}
#

def v_minutah(niz):
    indeks = niz.index(':')
    ure = int(niz[:indeks])
    minute = int(niz[indeks+1:])
    return ure + minute

def preberi_podatke(datoteka):
    with open(datoteka) as d:
        slovar = {}
        for vrstica in d:
            razbita = vrstica.split(',')
            datum = razbita[0]
            dolzina = int(razbita[1])
            cas = v_minutah(razbita[2])
            slovar[datum] = (dolzina, cas)
        return slovar

#
# 2. naloga
# Sestavite funkcijo `povprecna_hitrost(dolzina, cas)`, ki ob dani pretečeni
# dolžini in času vrne povprečno hitrost teka, zaokroženo na dve decimalki.
# 
#     >>> povprecna_hitrost(10.0, 53)
#     0.19
#

def povprecna_hitrost(dolzina, cas):
    hitrost = float(dolzina / cas)
    return round(hitrost, 2)

#
# 3. naloga
# Sestavite funkcijo `pretvori_v_latex(vhod, izhod)`, ki prebere dano vhodno
# datoteko s podatki o teku in ustvari novo izhodno datoteko, ki izgleda takole:
# 
#     \documentclass[a4paper, 12pt]{amsart}
#     \usepackage[utf8]{inputenc}
#     \usepackage[slovene]{babel}
#     \usepackage{lmodern}
#     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     \pagestyle{empty}
#     \pagenumbering{gobble}
#     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     \usepackage{booktabs}
#     \usepackage{longtable}
#     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     \title{Marko te\v{c}e, Marko te\v{c}e}
#     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     \begin{document}
#     \maketitle
# 
# 
#     \begin{longtable}[c]{cccc}
#     \toprule
#     {\em Datum      } &
#     {\em Razdalja   } &
#     {\em Čas        } &
#     {\em Hitrost    }
#     \\ \midrule \endhead
# 
#     09. 04. 2017 & 10.0 & 53 & 0.19 \\
#     10. 04. 2017 & 12.0 & 61 & 0.20 \\
#     12. 04. 2017 & 14.0 & 76 & 0.18 \\
#     13. 04. 2017 & 8.0 & 39 & 0.21 \\
# 
#     \bottomrule
#     \end{longtable}
# 
#     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     \end{document}
#

def pretvori_v_latex(vhod, izhod):
    nizi = []
    for datum, (razdalja, cas) in preberi_podatke(vhod).items():
            novi_datum = datum.replace('-', '. ')
            hitrost = povprecna_hitrost(razdalja, cas)
            niz = '{} & {} & {} & {} \\'.format(novi_datum, razdalja, cas, hitrost)
            nizi.append(niz)
    with open(izhod, 'w') as i:
        print('\documentclass[a4paper, 12pt]{amsart}', file=i)
        print(r'\usepackage[utf8]{inputenc}', file=i)
        print(r'\usepackage[slovene]{babel}', file=i)
        print(r'\usepackage{lmodern}', file=i)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', file=i)
        print('\pagestyle{empty}', file=i)
        print('\pagenumbering{gobble}', file=i)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', file=i)
        print(r'\usepackage{booktabs}', file=i)
        print(r'\usepackage{longtable}', file=i)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', file=i)
        print('\title{Marko te\v{c}e, Marko te\v{c}e}', file=i)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', file=i)
        print('\begin{document}', file=i)
        print('\maketitle', file=i)
        print(' ', file=i)
        print(' ', file=i)
        print('\begin{longtable}[c]{cccc}', file=i)
        print('\toprule', file=i)
        print('{\em Datum      } &', file=i)
        print('{\em Razdalja   } &', file=i)
        print('{\em Čas        } &', file=i)
        print('{\em Hitrost    }', file=i)
        print('\\ \midrule \endhead', file=i)
        for n in nizi:
            print(n, file = i)
        print('\bottomrule', file=i)
        print('\end{longtable}', file=i)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', file=i)
        print('\end{document}', file=i)
