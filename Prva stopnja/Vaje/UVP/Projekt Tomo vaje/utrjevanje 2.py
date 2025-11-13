## Poudarjanje znakov
#
# 1. naloga
# Sestavite funkcijo `poudari(naslov)`, ki vrne poudarjen niz `naslov`,
# v katerem so vse črke velike in med seboj ločene s presledki. Presledke
# obravnavajte tako kot ostale znake (spremenijo se v trojni presledek).
# Pazite, da se niz ne konča s presledkom.
# 
#     >>> poudari("Zadnja novica")
#     "Z A D N J A   N O V I C A"
#

#
# 2. naloga
# Sestavite funkcijo `poudari_besede(naslov)`, ki vrne naslov, v katerem
# so vse besede, označene z znakoma `*`, zapisane z velikimi črkami.
# 
#     >>> poudari_besede("Zadnja *novica* danes!")
#     "Zadnja NOVICA danes!"
#


## Praštevila
#
# 1. naloga
# Sestavite funkcijo `je_prastevilo(n)`, ki vrne `True`, če `n` je
# praštevilo, in `False`, če ni.
#

#
# 2. naloga
# Sestavite funkcijo `prastevilo(n)`, ki vrne `n`-to praštevilo.
#

#
# 3. naloga
# Sestavite funkcijo `naslednje_prastevilo(n)`, ki vrne prvo praštevilo,
# strogo večje od števila `n`.
#

#
# 4. naloga
# Sestavite funkcijo `prvo_prastevilo_z_vsoto_stevk_vsaj(n)`, ki izračuna
# točno to, kar piše v njenem imenu.
#


## Vsote
#
# 1. naloga
# Sestavite funkcijo `vsota_kvadratov(n)`, ki izračuna in vrne vsoto
# $1^2 + 2^2 + 3^2 + \ldots + n^2$. Primer:
# 
#     >>> vsota_kvadratov(10)
#     385
#

#
# 2. naloga
# Sestavite funkcijo `vsota_produktov_sosednjih(n)`, ki izračuna in vrne vsoto
# $1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 + \ldots + n \cdot (n + 1)$. Primer:
# 
#     >>> vsota_produktov_sosednjih(10)
#     440
#

#
# 3. naloga
# Sestavite funkcijo `stevilo_clenov(m)`, ki izračuna, največ koliko členov
# vsote $1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 + \ldots + n \cdot (n + 1) + \ldots$
# lahko seštejemo, da bo dobljena vsota še vedno manjša ali enaka `m`.
# Primer:
# 
#     >>> stevilo_clenov(20)
#     3
#

#
# 4. naloga
# Sestavite funkcijo `najblizje(a, b, m)`, ki poišče takšno število `k`
# med `a` in `b`, pri katerem se z eno od delnih vsot
# $k \cdot (k+1) + (k+1) \cdot (k+2) + (k+2) \cdot (k+3) + \ldots$
# najbolj približamo številu `m`. Če je takšnih števil več, naj funkcija
# vrne najmanjšega. Primer:
# 
#     >>> najblizje(10, 20, 10000)
#     14
#



## Analiza besedila
#
# Pri tej nalogi bomo analizirali nize, ki predstavljajo pravilno slovensko
# oblikovane besede in stavke. Pri vseh podnalogah lahko predpostavite, da
# so vhodni nizi `s` dobro oblikovani, tj. ne vsebujejo dveh zaporednih
# presledkov oz. nepotrebnih presledkov ter prelomov vrstice na začetku ali
# na koncu.
#
# 1. naloga
# Sestavite funkcijo `stevilo_besed(s)`, ki v podanem nizu prešteje
# število besed, pri čemer lahko predpostavite, da presledki stojijo
# **natanko pred vsako** (razen prvo) besedo v nizu. Primer:
# 
#     >>> stevilo_besed('Višje, hitreje, močneje!')
#     3
#

#
# 2. naloga
# Sestavite funkcijo `samoglasniki(s)`, ki v podanem nizu `s` prešteje
# število samoglasnikov. Zgled:
# 
#     >>> samoglasniki('pomaranča')
#     4
#

