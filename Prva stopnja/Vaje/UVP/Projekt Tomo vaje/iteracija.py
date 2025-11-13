## Enostavne naloge z generatorji
#
# 1. naloga
# Napišite generator `stevke(n)`, ki generira števke naravnega števila
# `n` začenši z enicami (s skrajno desno števko).
# 
#     >>> [x for x in stevke(1337)]
#     [7, 3, 3, 1]
#

def stevke(n):
    while n > 0:
        c = n % 10
        n //= 10
        yield c

#
# 2. naloga
# Sestavite generator `potence_naravnih(k)`, ki kot argument dobi število
# `k` in generira (neskončno) zaporedje $1^k, 2^k, 3^k, 4^k, \ldots$
# 
#     >>> g = potence_naravnih(2)
#     >>> [next(g) for i in range(10)]
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#

def potence_naravnih(k):
    i=1
    while k:
        yield i ** k
        i += 1

#
# 3. naloga
# Sestavite generator `fakultete(n)`, ki kot argument dobi nenegativno
# celo število `n` in generira (neskončno) zaporedje $n!, (n+1)!, (n+2)!, \ldots$
# 
#     >>> g = fakultete(0)
#     >>> [next(g) for i in range(10)]
#     [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
#

def fakulteta(n):
    produkt = 1
    if n == 0:
        return produkt
    else:
        for i in range(1, n+1):
            produkt *= i
        return produkt

def fakultete(n):
    while True:
        i = fakulteta(n)
        yield i
        n +=1

#
# 4. naloga
# Spomnimo se, da je Collatzovo zaporedje z začetnim členom $a_0$ definirano
# s predpisom $a_{i+1} = a_i / 2$, če je $a_i$ sodo, in $a_{i+1} = 3 a_i + 1$ sicer.
# 
# Sestavite generator `collatz(n)`, ki kot argument dobi naravno število `n`
# in generira Collatzovo zaporedje z začetnim členom `n`. Generiranje naj se
# konča, ko pridemo do števila 1.
# 
#     >>> [x for x in collatz(20)]
#     [20, 10, 5, 16, 8, 4, 2, 1]
#

