## Ogrlice
#
# Takrat, ko je upokojenki Marti dolgčas, vzame svoji dve posodici z belimi
# in rdečimi kroglicami ter začne nizati ogrlice. Te ogrlice bomo predstavili
# z nizi, sestavljenimi iz znakov `B` in `R`.
# 
# Na primer: `'BBRBBRB'` in `'RRBBBBB'` sta dve izmed 21 možnih ogrlic,
# sestavljenih iz petih belih in dveh rdečih kroglic.
#
# 1. naloga
# Sestavite funkcijo `je_ogrlica(niz, b, r)`, ki preveri, ali `niz`
# predstavlja ogrlico iz `b` belih in `r` rdečih kroglic. Na primer:
# 
#     >>> je_ogrlica('BBRBBRB', 5, 2)
#     True
#     >>> je_ogrlica('RRBBBBB', 5, 2)
#     True
#     >>> je_ogrlica('BBRBBRB', 2, 5)
#     False
#     >>> je_ogrlica('BBRBBRBBB', 5, 2)
#     False
#     >>> je_ogrlica('BBRBBRBXY', 5, 2)
#     False
#

#
# 2. naloga
# Z $O(b, r)$ označimo število različnih ogrlic, sestavljenih iz natanko
# $b$ belih in $r$ rdečih kroglic. Če je eno od števil $b$ ali $r$ enako
# nič, potem je $O(b, r) = 1$. Na primer, $O(5, 0) = 1$, saj iz petih
# belih kroglic lahko sestavimo le ogrlico `'BBBBB'`.
# 
# V nasprotnem primeru pa velja $O(b, r) = O(b - 1, r) + O(b, r - 1)$,
# saj se vsaka izmed ogrlic iz $b$ belih in $r$ rdečih kroglic:
# 
# * bodisi začne z belo kroglico, preostalih $b - 1$ belih in $r$ rdečih
#   kroglic pa lahko sestavimo na $O(b - 1, r)$ načinov,
# * bodisi začne z rdečo kroglico, preostalih $b$ belih in $r - 1$ rdečih
#   kroglic pa lahko sestavimo na $O(b, r - 1)$ načinov.
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

#
# 3. naloga
# Sestavite generator `ogrlice(b, r)`, ki zaporedoma generira vse nize,
# ki predstavljajo ogrlice, sestavljene iz `b` belih in `r` rdečih kroglic.
# Generator naj nize vrača v abecednem vrstnem redu.
# 
#     >>> for ogrlica in ogrlice(2, 2):
#     ...     print(ogrlica)
#     BBRR
#     BRBR
#     BRRB
#     RBBR
#     RBRB
#     RRBB
#

## Razčlenitve
#
# Naraščajočemu zaporedju neničelnih naravnih števil
#   $m_1 \le m_2 \le \cdots \le m_k$,
# za katere velja
#   $m_1 + m_2 + \cdots + m_k = n$,
# pravimo _razčlenitev naravnega števila $n$ na $k$ členov_.
# Na primer, $1 + 3 + 7$ in $2 + 4 + 5$ sta dve razčlenitvi števila $11$
# na $3$ člene.
# 
# S $p_k(n)$ označimo število vseh razčlenitev števila $n$ na $k$ členov.
# Očitno velja $p_k(n) = 0$, če je $k > n$. Če dodatno predpostavimo še
# $p_0(0) = 1$ ter $p_0(n) = 0$ za vse $n > 0$, potem velja
#   $p_k(n) = p_{k - 1}(n - 1) + p_k(n - k)$,
# kar lahko pokažemo na sledeč način:
# 
# * če je prvi člen zaporedja enak $1$, potem preostanek zaporedja tvori
#   razčlenitev števila $n - 1$ na $k - 1$ členov;
# * če je prvi člen zaporedja večji od $1$, potem lahko vsakemu izmed $k$
#   členov odštejemo $1$ (saj je zaporedje naraščajoče) in s tem dobimo
#   razčlenitev števila $n - k$ na $k$ členov.
#
# 1. naloga
# Sestavite funkcijo `stevilo_razclenitev(n, k)`, ki vrne število vseh
# razčlenitev števila `n` na `k` členov. Primer:
# 
#     >>> stevilo_razclenitev(7, 3)
#     4
#     >>> stevilo_razclenitev(6, 2)
#     3
#