#
# 3. naloga
# V Pythonu vrstice večvrstičnega niza ločujemo z znakom `'\n'`.
# Sestavite funkcijo `vrstice(s)`, ki sprejme večvrstični niz `s` in
# vrne seznam, ki vsebuje vse vrstice tega niza (v istem vrstnem redu).
# Zgled:
# 
#     >>> vrstice("Danes\n je lep\ndan.\n")
#     ['Danes', ' je lep', 'dan.', '']
# 
# _Opomba_: Python obravnava niz `'\n'` kot en sam znak.
#

#
# 4. naloga
# Haiku (japonsko 俳句) je japonska pesniška oblika iz treh verzov
# (vrstic), ki obsega sedemnajst zlogov. Prvi in tretji verz imata po pet
# zlogov, drugi sedem.
# 
# Na kulturnem natečaju TomoHaiku udeleženci oddajajo svoje izdelke na
# strežnik Tomo. Napišite kontrolno funkcijo `haiku(s)`, ki sprejme
# niz `s` ter vrne `True`, če niz ustreza pesniški obliki haiku, sicer
# pa vrne `False`.
# 
# Predpostavite lahko, da število samoglasnikov v neki besedi ustreza
# številu njenih zlogov ter da niz `s` ne vsebuje nepotrebnih začetnih oz.
# končnih praznih vrstic. Vrstice so ločene z znakom za prelom vrstice `'\n'`.
# Primer:
# 
#     >>> haiku('Skrit v svojem svetu,\ntemna otožnost neba,\ntvoj topli objem.')
#     True
#     >>> haiku('Riba,\nraca, rak,\nvinjak je grenak!')
#     False
#

#
# 5. naloga
# Sestavite funkcijo `podcrtaj(s)`, ki za parameter dobi niz `s`, v
# katerem so podnizi, ki bi morali biti izpisani podčrtano, označeni s
# podčrtajem na začetku in na koncu. Če je v nizu liho mnogo podčrtajev,
# si mislite, da je še eden na koncu. Funkcija naj vrne dvovrstični niz,
# kjer je v prvi vrstici originalni niz `s` toda brez podčrtajev, sledi
# znak za prelom vrstice, naslednjo vrstico pa sestavlja niz, sestavljen
# iz presledkov in minusov, pri čemer minusi ležijo pod tistimi deli
# besedila, ki morajo biti podčrtani. Primer:
# 
#     >>> podcrtaj("Jaz _sem_ pa cajzelc!")
#     'Jaz sem pa cajzelc!\n    ---            '
# 
# Predpostavite, da v nizu `s` ni nobenega znaka `'\n'`.
#

#
# 6. naloga
# Sestavite funkcijo `stevilo_znakov(s)`, ki v podanem nizu `s` prešteje
# število znakov, pri čemer se presledki ne upoštevajo. Zgled:
# 
#     >>> stevilo_znakov('B     u!')
#     3
#

#
# 7. naloga
# [Sonet](https://sl.wikipedia.org/wiki/Sonet) je priljubljena pesniška oblika.
# Sestavljen je iz štirih kitic,
# pri čemur med vsakima dvema kiticama avtor izpusti eno prazno vrstico.
# Prvi dve kitici sta štirivrstični — kvartini, drugi dve pa sta trivrstični
# — tercini.
# 
# V slovenskem sonetu je standardni verz italijanski (laški) ali jambski
# enajsterec. To pomeni, da v vsaki vrstici nastopa natanko enajst zlogov.
# 
# Na kulturnem natečaju TomoSonet udeleženci oddajajo svoje izdelke na
# strežnik Tomo. Napiši kontrolno funkcijo `sonet(s)`, ki sprejme niz
# `s`, ter vrne `True`, če niz ustreza slovenskemu sonetu, in `False` sicer.
# Zgled:
# 
#     >>> sonet('Bolj slab\nsonet.\n\nZa umret!')
#     False
# 
# _Namig_: V slovenskem jeziku število samoglasnikov v neki besedi ustreza
# številu njenih zlogov. (Obstaja nekaj izjem, ki pa jih bomo zanemarili.)
#



