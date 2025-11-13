## Kuhamo in pečemo
#
# Sestavine, ki jih potrebujemo za nek recept, opišemo s slovarjem, v
# katerem so ključi sestavine, vrednosti pa količine, ki jih potrebujemo.
#
# 1. naloga
# Sestavite funkcijo `pomnozi(recept, faktor)`, ki sestavi in vrne nov
# recept. Ta naj vsebuje iste sestavine kot recept `recept`, le da so vse
# količine v njem pomnožene z danim faktorjem.
# 
#     >>> pomnozi({'jajca': 4, 'moka': 500}, 2)
#     {'jajca': 8, 'moka': 1000}
# =============================================================================
def pomnozi(recept, faktor):
    for ingredient in recept:
        recept[ingredient] = faktor * recept[ingredient]
    return recept

#
# 2. naloga
# Sestavite funkcijo `ali_imamo_sestavine(recept, shramba)`, ki preveri, ali
# imamo v shrambi dovolj sestavin za dani recept. Sestavine, ki jih imamo
# v shrambi, so predstavljene s slovarjem na enak način kot sestavine v
# receptu.
# 
#     >>> ali_imamo_sestavine({'jajca': 3, 'moka': 500}, {'moka': 1000, 'jajca': 6, 'sladkor': 1000})
#     True
#     >>> ali_imamo_sestavine({'jajca': 3, 'moka': 500}, {'moka': 1000, 'sladkor': 1000})
#     False
#
def ali_imamo_sestavine(recept, shramba):
    for ingredient in recept:
        needed = recept[ingredient]
        if ingredient not in shramba:
            return False
        else:
            for item in shramba:
                available = shramba[item]
                if item == ingredient:
                    if available < needed:
                        return False
    return True
# Rather:
# def ali_imamo_sestavine(recept, shramba):
#     for (sestavina, kolicina) in recept.items():
#         if shramba.get(sestavina, 0) < kolicina:
#             return False
#     return True
#
#
# 3. naloga
# Sestavite funkcijo `kaj_moramo_se_kupiti(recept, shramba)`, ki vrne slovar
# sestavin s pripadajočimi količinami, ki jih moramo še dokupiti, da bomo
# lahko skuhali jed po danem receptu.
# 
#     >>> kaj_moramo_se_kupiti({'jajca': 3, 'moka': 500}, {'moka': 1000, 'jajca': 6, 'sladkor': 1000})
#     {}
#     >>> kaj_moramo_se_kupiti({'jajca': 3, 'moka': 500}, {'moka': 1000, 'sladkor': 1000})
#     {'jajca': 3}
#     >>> kaj_moramo_se_kupiti({'jajca': 3, 'moka': 500}, {'moka': 100})
#     {'jajca': 3, 'moka': 400}
#
def kaj_moramo_se_kupiti(recept, shramba):
    shopping_list = {}
    if ali_imamo_sestavine(recept, shramba):
        return shopping_list
    else:
        for (sestavina, kolicina) in recept.items():
            if shramba.get(sestavina, 0) < kolicina:
                shopping_list[sestavina] = (kolicina - shramba.get(sestavina, 0))
        return shopping_list



## Šifriranje
#
# Substitucijska šifra je enostaven način šifriranja, pri katerem vsako
# črko iz dane abecede zamenjamo z neko drugo črko. Tako šifro predstavimo
# s slovarjem, ki ima za ključe vse črke iz abecede, pripadajoče vrednosti
# pa so črke, s katerimi jih zašifriramo.
# 
# Tako slovar `{'A': 'B', 'C': 'C', 'B': 'D', 'D': 'A'}` pomeni, da se
# `A` zašifrira v `B`, `B` v `D`, `D` v `A`, `C` pa se ne spremeni.
# 
# V vseh testnih primerih bomo uporabljali naslednjo substitucijsko šifro:
# 
#     nasa_sifra = {'Č': 'K', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
#                   'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
#                   'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
#                   'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
#                   'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'Ž': 'D'}
# 
# 1. naloga
# Sestavite funkcijo `sifriraj(sifra, beseda)`, ki vrne besedo, zašifrirano
# z dano šifro. Predpostavite lahko, da vse črke v besedi nastopajo v šifri.
# 
#     >>> sifriraj(nasa_sifra, 'MATEMATIK')
#     'UOČVUOČBI'
#
def sifriraj(sifra, beseda):
    result = ""
    for letter in beseda:
        result += sifra[letter]
    return result