#
# 2. naloga
# Sestavite generator `razclenitve(n, k)`, ki zaporedoma vrača vse
# razčlenitve števila `n` na `k` členov, predstavljene s seznami števil.
# Generator naj razčlenitve vrača v leksikografskem vrstnem redu. Primer:
# 
#     >>> for razclenitev in razclenitve(7, 3):
#     ...     print(razclenitev)
#     [1, 1, 5]
#     [1, 2, 4]
#     [1, 3, 3]
#     [2, 2, 3]
# 
# _Opomba:_ Razčlenitev števila 0 na 0 členov predstavimo s praznim seznamom.
#

#
# 3. naloga
# Sestavite generator `vse_razclenitve(n)`, ki zaporedoma vrača vse razčlenitve
# števila `n` (ne glede na število členov). Generator naj razčlenitve vrača v
# leksikografskem vrstnem redu. Primer:
# 
#     >>> for razclenitev in vse_razclenitve(6):
#     ...     print(razclenitev)
#     [1, 1, 1, 1, 1, 1]
#     [1, 1, 1, 1, 2]
#     [1, 1, 1, 3]
#     [1, 1, 2, 2]
#     [1, 1, 4]
#     [1, 2, 3]
#     [1, 5]
#     [2, 2, 2]
#     [2, 4]
#     [3, 3]
#     [6]
#

## Geometrija
#
# Pri tej vaji bomo implementirali razrede `Vektor`, `Tocka` in `Premica`,
# ki predstavljajo vektor, točko in premico v evklidski ravnini. Nekaj
# metod je že implementiranih, nekaj pa jih boste implementirali sami.
#
# 1. naloga
# Kodo, objavljeno na strani http://pastebin.com/aFPm162n vnesite kot rešitev
# te podnaloge.
#

#
# 2. naloga
# V razredu `Vektor` sestavite metodo `__repr__(self)`. Zgled:
# 
#     >>> v = Vektor(3, 2)
#     >>> v
#     Vektor(3, 2)
# 
# Obstoječemu razredu lahko dodate novo metodo takole (razred
# `FooBar` že obstaja):
# 
#     class FooBar(FooBar):
# 
#         def nova_metoda(self, baz):
#             pass
# 
# _Opomba:_ Če v interaktivni konzoli pokličemo nek objekt, se izpiše niz,
# ki ga vrne klic metode `__repr__` na tem objektu. Priporočilo je, da je
# niz, ki ga vrne metoda `__repr__`, veljavna programska koda v Pythonu,
# ki ustvari identično kopijo objekta.
#

#
# 3. naloga
# V razredu `Vektor` sestavite metodo `__str__(self)`. Zgled:
# 
#     >>> v = Vektor(3, 2)
#     >>> print(v)
#     (3, 2)
# 
# _Opomba:_ Funkcija `print` na svojem argumentu pokliče metodo `__str__`
# in izpiše niz, ki ga ta metoda vrne. Metoda `__str__` običajno vrne
# razumljiv opis objekta, ki naj bi ga razumeli tudi ne-programerji.
#

#
# 4. naloga
# V razredu `Vektor` sestavite metodo `__abs__(self)`, ki naj vrne dolžino
# (normo) vektorja. Zgled:
# 
#     >>> v = Vektor(1, 3)
#     >>> abs(v)
#     3.1622776601683795
#

#
# 5. naloga
# V razredu `Vektor` sestavite metodo `__sub__(self, other)`, ki vrne
# razliko vektorjev. Zgled:
# 
#     >>> v = Vektor(-1, 3)
#     >>> u = Vektor(2, 1)
#     >>> u - v
#     Vektor(-3, 2)
#

#
# 6. naloga
# V razredu `Vektor` sestavite metodo `__truediv__(self, skalar)`, ki vrne
# produkt vektorja `self` s skalarjem `1 / skalar`. Zgled:
# 
#     >>> Vektor(-1, 3) / 2
#     Vektor(-0.5, 1.5)
#

#
# 7. naloga
# V razredu `Vektor` sestavite metodo `sta_pravokotna(self, other)`, ki
# vrne `True`, če sta vektorja `self` in `other` pravokotna, in `False`
# sicer. Zgled:
# 
#     >>> v = Vektor(-1, 3)
#     >>> u = Vektor(2, 1)
#     >>> v.sta_pravokotna(u)
#     False
#

#
# 8. naloga
# V razredu `Vektor` sestavite metodo `rotacija(self, alpha)`, ki vrne
# rotacijo vektorja `self` za kot `alpha` (v radianih). Zgled:
# 
#     >>> Vektor(1, 0).rotacija(math.pi/4)
#     Vektor(0.7071067811865476, 0.7071067811865475)
#