## Lepšanje in šifriranje
#
# [Klodovik /papiga/](http://skab612.com/AlanFord/af_likovi.html) in ne
# [Klodvik /frankofonski kralj/](https://sl.wikipedia.org/wiki/Seznam_frankovskih_kraljev)
# bi rad zašifriral svoja besedila, da jih nepoklicane osebe
# ne bodo mogle prebrati.
#
# 1. naloga
# To stori tako, da najprej v besedilu vse male črke spremeni v velike in
# odstrani vse znake, ki niso črke. (Klodovik vsa pomembna besedila piše v
# angleščini. Uporabljali bomo angleško abecedo.) Na primer iz besedila
# `'Attack at dawn!'` dobi besedilo `'ATTACKATDAWN'`. Nato ga zapiše cik-cak
# v treh vrsticah, kot prikazuje primer:
# 
#     A...C...D...
#     .T.A.K.T.A.N
#     ..T...A...W.
# 
# Sestavite funkcijo `cik_cak(s)`, ki vrne trojico nizov (torej `tuple`) in
# sicer prvo, drugo in tretjo vrstico v tem zapisu. Primer:
# 
#     >>> cik_cak('Attack at dawn!')
#     ('A...C...D...', '.T.A.K.T.A.N', '..T...A...W.')
#

#
# 2. naloga
# Zašifrirano besedilo dobi tako, da najprej prepiše vse znake iz prve
# vrstice, nato vse znake iz druge vrstice in na koncu še vse znake iz
# tretje vrstice. V zgornjem primeru bi tako dobil `'ACDTAKTANTAW'`.
# Sestavite funkcijo `cik_cak_sifra(s)`, ki dobi kot argument niz `s`
# in vrne zašifrirano besedilo. Primer:
# 
#     >>> cik_cak_sifra('Attack at dawn!')
#     'ACDTAKTANTAW'
#

#
# 3. naloga
# Klodovik se zelo razjezi, ko dobi elektronsko pošto v takšni obliki:
# 
#     Kar sva  si obljubljala    že leta,  si   želiva potrditi tudi   pred prijatelji in   celo
#     žlahto. Vabiva te na
#     
#          poročno slovesnost,        ki bo
#        10.   maja 2016 ob    15.    uri na gradu Otočec.   Prijetno   druženje bomo 
#     nadaljevali v    hotelu   Mons.   Tjaša in  Pavle
# 
# Nepopisno mu gre na živce, da je med besedami po več presledkov. Še
# bolj pa ga nervira, ker so nekatere vrstice precej daljše od drugih.
# Ker je Klodovik vaš dober prijatelj, mu boste pomagali in napisali
# funkcije, s katerimi bo lahko olepšal besedila.
# 
# 
# Najprej napišite funkcijo `razrez(s)`, ki kot argument dobi niz `s` in vrne
# seznam besed v tem nizu. Besede so med seboj ločene z enim ali večimi
# praznimi znaki: `' '` (presledek), `'\t'` (tabulator) in `'\n'` (skok
# v novo vrstico). Pri tej nalogi ločilo obravnavamo kot del besede.
# Primer:
# 
#     >>> razrez('   Kakšen\t pastir, \n\ntakšna  čreda. ')
#     ['Kakšen', 'pastir,', 'takšna', 'čreda.']
#

#
# 4. naloga
# Sedaj, ko že imate funkcijo `razrez(s)`, bo lažje napisati tisto funckijo, ki
# jo Klodovik zares potrebuje. To je 
# funkcija `olepsanoBesedilo(s, sir)`, ki kot argumenta dobi niz
# `s` in naravno število `sir`. Funkcija vrne olepšano besedilo, kar
# pomeni naslednje:
# 
# * Funkcija naj odstrani odvečne prazne znake.
# * Vsaka vrstica naj bo kar se le da dolga.
# * Nobena vrstica naj ne vsebuje več kot `sir` znakov (pri čemer znaka
#   `'\n'` na koncu vrstice ne štejemo).
# * Besede znotraj iste vrstice naj bodo ločene s po enim presledkom
#   (ne glede na to, s katerimi in koliko praznimi znaki so ločene v
#   originalnem besedilu).
# 
# Predpostavite, da dolžina nobene besede ni več kot `sir` in da je niz
# `s` neprazen. Primer:
# 
#     >>> s2 = olepsanoBesedilo('  Jasno in   svetlo \t\tna sveti \t\n\nvečer,  dobre\t\t letine je dost, če pa je\t  oblačno in   temno,        žita ne bo.', 20)
#     >>> print(s2)
#     Jasno in svetlo na
#     sveti večer, dobre
#     letine je dost, če
#     pa je oblačno in
#     temno, žita ne bo.
#