#
# 2. naloga
# Sestavite funkcijo `ali_je_sifra(slovar)`, ki ugotovi, ali `slovar`
# predstavlja šifro, torej ali je bijekcija črk na neki abecedi.
# 
#     >>> ali_je_sifra({'A': 'B', 'B': 'A'})
#     True
#     >>> ali_je_sifra({'A': 'B', 'B': 'C'})
#     False
#
def ali_je_sifra(slovar):
    for (key, value) in slovar.items():
        if key not in slovar.values():
            return False
    return True
        
#
# 3. naloga
# Sestavite funkcijo `inverz(sifra)`, ki vrne inverz dane šifre, če ta
# obstaja. V nasprotnem primeru funkcija vrne `None`.
# 
#     >>> inverz({'A': 'B', 'B': 'C', 'C': 'A'})
#     {'A': 'C', 'B': 'A', 'C': 'B'}
#
def inverz(sifra):
    result = {}
    if ali_je_sifra(sifra):
        for (k, v) in sifra.items():
            result[v] = k
        return result
    else:
        return None
#
# 4. naloga
# Sestavite funkcijo `odsifriraj(sifra, beseda)`, ki sprejme šifro in
# zašifrirano besedilo, vrne pa odšifrirano besedilo. Če slovar ni bijekcija
# (in se torej besedilo ne da nujno odšifrirati), naj funkcija vrne `None`.
# 
#     >>> odsifriraj(nasa_sifra, 'MVCOI')
#     'BEDAK'
#
def odsifriraj(sifra, beseda):
    if ali_je_sifra(sifra):
        return sifriraj(inverz(sifra), beseda)


## Permutacije
#
# V slovarju imamo shranjeno permutacijo naravnih števil od $1$ do $n$.
# Permutacijo, ki slika $1$ v $3$, $3$ v $1$, število $2$ pa pusti pri miru,
# torej zapišemo s slovarjem `{1: 3, 2: 2, 3: 1}`.
# 
# 1. naloga
# Sestavite funkcijo `slika(permutacija, x)`, ki vrne sliko števila `x`
# s podano permutacijo.
# 
#     >>> slika({1: 3, 2: 4, 3: 2, 4: 1}, 1)
#     3
#
def slika(permutacija, x):
    return permutacija[x]
#
# 2. naloga
# Sestavite funkcijo `slike(permutacija, x, n)`, ki vrne zaporedje slik,
# ki ga dobimo, če začnemo s številom `x` in na njem `n`-krat uporabimo
# permutacijo `permutacija`.
# 
#     >>> slike({1: 3, 2: 4, 3: 2, 4: 1}, 1, 2)
#     [1, 3, 2]
#
def slike(permutacija, x, n):
    i = 0
    result = []
    while i <= n:
        if i == 0:
            result.append(x)
        else:
            x = slika(permutacija, x)
            result.append(x)
        i += 1
    return result
# rather:
# def slike_nerekurzivno(permutacija, x, n):
#     r = []
#     for i in range(n + 1):
#         r.append(x)
#         x = permutacija[x]
#     return r
#
#
# 3. naloga
# Sestavite funkcijo `cikel(permutacija, x)`, ki vrne celoten cikel, ki
# se začne s številom `x`.
# 
#     >>> cikel({1: 3, 2: 2, 3: 1}, 1)
#     [1, 3]
#     >>> cikel({1: 3, 2: 2, 3: 1}, 2)
#     [2]
#
# when will the first key pop up as a value? 
def cikel(permutacija, x):
    r = [x]
    while permutacija[x] not in r:
        r.append(permutacija[x])
        x = permutacija[x]
    return r