#
# 9. naloga
# V razredu `Premica` sestavite metodo `projekcija(self, tocka)`, ki vrne
# pravokotno projekcijo točke `tocka` na premico `self`. Zgled:
# 
#     >>> p = Premica(Tocka(1, 1), Vektor(0, 1))
#     >>> p.projekcija(Tocka(3, 0))
#     Tocka(3, 1)
#

#
# 10. naloga
# V razredu `Premica` sestavite metodo `presek(self, other)`, ki vrne
# točko, ki je presek dveh premic. Zgled:
# 
#     >>> p = Premica(Tocka(3, 4), Vektor(2, -1))
#     >>> q = Premica(Tocka(0, 1), Vektor(1, 2))
#     >>> p.presek(q)
#     Tocka(1.2, 0.4)
#

#
# 11. naloga
# V razredu `Tocka` sestavite metodo `zrcali_cez_premico(self, premica)`,
# ki vrne zrcalno sliko točke `self` čez premico `premica`. Zgled:
# 
#     >>> p = Premica(Tocka(1, 1), Vektor(0, 1))
#     >>> Tocka(3, 4).zrcali_cez_premico(p)
#     Tocka(3, -2)
#


## Permutacija
#
# Najbolj popularnih zapisov permutacije je po mnenju mnogih ciklični zapis
# (tj. permutacijo zapišemo kot produkt disjunktnih ciklov). Primer:
# 
#     (1 5 2) (3 6) (4)
# 
# Ciklov dolžine 1 (fiksnih točk) po navadi ne pišemo, torej zgornjo
# permutacijo običajno pišemo kar takole:
# 
#     (1 5 2) (3 6)
#
# 1. naloga
# Sestavite razred `Permutacija`, s katerim predstavimo permutacijo.
# Najprej sestavite konstruktor `__init__(self, cikli, stopnja=None)`, kjer
# je `cikli` seznam seznamov, ki predstavljajo cikle permutacije. Argument
# `stopnja` ima privzeto vrednost `None` – v tem primeru naj bo stopnja
# največje število, ki nastopa v katerem od ciklov. Razred naj ima atributa
# `stopnja` in `cikli`. Na prvem mestu v vsakem ciklu naj bo najmanjši
# element tega cikla (s cikličnim pomikom dobimo isti cikel). Tudi cikli
# naj bodo urejeni. Morebitne cikle dožine 1 naj konstruktor odstrani.
# 
#     >>> p = Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=7)
#     >>> p.stopnja
#     7
#     >>> p.cikli
#     [[1, 5, 2], [3, 7]]
#

#
# 2. naloga
# V razredu `Permutacija` definirajte metodo `inverz(self)`, ki sestavi
# in vrne inverz dane permutacije. Inverz permutacije dobimo tako, da
# v cikličnem zapisu obrnemo vse cikle (vsakega posebej).
# 
#     >>> p = Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=7)
#     >>> q = p.inverz()
#     >>> q.stopnja
#     7
#     >>> q.cikli
#     [[1, 2, 5], [3, 7]]
#

#
# 3. naloga
# V razredu `Permutacija` sestavite metodo `ciklicni_tip(self)`, ki vrne
# ciklični tip permutacije. To je nabor, ki ima toliko elementov, kot je
# dolžina najdaljšega cikla. Prvi element v tem naboru je število ciklov
# dolžine 1, drugi element je število ciklov dolžine 2, itn.
# 
#     >>> p = Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=7)
#     >>> p.ciklicni_tip()
#     (2, 1, 1)
#

#
# 4. naloga
# V razredu `Permutacija` sestavite metodo `red(self)`, ki izračuna in
# vrne red permutacije. Naj bo $\pi$ permutacija. Red permutacije $\pi$ je
# najmanjše pozitivno število $k$, pri katerem je $\pi^k$ identiteta.
# 
# Namig 1: Red permutacije je najmanjši skupni večkratnik dolžin vseh ciklov.
# 
# Namig 2: Za poljubni dve naravni števili `a` in `b` velja, da je
# `gcd(a, b) * lcm(a, b) == a * b`. (Funkcija `gcd` računa največji
# skupni delitelj, funkcija `lcm` pa najmanjši skupni večkratnik.)
# 
#     >>> p = Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=7)
#     >>> p.red()
#     6
#


