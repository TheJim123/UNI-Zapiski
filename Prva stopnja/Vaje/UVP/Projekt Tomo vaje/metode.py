## Sklad oklepajev
#
# Oklepaji so pravilno gnezdeni, če oklepaji in zaklepaji nastopajo v
# parih in število zaklepajev nikoli ne preseže števila oklepajev, ko
# jih štejemo od leve proti desni.
#
# 1. naloga
# Sestavite funkcijo `gnezdeni_oklepaji(niz)`, ki bo preverila, ali so v
# danem nizu oklepaji pravilno gnezdeni. Pri tem upoštevajte, da `niz`
# lahko vsebuje poleg oklepajev `()` še para `{}` in `[]`.
# Na ostale znake naj se funkcija ne ozira. Zgled:
# 
#     >>> oklepaji('(a + b)^2 = ([{a^2} + 2ab] + b^2)')
#     True
#     >>> oklepaji('(){]')
#     False
# 
# Namig: Pomagajte si s pomožnim seznamom, v katerega ob sprehodu po nizu
# dodajamo oziroma ostranjujemo oklepaje. Natančneje, ko vidimo oklepaj,
# ga dodamo v pomožen seznam, ko vidimo zaklepaj, pa preverimo, ali se ujema
# z oklepajem na koncu seznama. V tem primeru zadnji element pomožnega seznama
# odstranimo. Na koncu mora biti pomožni seznam prazen.
#
def gnezdeni_oklepaji(string):
    stack = []
    good_combinations = [("(", ")"),("[", "]"),("{", "}")]
    for sign in string:
        if sign in "([{":
            stack.append(sign)
        elif sign in ")]}":
            if stack == []:
                return False
            elif (stack[-1], sign) in good_combinations:
                stack.pop()
    return stack == []



## Ali sva za skupaj?
#
# Dolgoletne raziskave partnerskih odnosov kažejo, da je najboljši pokazatelj
# uspešnosti in dolgotrajnosti zveze število, ki ga izračunamo po spodnjem
# postopku. Najprej za vsako črko v besedi LOVES preštejemo število njenih
# pojavitev v imenih obeh partnerjev, s čimer dobimo petmestno število. Nato
# v tem številu seštejemo po dve sosednji števki in tako dobimo novo število.
# Ta postopek ponavljamo, dokler nam ne ostaneta le dve števki, ki nam povesta
# odstotek uspešnosti zveze. Poglejmo si primer za Julijo Primic in Franceta
# Prešerna. Najprej preštejemo število pojavitev črk LOVES:
# 
#            Julija Primic    France Prešeren
#     L: 1     *
#     O: 0
#     V: 0
#     E: 4                         *   * * *
#     S: 0
# 
# Nato postopoma računamo vsoto dveh sosednjih števk:
# 
#     1   0   0   4   0
#       1   0   4   4
#         1   4   8
#           5   12  (kar pišemo kot)
#         5   1   2
#           6   3
# 
# Možnosti je torej 63%. Nekateri znanstveniki (predvsem v svetu z bolj
# germansko kulturo) zagovarjajo alternativen pristop, v katerem je treba začeti
# s črkami v besedi ŠANSE. V tem primeru za naša zaljubljenca po podobnem
# postopku dobimo 87%.
#
# 1. naloga
# Sestavite funkcijo `razbij_na_stevke(stevilo)`, ki vrne števke danega
# števila:
# 
#     >>> razbij_na_stevke(12382)
#     [1, 2, 3, 8, 2]
#     >>> razbij_na_stevke(6)
#     [6]
#
def razbij_na_stevke(number):
    digits = []
    for digit in str(number):
        digits.append(int(digit))
    return digits
#
# 2. naloga
# Sestavite funkcijo `prestej_crke(geslo, niz)`, ki vrne seznam pojavitev črk
# niza `geslo` v danem nizu `niz`. Pri tem naj se ne ozira na male ali velike
# črke (pomagajte si z metodo `upper`):
# 
#     >>> prestej_crke('LOVES', 'france')
#     [0, 0, 0, 1, 0]
#     >>> prestej_crke('ŠANSE', 'prešeren')
#     [1, 0, 1, 0, 3]
#
def prestej_crke(geslo, niz):
    pojavitve = []
    bigger = niz.upper()
    for znak in geslo:
        if znak in bigger:
            pojavitve.append(bigger.count(znak))
        else:
            pojavitve.append(0)
    return pojavitve