#
# 4. naloga
# Sestavite funkcijo `cikli(permutacija)`, ki vrne seznam disjunktnih
# ciklov dane permutacije. Vsak cikel naj se začne z najmanjšim številom
# v ciklu, cikli pa naj bodo urejeni po začetnem številu.
# 
#     >>> cikli({1: 3, 2: 2, 3: 1})
#     [[1, 3], [2]]
#
def cikli(permutacija):
    cycles = []
    used = set()
    keys = permutacija.keys()
    for x in keys:
        if used == set():
            cycles.append(cikel(permutacija, x))
            used = used.union(set(cikel(permutacija, x)))
        elif used.intersection(set(cikel(permutacija, x))) == set():
            cycles.append(cikel(permutacija, x))
            used = used.union(set(cikel(permutacija, x)))
    return cycles
# rather:
# def cikli(permutacija):
#     cikli = [] 
#     ugotovljena = set()
#     for i in range(1, len(permutacija) + 1): 
#         if i not in ugotovljena: 
#             c = cikel(permutacija, i) 
#             cikli.append(c)
#             ugotovljena.update(c) 
#     return cikli
#
#
# 5. naloga
# Sestavite funkcijo `je_permutacija(slovar)`, ki vrne `True`, če dani
# slovar predstavlja permutacijo, in `False` sicer.
# 
#     >>> je_permutacija({1: 2, 2: 1})
#     True
#     >>> je_permutacija({1: 3, 2: 4})
#     False
#
def je_permutacija(slovar):
    k = slovar.keys()
    v = slovar.values()
    return set(range(1, len(slovar) + 1)) == set(k) and set(k) == set(v)


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
def narcisoidi(zaljubljeni):
    r = set()
    for (k, v) in zaljubljeni.items():
        if {k}.intersection(v) != set():
            r.update({k})
    return r
#rather:
# def narcisoidi(zaljubljeni):
#     return {oseba for oseba in zaljubljeni if oseba in zaljubljeni[oseba]}
#
#
# 2. naloga
# Sestavite funkcijo `ljubljeni(zaljubljeni)`, ki sprejme slovar zaljubljenih
# in vrne _množico_ tistih, ki so ljubljeni.
#
def ljubljeni(zaljubljeni):
    return {oseba for x in zaljubljeni for oseba in zaljubljeni[x]}
#
# 3. naloga
# Sestavite funkcijo `pari(zaljubljeni)`, ki sprejme slovar zaljubljenih
# in vrne _množico_ vseh parov, ki so srečno ljubljeni. Vsak
# par naj se pojavi samo enkrat in sicer tako, da sta zaljubljenca
# našteta po abecedi. Na primer, če sta Ana in Bine zaljubljena,
# dodamo par `('Ana', 'Bine')`.
#
def pari(zaljubljeni):
    parcki = set()
    for oseba in ljubljeni(zaljubljeni):
        if zaljubljeni[oseba] == set():
            pass
        else:
            for ljubezen in zaljubljeni[oseba]:
                if oseba in zaljubljeni[ljubezen]:
                    parcki.add((min(oseba, ljubezen), max(oseba,ljubezen)))
    return parcki
# raje:
# def pari(zaljubljeni):
#  return {tuple(sorted((x, y))) for x in zaljubljeni
#          for y in zaljubljeni[x] if x in zaljubljeni[y]}
#
# 4. naloga
# Sestavite funkcijo `ustrezljivi(oseba, zaljubljeni)`, ki sprejme ime osebe
# ter slovar zaljubljenih, vrne pa _množico_ vseh ljudi, ki so do dane osebe
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


def ustrezljivi(oseba, zaljubljeni):
    def posredno_ljubijo(persona):
        posredno = zaljubljeni[persona]
        while True:
            razsirjeni = set()
            for clovek in posredno:
                razsirjeni.update(zaljubljeni[clovek])
            razsirjeni.update(posredno)
            if razsirjeni == posredno:
                return razsirjeni
            posredno = razsirjeni
        return
    
    ustrezljivi = set()
    for individual in zaljubljeni:
        if oseba in posredno_ljubijo(individual):
            ustrezljivi.add(individual)
    return ustrezljivi