## Mnogokotnik
#
# Mnogokotnik v ravnini lahko predstavimo s seznamom njegovih oglišč
# (pari števil). Na primer seznam
# 
#     [(0, 0), (1, 0), (1, 1), (0, 1)]
# 
# opisuje kvadrat, seznam
# 
#     [(2, 0), (2, 1), (0, 2), (-2, 1), (-2, 0), (0, 1)]
# 
# pa opisuje (nekonveksen) šestkotnik.
# =====================================================================@002135=
# 1. podnaloga
# Sestavite razred `Mnogokotnik`, s katerim predstavimo ravninski
# mnogokotnik. Najprej sestavite konstruktor `__init__(self, oglisca)`,
# kjer je `oglisca` seznam njegovih oglišč. Atribut razreda naj bo
# poimenovan `oglisca`.
# 
# Nekateri ljudje mnogokotnike zapisujejo tako, da na konec seznama oglišč
# ponovno postavijo prvo oglišče (s tem poudarijo, da je mnogokotnik
# sklenjen). Zgornji kvadrat bi torej zapisali takole:
# 
#     [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
# 
# V našem razredu `Mnogokotnik` naj se dolžina seznama `oglisca` ujema s
# številom oglišč mnogokotnika. Podvojeno oglišče na koncu seznama naj
# konstruktor po potrebi odstrani. Zgled:
# 
#     >>> p = Mnogokotnik([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
#     >>> p.oglisca
#     [(0, 0), (1, 0), (1, 1), (0, 1)]
# 
# Predpostavite lahko, da mnogokotniki ne bodo izrojeni (tj. če imata dve
# stranici neprazen presek, sta nujno sosednji, presek pa je natanko
# njuno skupno oglišče).
#

#
# 2. naloga
# V razredu `Mnogokotnik` definirajte metodo `obseg(self)`, ki izračuna in
# vrne njegov obseg. Zgled:
# 
#     >>> p = Mnogokotnik([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
#     >>> p.obseg()
#     4.0
#

#
# 3. naloga
# V razredu `Mnogokotnik` definirajte metodo `ploscina(self)`, ki izračuna
# in vrne njegovo ploščino.
# 
# Ploščina mnogokotnika (brez samopresečišč) z oglišči
# $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$ je $|D|/2$, kjer je
# $D = x_1 y_2 - x_2 y_1 + x_2 y_3 - x_3 y_2 + \ldots + x_{n-1} y_n - x_n y_{n-1} + x_n y_1 - x_1 y_n$.
# 
#     >>> p = Mnogokotnik([(0, 0), (1, 0), (1, 1), (0, 1)])
#     >>> p.ploscina()
#     1.0
#

#
# 4. naloga
# V razredu `Mnogokotnik` definirajte metodo `je_konveksen(self)`, ki
# vrne `True`, če je mnogokotnik konveksen in `False` sicer.
# 
# Predstavljajte si, da je ravnina, na kateri leži mnogokotnik, vložena v
# trirazsežni prostor tako, da je $z = 0$. Na bodo $P$, $Q$ in $R$ tri
# zaporedna oglišča mnogokotnika. Naj bo $u$ vektor od $P$ do $Q$ in
# naj bo $v$ vektor od $Q$ do $R$. Potem je $z$-komponenta vektorskega
# produkta vektorjev $u$ in $v$ pozitivna, če $PQR$ "zavije v levo", in
# negativna sicer. Mnogokotnik je konveksen, če vedno "zavijamo v isto
# smer", ko delamo obhod po robu mnogokotnika. Zgled:
# 
#     >>> p = Mnogokotnik([(0, 0), (1, 0), (1, 1), (0, 1)])
#     >>> p.je_konveksen()
#     True
#     >>> q = Mnogokotnik([(2, 0), (2, 1), (0, 2), (-2, 1), (-2, 0), (0, 1)])
#     >>> q.je_konveksen()
#     False
# 
# Predpostavite lahko, da nobeni dve zaporedni stranici ne oklepata
# iztegnjenega kota (180 °).
#

## Praštevila in racionalna števila
#
# 1. naloga
# Sestavite (neskončen) generator `prastevila(n)`, ki bo kot argument
# dobil naravno število `n` in vračal praštevila, začenši z najmanjšim
# praštevilom, ki je strogo večje od `n`.
# 
#     >>> g = prastevila(1)
#     >>> for p in g:
#     ...     if p > 30:
#     ...         break
#     ...     print(p)
#     ...
#     2
#     3
#     5
#     7
#     11
#     13
#     17
#     19
#     23
#     29
#     >>> [next(g) for i in range(10)] # next(g) vrne naslednji člen generatorja, to ponovimo 10-krat
#     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
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