## Zmajeva krivulja
# 
# [Zmajevo krivuljo](http://en.wikipedia.org/wiki/Dragon_curve) rišemo
# podobno kot Kochovo, le da vsako daljico nadomestimo z dvema pravokotnima
# daljicama pod kotom $45$ stopinj:
# 
#     ______  => \  /
#                 \/
# 
# Torej, krivuljo reda $n$ narišemo tako, da se obrnemo za $45$ stopinj v desno,
# narišemo krivuljo reda $n - 1$, se obrnemo za $90$ stopinj v levo in narišemo
# še eno krivuljo reda $n - 1$, le da obrate naredimo v nasprotno smer.
# Razmislite, koliko morata biti dolgi krivulji reda $n - 1$.
#
# 1. naloga
# Napišite funkcijo `zmajeva_krivulja(n, d, prvi_obrat_v_desno=True)`, ki s
# pomočjo želvje grafike nariše zmajevo krivuljo danega reda z dano začetno
# dolžino krivulje reda nič in dano smerjo prvega obrata. Sami preverite, ali
# ukaz `zmajeva_krivulja(8, 200)` pravilno nariše zmajevo krivuljo reda $8$.
#



## Ljubezen nam je vsem v pogubo
#
# Socialno omrežje zaljubljenosti podamo s slovarjem, ki ime osebe
# preslika v množico vseh, v katere je oseba zaljubljena (ena oseba
# je lahko zaljubljena v več oseb). Na primer, slovar
# 
#     {
#         'Ana': {'Bine', 'Cene'},
#         'Bine': set(),
#         'Cene': {'Bine'},
#         'Davorka': {'Davorka'},
#         'Eva': {'Bine'}
#     }
# 
# nam pove, da je Ana zaljubljena v Bineta in Ceneta, Bine ni
# zaljubljen, Cene ljubi Bineta, Davorka samo sebe in Eva Bineta.
#
# 1. naloga
# Sestavite funkcijo `narcisoidi(zaljubljeni)`, ki sprejme slovar zaljubljenih
# in vrne _množico_ tistih, ki ljubijo same sebe.
#

#
# 2. naloga
# Sestavite funkcijo `ljubljeni(zaljubljeni)`, ki sprejme slovar zaljubljenih
# in vrne _množico_ tistih, ki so ljubljeni.
#

#
# 3. naloga
# Sestavite funkcijo `pari(zaljubljeni)`, ki sprejme slovar zaljubljenih
# in vrne _množico_ vseh parov, ki so srečno ljubljeni. Vsak
# par naj se pojavi samo enkrat in sicer tako, da je sta zaljubljenca
# našteta po abecedi. Na primer, če sta Ana in Bine zaljubljena,
# dodamo par `('Ana','Bine')`.
#

#
# 4. naloga
# Sestavite funkcijo `ustrezljivi(oseba, zaljubljeni)`, ki sprejme ime osebe ter
# slovar zaljubljenih, vrne pa _množico_ vseh ljudi, ki so do dane osebe
# še posebej ustrežljivi. Posebej ustrežljivi so seveda zato, ker so
# bodisi zaljubljeni v dano osebo, bodisi so zaljubljeni v osebo, ki je
# posebej ustrežljiva do nje, in tako naprej.
# 
# Na primer, če imamo slovar
# 
#     {
#         'Ana': {'Bine', 'Cene'},
#         'Bine': {'Ana'},
#         'Cene': {'Bine'},
#         'Davorka': {'Davorka'},
#         'Eva': {'Bine'}
#     }
# 
# so do Ceneta posebej ustrežljivi Ana (ki je zaljubljena vanj), Bine
# (ki je zaljubljen v Ano) ter Cene in Eva (ki sta zaljubljena v Bineta).
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