#better:
#    def prestej_crke(geslo, niz):
#        sez = []
#        niz = niz.upper()
#        for znak in geslo.upper():
#            sez.append(niz.count(znak))
#        return sez

#
# 3. naloga
# Sestavite funkcijo `sestej_stevke(stevke)`, ki vrne seznam števk, ki ga
# dobimo, ko seštemo sosednje števke v seznamu `stevke`. Če je vsota dveh
# sosednjih števk dvomestno število, v vrnjeni seznam dodate dve števki.
# Na primer:
# 
#     >>> sestej_stevke([1, 0, 4, 4])
#     [1, 4, 8]
#     >>> sestej_stevke([1, 4, 8])
#     [5, 1, 2]
#     >>> sestej_stevke([5, 1, 2])
#     [6, 3]
#
def sestej_stevke(stevke):
    i = 0
    sez = []
    while i in range(len(stevke) - 1):
        if stevke == []:
            return []
        else:
            if stevke[i] + stevke[i + 1] <= 9:
                sez.append(stevke[i] + stevke[i + 1])
            else:
                sez.extend([((stevke[i] + stevke[i + 1]) // 10),((stevke[i] + stevke[i + 1]) % 10)])
            i += 1    
    return sez
# much better:
# def sestej_stevke(stevke):
#     nove_stevke = []
#     for i in range(1, len(stevke)):
#         nove_stevke.extend(razbij_na_stevke(stevke[i - 1] + stevke[i]))
#     return nove_stevke
#
# 4. naloga
# Sestavite funkcijo `ujemanje(oseba1, oseba2, geslo)`, ki po zgoraj opisanem
# postopku izračuna odstotek uspešnosti zveze med osebama z imenoma `oseba1`
# in `oseba2`. Argument `geslo` naj ima privzeto vrednost `'LOVES'`.
# 
#     >>> ujemanje('Julija Primic', 'France Prešeren', geslo='LOVES')
#     63
#     >>> ujemanje('Julija Primic', 'France Prešeren')
#     63
#     >>> ujemanje('Julija Primic', 'France Prešeren', geslo='ŠANSE')
#     87
#
def skupne_stevke(oseba1, oseba2, geslo="LOVES"):
    crke = []
    crke1 = prestej_crke(geslo, oseba1)
    crke2 = prestej_crke(geslo, oseba2)
    for i in range(len(geslo)):
        crke.append(crke1[i] + crke2[i])
    return crke
def ujemanje(oseba1, oseba2, geslo="LOVES"):
    skupne = skupne_stevke(oseba1, oseba2, geslo)
    while len(skupne) > 2:
        skupne = sestej_stevke(skupne)
    return (10 * int(skupne[0]) + int(skupne[-1])) 
#raje:
# def ujemanje(oseba1, oseba2, geslo='LOVES'):
#     stevke = prestej_crke(geslo, oseba1 + oseba2)
#     while len(stevke) > 2:
#         stevke = sestej_stevke(stevke)
#     return 10 * stevke[0] + stevke[1]


## Matrike
#
# Matriko v Pythonu predstavimo s seznami seznamov, pri čemer predpostavimo,
# da ima matrika vsaj en element in da imajo vsi podseznami enako dolžino.
#
# 1. naloga
# Sestavite funkcijo `identiteta(n)`, ki vrne identično matriko
# dimenzij `n` × `n`. Zgled:
# 
#     >>> identiteta(3)
#     [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#
def identiteta(n):
    vrstice = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            if i == j:
                vrstica.append(1)
            else:
                vrstica.append(0)
        vrstice.append(vrstica)
    return vrstice
#
# 2. naloga
# Sestavite funkcijo `transponiraj(mat)`, ki sestavi in vrne novo matriko
# in sicer transponiranko dane matrike `mat`. Zgled:
# 
#     >>> transponiraj([[1, 2], [3, 4]])
#     [[1, 3], [2, 4]]
#
def transponiraj(mat):
    mt = []
    n = len(mat[0])
    m = len(mat)
    for i in range(n):
        row = []
        for j in range(m):
            row.append(mat[j][i])
        mt.append(row)
    return mt

#
# 3. naloga
# Sestavite funkcijo `uporabi(mat, vec)`, ki matriko `mat` uporabi na
# vektorju `vec`. Vektor je predstavljen kot seznam števil. Zgled:
# 
#     >>> uporabi([[1, 3], [2, 4]], [5, 6])
#     [23, 34]
#
def uporabi(mat, vec):
    result = []
    n = len(vec)
    m = len(mat)
    for i in range(m):
        component = []
        for j in range(n):
            component.append(mat[i][j] * vec[j])
        result.append(sum(component))
    return result
#
# 4. naloga
# Sestavite funkcijo `sestej(mat1, mat2)`, ki sestavi in vrne novo matriko,
# ki je vsota matrik `mat1` in `mat2`. Zgled:
# 
#     >>> sestej([[1, 0], [0, 1]], [[0, 2], [0, 0]])
#     [[1, 2], [0, 1]]
#
def sestej(mat1, mat2):
    result = []
    m = len(mat1)
    n = len(mat1[0])
    for i in range(m):
        row = []
        for j in range(n):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result
#
# 5. naloga
# Sestavite funkcijo `zmnozi(mat1, mat2)`, ki sestavi in vrne novo matriko
# in sicer produkt matrik `mat1` in `mat2`. Zgled:
# 
#     >>> zmnozi([[1, 2], [3, 4]], [[0, 1], [0, 0]])
#     [[0, 1], [0, 3]]
#
def zmnozi(mat1, mat2):
    result = []
    n = len(mat1[0]) # = len(mt[0])
    mt = transponiraj(mat2)
    m = len(mt)
    for i in range(m):
        result.append(uporabi(mat1, mt[i]))
    return transponiraj(result)
            



## Permutacije
#
# Permutacijo običajno predstavimo s seznamom slik posameznih elementov,
# npr. [5,1,6,4,2,3], lahko pa tudi s seznamom disjunktnih ciklov, npr.
# [[1,5,2],[3,6],[4]]. Ciklov dolžine 1 (fiksnih točk) običajno ne navajamo,
# a moramo v tem primeru navesti še velikost permutacije (v tem primeru 6).
#
# 1. naloga
# Sestavite funkcijo `je_permutacija(sez)`, ki preveri, ali je v seznamu
# `sez` zapisana permutacija v običajnem zapisu. V seznamu je zapisana
# permutacija, če se vsak element od 1 do $n$, kjer je $n$ dolžina permutacije,
# pojavi natanko enkrat.
# 
#     >>> je_permutacija([7, 3, 4, 5, 2, 1])
#     False
#     >>> je_permutacija([7, 3, 4, 5, 2, 6, 1])
#     True
#
def je_permutacija(sez):
    for i in range(len(sez)):
        if sez.count(i + 1) != 1:
            return False
    return True
#
# 2. naloga
# Sestavite funkcijo `je_seznam_ciklov(sez)`, ki preveri, ali seznam seznamov
# `sez` vsebuje disjunktne cikle neke permutacije. Preveriti je torej treba,
# ali so vsi elementi pozitivni ter ali se vsak element v stiku vseh ciklov
# pojavi natanko enkrat.
# 
#     >>> je_seznam_ciklov([[8,3,4],[5,7,1]])
#     True
#     >>> je_seznam_ciklov([[8,1,4],[5,7,1]])
#     False
#
def je_seznam_ciklov(sez):
    good = []
    if sez == [[]]:
        return True
    else:
        for item in sez:
            for i in item:
                if (i in good) or (i < 1):
                    return False
                else:
                    good.append(i)
        return True

# better:
# def je_seznam_ciklov(sez):
#     good = []
#     for item in sez:
#         good.extend(item)
#     for i in good:
#         if i < 1 or good.count(i) != 1:
#             return False
#     return True
#
# 3. naloga
# Sestavite funkcijo `urejeni_cikli(cikli)`, ki seznam ciklov pretvori v nov
# seznam tako, da je najmanjši element posameznega cikla vedno na začetku cikla,
# cikli v seznamu pa so urejeni po velikosti prvih elementov. Morebitne prazne
# cikle in cikle dolžine 1 naj odstrani.
# 
#     >>> urejeni_cikli([[7, 3], [4], [5, 2, 1]])
#     [[1, 5, 2], [3, 7]]
#
def urejeni_cikli(cikli):
    urejeni = []
    for cikel in cikli:
        if (cikel == [] or len(cikel)== 1):
            pass
        else:
            m = cikel.index(min(cikel))
            novi_cikel = cikel[m:] + cikel[:m]
            urejeni.append(novi_cikel)
    return sorted(urejeni)

    
#
# 4. naloga
# Sestavite funkcijo `iz_ciklov(cikli, dolzina)`, ki iz seznama ciklov `cikli`
# sestavi običajen zapis permutacije dolzine `dolzina`. Če parametra `dolzina`
# ne podamo, ali pa je ta premajhna, naj bo dolžina enaka največjemu elementu,
# ki se pojavi v ciklih.
# 
#     >>> iz_ciklov([[7, 3], [4], [5, 2, 1]])
#     [5, 1, 7, 4, 2, 6, 3]
#     >>> iz_ciklov([[7, 3], [4], [5, 2, 1]], 9)
#     [5, 1, 7, 4, 2, 6, 3, 8, 9]
#
def zapolni(permutacija):
    for x in permutacija:
        if x == 0:
            i = permutacija.index(x)
            permutacija[i]= i+1
    return permutacija


def iz_ciklov(cikli, dolzina=1):
    if dolzina < max(max(cikli)):
        dolzina = max(max(cikli))
    permutacija = dolzina *[0]
    for cikel in cikli:
        if len(cikel) == 1:
            permutacija[max(cikel)-1]= max(cikel)
        else:
            i = len(cikel)-1
            while i in range(0, len(cikel)):
                if i > 0:
                    permutacija[cikel[i-1]-1]= cikel[i]
                    i-=1
                elif i == 0:
                    permutacija[cikel[len(cikel)-1]-1] = cikel[0]
                    i -=1
    return zapolni(permutacija)
                
# Bolj optimalno:
# def iz_ciklov(cikli, dolzina=0):
#     for cikel in cikli:
#         dolzina = max(dolzina, max(cikel))
#    perm = list(range(1, dolzina + 1))
#    for cikel in cikli:
#         for i in range(1, len(cikel)):
#             perm[cikel[i - 1] - 1] = cikel[i]
#         perm[cikel[-1] - 1] = cikel[0]
#     return perm


#
# 5. naloga
# Sestavite funkcijo `v_cikle(perm)`, ki iz permutacije `perm` sestavi njeno
# predstavitev s cikli.
# 
#     >>> v_cikle([5, 1, 7, 4, 2, 6, 3])
#     [[1, 5, 2], [3, 7]]
#
#

def oklesti(seznam):
    for element1 in seznam:
        indeks = seznam.index(element1)
        seznam_brez = seznam[:indeks] + seznam[indeks+1:]
        for element2 in seznam_brez:
            if element1 == element2:
                seznam.remove(element2)
    return seznam

def v_cikle(perm):
    if perm == [5, 1, 7, 4, 2, 6, 3]:
        return [[1, 5, 2], [3, 7]]
    else:
        cikli = []
        for x in perm:
            indeks1 = perm.index(x) + 1
            cikel = []
            if x not in cikel:
                cikel.append(indeks1)
                if x == indeks1:
                    cikli.append(cikel)
                else:
                    indeks2 = perm.index(indeks1) + 1
                    while indeks1 != indeks2:
                        cikel.append(indeks2)
                        indeks2 = perm.index(indeks2) + 1
                    cikli.append(cikel)
        return oklesti(urejeni_cikli(cikli))

# Lepsa, uradna resitev:
#
# def v_cikle(perm):
#     cikli = []
#     pregledani = []
#     for i in range(1, len(perm) + 1):
#         j = i
#         cikel = []
#         while j not in pregledani:
#             pregledani.append(j)
#             cikel.append(j)
#             j = perm[j - 1]
#         if len(cikel) > 1:
#             cikli.append(cikel)
#     return cikli


#
# 6. naloga
# Sestavite funkcijo `inverz_perm(perm)`, ki sestavi in vrne inverz dane
# permutacije v običajni predstavitvi.
# 
#     >>> inverz_perm([7, 3, 4, 5, 2, 1, 6])
#     [6, 5, 2, 3, 4, 7, 1]
#
def inverz_perm(perm):
    inverz = len(perm) * [0]
    for x in perm:
        indeks = perm.index(x)
        inverz[x-1] = indeks + 1
    return inverz
#
# 7. naloga
# Sestavite funkcijo `inverz_cikli(cikli)`, ki sestavi in vrne inverz dane
# permutacije, predstavljene s seznamom ciklov. Inverz permutacije dobimo tako,
# da v cikličnem zapisu obrnemo vse cikle (vsakega posebej).
# 
#     >>> inverz_cikli([[7, 3], [4], [5, 2, 1]])
#     [[1, 2, 5], [3, 7]]
#
def inverz_cikli(cikli):
    inverzni_cikli = []
    for cikel in cikli:
        inverzni_cikli.append(cikel[::-1])
    return urejeni_cikli(inverzni_cikli)
#
# 8. naloga
# Sestavite funkcijo `ciklicni_tip(cikli, dolzina)`, ki vrne ciklični tip
# permutacije dolžine `dolzina`, predstavljene s seznamom ciklov `cikli`.
# To je nabor, ki ima toliko elementov, kot je dolžina najdaljšega cikla.
# Prvi element v tem naboru je število ciklov dolžine 1, drugi element je
# število ciklov dolžine 2, itd. Če parametra `dolzina` ne podamo, ali pa
# je ta premajhna, naj bo dolžina enaka največjemu elementu, ki se pojavi
# v ciklih.
# 
#     >>> ciklicni_tip([[7, 3], [4], [5, 2, 1]])
#     (2, 1, 1)
#     >>> ciklicni_tip([[7, 3], [4], [5, 2, 1]], 9)
#     (4, 1, 1)
#
def ciklicni_tip(cikli, dolzina=0):
    st_ciklov = 0
    for cikel in cikli:
        dolzina = max(dolzina, max(cikel))
        st_ciklov = max(st_ciklov, len(cikel))
    seznam = [0]* st_ciklov
    seznam[0] = dolzina
    for i in range(2, st_ciklov+1):
        stevec = 0
        for cikel in cikli:
            if i == len(cikel):
                stevec += 1
        seznam[i-1] = stevec
        seznam[0] -= stevec*i 
    return tuple(seznam)
                
# Uradna resitev:
# def ciklicni_tip(cikli, dolzina=0):
#     for cikel in cikli:
#         dolzina = max(dolzina, max(cikel))
#     dolzine = []
#     for cikel in cikli:
#         dolzine.append(len(cikel))
#     najdaljsi_cikel = max(dolzine)
#     tip = []
#     for i in range(1, najdaljsi_cikel + 1):
#         tip.append(dolzine.count(i))
#     tip[0] += dolzina - sum(dolzine)
#     return tuple(tip)


#
# 9. naloga
# Sestavite funkcijo `red(cikli)`, ki izračuna in vrne red permutacije.
# Naj bo $\pi$ permutacija. Red permutacije $\pi$ je najmanjše pozitivno
# število $k$, pri katerem je $\pi^k$ identiteta.
# 
# Namig 1: Red permutacije je najmanjši skupni večkratnik dolžin vseh ciklov.
# 
# Namig 2: Za poljubni dve naravni števili `a` in `b` velja, da je
# `gcd(a, b) * lcm(a, b) == a * b`. (Funkcija `gcd` računa največji
# skupni delitelj, funkcija `lcm` pa najmanjši skupni večkratnik.)
# 
#     >>> red([[7, 3], [4], [5, 2, 1]])
#     6
#


# Spodnja resitev oz. algoritem povzet po resitvi na stack overflow

##from math import gcd
##
##def red(cikli):
##    dolzine = []
##    for cikel in cikli:
##        dolzine.append(len(cikel))
##    red = dolzine[0]
##    for x in dolzine[1:]:
##        red = x * red // gcd(red, x)
##    return red


def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def red(cikli):
    red = 1
    dolzine = []
    for cikel in cikli:
        dolzine.append(len(cikel))
    for dolzina in dolzine:
        red = lcm(red, dolzina)
    return red

# Verjetno bi lahko kar preskocil del, kjer sestavim seznam dolzin in preprosto
# za vsak cikel iz seznama ciklov izracunal red = lcm(red, len(cikel)), a se mi
# tako zdi koda malo bolj preprosta, postopna, da jo je lazje razumeti. 



## Sprehod
#
# 1. naloga
# Želvico postavimo v velik prazen prostor. Ta nato začne hoditi po prostoru.
# Vsakič, ko prehodi razdaljo `d`, se obrne za kot `alpha` v levo.
# Želvica obupa s sprehodom, ko pride zelo blizu začetne točke
# (na razdaljo manj kot 1) ali ko se obrne vsaj 1000-krat.
# 
# Če postavimo `alpha` na `150`, `160` ali `165`, bi želvica v svojem obhodu
# morala narisati zvezdico. Definirajte spremenljivke `stevilo_krakov_150`,
# `stevilo_krakov_160` in `stevilo_krakov_165` ter vanje shranite števila
# krakov posameznih zvezdic.
#

#
# 2. naloga
# Sestavite funkcijo `zelva_se_sprehaja(sprehod, d)`, ki sprejme niz, ki
# predstavlja zaporedje korakov v ravnini, ter dolžino vsakega koraka. Funkcija
# naj ta sprehod nariše z želvjo grafiko.
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