## Memoizacija in dinamično programiranje
#
# Pri pristopu, imenovanem *dinamično programiranje*, do rešitve danega
# problema pridemo tako, da rešitev sestavimo iz rešitev nekoliko manjših
# različic problema. Slednje lahko dobimo na enak način, dokler ne rešujemo
# tako majhnega problema, da ga lahko rešujemo neposredno.
# 
# Uberemo lahko dva pristopa. Prvi je od spodaj gor – najprej rešujemo
# najmanjše probleme, dokler ne pridemo do tistega, ki nas zanima.
# Pri tem lahko vmesne rešitve shranjujemo v slovar, iz katerega beremo rešitve
# pri reševanju večjih problemov.
# 
# Drugi način je od zgoraj dol, torej rekurzivno. Vendar to pomeni, da bomo
# morda isti problem reševali večkrat. Zato si pomagamo z *memoizacijo* - vsak
# problem prvič rešimo, nato pa njegovo rešitev spravimo v slovar, od koder
# preberemo rešitev, ko jo naslednjič potrebujemo.
#
# 1. naloga
# Zanima nas problem *najlažje poti po matriki*.
# Dana je matrika `A` (kot seznam seznamov števil), iščemo pa pot od zgornjega
# levega polja (`A[0][0]`) do spodnjega desnega polja, tako da je vsota števil
# v obiskanih poljih čim manjša. V vsakem koraku se lahko premikamo le za eno
# polje v desno ali dol (tj., v vsakem koraku se bo ena od koordinat povečala
# za 1). V testnih primerih bomo uporabili naslednjo matriko:
# 
#     A = [[5, 7, 3, 6],
#          [2, 7, 3, 4],
#          [1, 3, 9, 2],
#          [6, 6, 4, 2]]
# 
# Definirajte funkcijo `najlazja_pot_do(A, i, j, resitve)`, ki naj vrne dolžino
# najlažje poti v matriki `A` od `A[0][0]` do `A[i][j]`. Predpostavite, da ima
# slovar `resitve` že ključa `(i - 1, j)` oziroma `(i, j - 1)` z vrednostima,
# ki predstavljata vsoti najlažjih poti od `A[0][0]` do `A[i - 1][j]` oziroma
# `A[i][j - 1]` (ali pa upoštevajte ustrezne robne pogoje). Funkcija naj ne
# uporablja rekurzije ali zank, prav tako naj ne spreminja slovarja `resitve`.
#

#
# 2. naloga
# Sestavite funkcijo `najlazja_pot_slovar(A)`, ki naj vrne vsoto polj
# v najlažji poti v matriki `A`. Pri tem naj si pomaga s funkcijo
# `najlazja_pot_do` in ustrezno polni slovar, ki ji ga poda kot argument.
#

#
# 3. naloga
# V Pythonu lahko definiramo *dekoratorje*. Dekorator je funkcija,
# ki kot argument sprejme funkcijo in vrne novo funkcijo. Slednjo lahko
# definiramo kar znotraj telesa dekoratorja. Dekorator uporabimo tako,
# da ga z `@` napišemo pred definicijo dekorirane funkcije:
# 
#     @dekorator
#     def funkcija(x, y=1):
#         ...
# 
# `funkcija` se tako nadomesti z vrednostjo `dekorator(funkcija)`.
# 
# Definirajte dekorator `memo(fun)`, ki opravlja memoizacijo za funkcije z dvema
# argumentom. Tako slovar kot vrnjena funkcija naj bosta definirana v telesu
# dekoratorja.
# 
# Na primer, če definiramo:
# 
#     sesteti_pari = []
#     
#     @memo
#     def dodaj_in_sestej(x, y):
#          sesteti_pari.append((x, y))
#          return x + y
# 
# Bi morali dobiti sledeče rezultate
# 
#     >>> dodaj_in_sestej(42, 23)
#     65
#     >>> dodaj_in_sestej(23, 42)
#     65
#     >>> dodaj_in_sestej(42, 23)
#     65
#     >>> sesteti_pari
#     [(42, 23), (23, 42)]
#

#
# 4. naloga
# Sestavite funkcijo `najlazja_pot_memo(A)`, ki naj vrne vsoto polj
# v najlažji poti v matriki `A`. Pri tem naj si pomaga z dekoratorjem `memo`
# in gnezdeno rekurzivno pomožno funkcijo, ki jo pokliče samo enkrat.
#