def collatz(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield n

#
# 5. naloga
# Sestavite generator `delitelji(n)`, ki kot argument dobi naravno število
# `n` in generira njegove delitelje (od najmanjšega proti največjemu).
# 
#     >>> [x for x in delitelji(12)]
#     [1, 2, 3, 4, 6, 12]
#

def delitelji(n):
    deliteljcki = []
    i = 1
    while i * i < n:
        if n % i == 0:
            yield i
            deliteljcki.append( n // i)
        i += 1
    if i * i == n:
        yield i
    while len(deliteljcki) > 0:
        yield deliteljcki.pop()

#
# 6. naloga
# Sestavite generator `ucinkoviti_delitelji(n)`, ki deluje tako kot generator
# `delitelji(n)`, vendar poskrbite, da deluje učinkovito, saj bomo njegovo
# delovanje preverili na velikih številih. Najbolje je, da že generator
# `delitelji` napišete učinkovito, nato pa generator `ucinkoviti_delitelji`
# definirate kar kot:
# 
#     ucinkoviti_delitelji = delitelji
#

def ucinkoviti_delitelji(n):
    return delitelji(n)


## Bliskovito hitri telefonski imenik
#
# Zaradi hitrejšega iskanja po telefonskem imeniku imamo telefonske številke
# shranjene po skupinah glede na začetnico imena. Na primer:
# 
#     bliskoviti_primer = {
#         'J': [('Jure', '0248987522')],
#         'M': [('Minka', '0354228532'), ('Matija', '0162378332')]
#     }
#
# 1. naloga
# Napišite funckijo `dodaj_enega`, ki kot prvi argument sprejme imenik,
# preostale argumente, ki so pari, pa doda vanj. Funkcija naj ne vrača ničesar.
# 
#     >>> imenik = {}
#     >>> dodaj_enega(imenik, 'X1', '1')
#     >>> dodaj_enega(imenik, 'Y1', '2')
#     >>> dodaj_enega(imenik, 'X2', '3')
#     >>> imenik
#     {'X': [('X1', '1'), ('X2', '3')], 'Y': [('Y1', '2')]}
#

#
# 2. naloga
# Napišite funckijo `dodaj_vec`, ki kot prvi argument sprejme imenik,
# preostale argumente, ki so pari imen in številk, pa doda vanj.
# Spremenjeni imenik naj funkcija tudi vrne.
# 
#     >>> imenik = {}
#     >>> dodaj_vec(imenik, ('X1', '1'), ('X2', '3'), ('Y1', '2'))
#     {'X': [('X1', '1'), ('X2', '3')], 'Y': [('Y1', '2')]}
#

#
# 3. naloga
# Napiši funckijo `dodaj_vec_poimenovanih`, ki kot prvi argument sprejme imenik,
# preostale poimenovane argumente pa doda vanj, pri čemer ime predstavlja osebo,
# vrednost pa številko. Spremenjeni imenik naj tudi vrne.
# 
#     >>> imenik = {}
#     >>> dodaj_vec_poimenovanih({}, x1='1', x2='3', y1='2')
#     {'x': [('x1', '1'), ('x2', '3')], 'y': [('y1', '2')]}
#

#
# 4. naloga
# Napišite generator `nastej`, ki našteje vse pare v slovarju. Pari naj bodo
# abecedno urejeni po imenu, pri enakih imenih pa po telefonski številki.
# Na primer:
# 
#     >>> imenik = {}
#     >>> dodaj_enega(imenik, 'Metka', '051489654')
#     >>> dodaj_enega(imenik, 'Janez', '031548799')
#     >>> dodaj_enega(imenik, 'Janez', '025987522')
#     >>> dodaj_enega(imenik, 'Mojca', '014785645')
#     >>> dodaj_enega(imenik, 'Ana', '987651125')
#     >>> for ime, stevilka in nastej(imenik):
#     ...     print(ime, stevilka)
#     Ana 987651125
#     Janez 025987522
#     Janez 031548799
#     Metka 051489654
#     Mojca 014785645
#


## Vse se začne z ena
#
# 1. naloga
# Vedno se vse začne z `"1"`. Pa se vprašajmo, kaj vidimo v tem nizu. Eno
# enko seveda, torej `"11"`. Kaj pa vidimo v tem nizu? Dve enki, torej `"21"`.
# Kaj pa v tem zadnjem nizu? Eno dvojko in eno enko, torej `"1211"`. Pa zdaj?
# Eno eno, eno dvojko in dve enki, torej `"111221"`. Pa zdaj?
# 
# Temu zaporedju pravimo "poglej in povej zaporedje" z začetnim členom 1.
# 
# Sestavite (neskončen) generator `poglej_in_povej()`, ki bo generiral
# zgoraj opisano zaporedje. Generator naj vrača nize (in ne števila).
# 
#     >>> g = poglej_in_povej()
#     >>> [next(g) for i in range(5)]
#     ['1', '11', '21', '1211', '111221']
#

#
# 2. naloga
# Oglejmo si zaporedje
# 
#     1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 5 1 2 1 3 1 2 1 4 1 2 1 3 …
# 
# Kako smo ga dobili? Začnemo z 1. Sledi 2, potem pa še enkrat ponovimo vse,
# kar je bilo pred 2. Sledi 3, nato pa še enkrat ponovimo vse, kar smo imeli
# pred 3…
# 
# Sestavite (neskončen) generator `ravnilo()`, ki bo generiral člene zgoraj
# opisanega zaporedja.
# 
#     >>> g = ravnilo()
#     >>> [next(g) for x in range(20)]
#     [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3]
#


## Praštevila in racionalna števila
#
# 1. naloga
# Sestavite (neskončen) generator `prastevila(n)`, ki bo kot argument
# dobil naravno število `n` in vračal praštevila, začenši z najmanjšim
# praštevilom, ki je strogo večje od `n`.
# 
#     >>> g = prastevila(1)
#     >>> [next(g) for g in range(10)]
#     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#     >>> g = prastevila(2013)
#     >>> [next(g) for g in range(5)]
#     [2017, 2027, 2029, 2039, 2053]
#

#
# 2. naloga
# Sestavili bomo generator `pozitivna_racionalna()`, ki bo vračal
# pozitivna racionalna števila.
# 
# Mislimo si neskončno matriko, ki ima v $i$-ti vrstici in $j$-tem stolpcu
# ulomek $\frac{j}{i}$:
# 
# $\begin{pmatrix}
# \frac{1}{1} & \frac{2}{1} & \frac{3}{1} & \frac{4}{1} & \frac{5}{1} & \dots \\ 
# \frac{1}{2} & \frac{2}{2} & \frac{3}{2} & \frac{4}{2} & \frac{5}{2} & \dots \\ 
# \frac{1}{3} & \frac{2}{3} & \frac{3}{3} & \frac{4}{3} & \frac{5}{3} & \dots \\ 
# \frac{1}{4} & \frac{2}{4} & \frac{3}{4} & \frac{4}{4} & \frac{5}{4} & \dots \\
# \frac{1}{5} & \frac{2}{5} & \frac{3}{5} & \frac{4}{5} & \frac{5}{5} & \dots \\    
# \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\ 
# \end{pmatrix}$
# 
# V takšni neskončni matriki se nahajajo vsa pozitivna racionalna števila.
# Torej se moramo na nek _primeren način_ sprehoditi po elementih te matrike,
# pri čemer pa moramo biti pazljivi, saj se vsako racionalno število v takšni
# matriki pojavlja znova in znova. Na primer ulomki
# 
# $\frac{1}{3}, \frac{2}{6}, \frac{3}{9}, \frac{4}{12}, \ldots$
# 
# vsi predstavljajo isto racionalno število. Med vse temi ulomki pa je
# natanko en _okrajšan_ ulomek. Če se torej sprehodimo po vseh ulomkih v
# tej matriki in ignoriramo tiste, ki niso okrajšani, bomo vsako pozitivno
# racionalno število obiskali natanko enkrat.
# 
# Kako pa naj se na _primeren način_ sprehodimo po tej matriki? Če bi
# šli po prvi vrstici, bi obiskali samo naravna števila. Do ostalih ne
# bi nikoli prišli, saj je že naravnih števil neskončno. Če pa gremo po
# diagonalah, potem vsako število slej ko prej pride na vrsto. _Primeren_
# vrstni red je torej:
# 
# $\frac{1}{1}, \frac{2}{1}, \frac{1}{2}, \frac{3}{1}, \frac{2}{2}, \frac{1}{3},
# \frac{4}{1}, \frac{3}{2}, \frac{2}{3}, \frac{1}{4}, \ldots$
# 
# Sestavite generator `pozitivna_racionalna()`, ki bo vračal pare števcev in
# imenovalcev pozitivnih racionalnih števil. Vrstni red teh števil naj bo tak,
# kot je opisano zgoraj. Zgled:
# 
#     >>> g = pozitivna_racionalna()
#     >>> [next(g) for i in range(10)]
#     [(1, 1), (2, 1), (1, 2), (3, 1), (1, 3), (4, 1), (3, 2), (2, 3), (1, 4), (5, 1)]
#

#
# 3. naloga
# Zdaj pa sestavite še generator `racionalna_stevila()`, bo vračal
# racionalna števila.
# 
# Najprej naj vrne število 0, potem pa vsa racionalna števila v enakem
# vrstnem redu kot pri prejšnji podnalogi, pri čemer naj najprej vrne
# pozitivno število, potem pa še ustrezno negativno število. Zgled:
# 
#     >>> g = racionalna_stevila()
#     >>> [next(g) for i in range(10)]
#     [(0, 1), (1, 1), (-1, 1), (2, 1), (-2, 1),
#      (1, 2), (-1, 2), (3, 1), (-3, 1), (1, 3)]
#



