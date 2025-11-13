## Kalorije
#
# Tina si za vsak obrok, ki ga poje, zapiše njegovo kalorično vrednost
# (celo število). Vse te podatke hrani v datoteki. Za vsak dan ima v
# datoteki po eno vrstico. Znotraj iste vrstice so števila ločena z vejicami,
# kot prikazuje zgled:
# 
#     550,745,625,200
#     850,1250
#     40,650,743
#
# 1. naloga
# Sestavite funkcijo `vrni_kalorije(niz)`, ki dobi seznam kalorij, podan
# kot niz, v katerem so števila ločena z vejicami, in jih vrne kot seznam
# celih števil.
# 
#     >>> vrni_kalorije('10,4,7')
#     [10, 4, 7]
# 
# Pomagate si lahko z metodo `append`, ki danemu seznamu doda element:
# 
#     >>> l = [10]
#     >>> l.append(4)
#     >>> l
#     [10, 4]
#
def vrni_kalorije(niz):
    kalorije = []
    komponente = niz.split(",")
    for znak in komponente:
        kalorije.append(int(znak))
    return kalorije
#
# 2. naloga
# Sestavite funkcijo `kalorije_na_dan(ime_datoteke)`, ki kot parameter
# dobi ime vhodne datoteke. Vhodna datoteka je take oblike, kot je opisano
# zgoraj. Funkcija naj za vsak dan izračuna, koliko kalorij je Tina zaužila.
# Rezultat naj vrne v obliki seznama števil. Primer (denimo, da so podatki
# iz zgleda shranjeni v datoteki z imenom tina_kalorije.txt):
# 
#     >>> kalorije_na_dan('tina_kalorije.txt')
#     [2120, 2100, 1433]
# 
# Torej, za vsako vrstico v datoteki (ki predstavlja en dan) dodaj v seznam
# eno število, ki naj bo enako vsoti kalorij za tisti dan.
#
def kalorije_na_dan(ime_datoteke):
    na_dan = []
    with open(ime_datoteke) as file:
        for line in file:
            na_dan.append(sum(vrni_kalorije(line)))
        return na_dan
#
# 3. naloga
# Sestavite funkcijo `vsota_kalorij(ime_vhodne, ime_izhodne)`, ki kot
# argumenta dobi imeni dveh datotek. Vhodna datoteka vsebuje Tinine zapiske.
# Na izhodno datoteko naj za vsako vrstico v vhodni datoteki zapiše vsoto
# kaloričnih vrednosti zaužite hrane tistega dne. Vsako število v izhodni
# datoteki naj bo v svoji vrstici.
# 
# Po klicu funkcije `vsota_kalorij('tina_kalorije.txt', 'tina_vsote.txt')`
# pri enakih podatkih kot zgoraj, bo v datoteki tina_vsote.txt naslednja
# vsebina:
# 
#     2120
#     2100
#     1433
#
def vsota_kalorij(ime_vhodne, ime_izhodne):
    dnevne = kalorije_na_dan(ime_vhodne)
    with open(ime_izhodne, 'w') as izhodna:
        for data in dnevne:
            print(data, file=izhodna)
#
# 4. naloga
# Sestavite funkcijo `povprecje_kalorij(ime_vhodne, ime_izhodne)`, ki
# kot argumenta dobi imeni dveh datotek (vhodne in izhodne). Na izhodno
# datoteko naj za vsako vrstico na vhodni datoteki zapiše zaporedno številko
# vrstice (vrstice se začno šteti z ena) ter povprečno kalorično vrednost
# obrokov, ki jih je Tina zaužila tisti dan, na dve decimalni mesti.
# 
# V zadnjo (dodatno) vrstico pa naj funkcija zapiše povprečje dnevno
# zaužitih kalorij (prav tako na dve decimalni mesti).
# 
# Po klicu funkcije `povprecje_kalorij('tina_kalorije.txt', 'tina_povprecja.txt')`
# pri enakih podatkih kot zgoraj, bo v datoteki tina_povprecja.txt naslednja
# vsebina:
# 
#     1 530.00
#     2 1050.00
#     3 477.67
#     1884.33
#
def povprecje_na_dan(ime_datoteke):
    na_dan = []
    with open(ime_datoteke) as file:
        for line in file:
            povprecje = ((sum(vrni_kalorije(line)) / len(vrni_kalorije(line))))
            na_dan.append(('{0:.2f}'.format(povprecje)))
        return na_dan
    
def povprecje_kalorij(ime_vhodne, ime_izhodne):
    k = 1
    dnevne = kalorije_na_dan(ime_vhodne)
    dnevno = ('{0:.2f}'.format((sum(dnevne) / len(dnevne))))
    povprecja = povprecje_na_dan(ime_vhodne)
    with open(ime_izhodne, 'w') as izhodna:
        for item in povprecja:
            print(k,item, file=izhodna)
            k += 1
        print(dnevno, file=izhodna)
                
            


# '...poljuben string...{0:.2f}...{1:.2f}...{3:.2f}...'.format(i, j, k)



## Ukazna vrstica
#
# V tej nalogi se seznanimo z ukazno vrstico v okolju Windows. Najprej prenesite
# datoteko s to nalogo in jo shranite na disk.
#
# 1. naloga
# V operacijskem sistemu Windows lahko programe poganjamo z ukazno vrstico
# `Command Prompt`. Odpremo jo tako, da zaženemo program `CMD`. Storite to.
#
import os
os.system('start cmd')
#
# 2. naloga
# Ukazna vrstica deluje podobno kot brskalnik po datotečnem sistemu. Na začetku
# smo v domači mapi. V ukazno vrstico nato vpisujemo ukaze, na primer
# `assoc`, `DriverQuery`, `exit`, `Ipconfig`, `dir` ... S katerim ukazom 
# dobimo pregled nad vsebino mape, v kateri smo?
# Odgovor na koncu naloge zapišite v spremenljivko `ukaz`.
#
ukaz = 'dir'
#
# 3. naloga
# Z ukazno vrstico se premaknemo v mapo `ime_mape` z ukazom `cd ime_mape`. 
# S katerim ukazom se premaknemo en nivo višje? 
# Premaknite se v mapo, ki vsebuje datoteko z navodili te naloge.
# Odgovor na koncu naloge zapišite v spremenljivko `ukaz_2`.
#
ukaz_2 = 'cd ..'
#
# 4. naloga
# Z ukazno vrstico lahko poženemo tudi programe, napisane v Pythonu. To storimo
# z ukazom `python ime_programa.py`. Poženite to nalogo. V urejevalniku kot
# rešitev zapišite le `pass`.
#

pass


## Imena
#
# V neki datoteki, ki ima lahko več vrstic, so zapisana imena. Znotraj
# posamične vrstice so imena ločena z vejicami (brez presledkov). Primer
# take datoteke:
# 
#     Jaka,Peter,Miha,Peter,Anja
#     Franci,Roman,Renata,Jožefa
#     Pavle,Tadeja,Arif,Filip,Gašper
#
# 1. naloga
# Sestavite funkcijo `kolikokrat_se_pojavi(niz, ime)`, ki vrne število
# pojavitev imena `ime` v nizu imen `niz`.
# 
#     >>> kolikokrat_se_pojavi('Alojz,Samo,Peter,Alojz,Franci', 'Alojz')
#     2
# 
# Pomagate si lahko z metodo `count`, ki deluje na seznamih.
#
def kolikokrat_se_pojavi(niz, ime):
    seznam_imen = list(niz.strip().split(","))
    return seznam_imen.count(ime)
#
# 2. naloga
# Sestavite funkcijo `koliko(niz, datoteka)`, ki na izhodno datoteko z
# imenom `datoteka` za vsako ime zapiše, kolikokrat se pojavi v nizu `niz`.
# 
# Na primer, če je niz enak `'Jaka,Luka,Miha,Luka'`, naj funkcija v izhodno
# datoteko zapiše
# 
#     Jaka 1
#     Luka 2
#     Miha 1
# 
# Pozor: Imena naj bodo izpisana v takem vrstnem redu, kakor si sledijo
# njihove prve pojavitve v nizu `niz`.
#
def koliko(niz, datoteka):
    used = []
    seznam_znakov = niz.split(',')
    with open(datoteka, 'w') as file:
        for znak in seznam_znakov:
            if znak not in used:
                print(znak, kolikokrat_se_pojavi(niz, znak), file=file)
                used.append(znak)
            else:
                pass
            
#
# 3. naloga
# Sestavite funkcijo `koliko_iz_datoteke(vhodna, izhodna)`, ki naj naredi
# isto kot funkcija `koliko`, le da podatke prebere iz datoteke. Torej, na
# izhodno datoteko z imenom `izhodna` naj za vsako ime zapiše, kolikokrat
# se pojavi v datoteki z imenom `vhodna`.
# 
# Pozor: Vhodna datoteka ima lahko več vrstic. Imena izpišite v enakem
# vrstnem redu, kot si sledijo njihove prve pojavitve v datoteki `vhodna`.
#
def pojavitve(datoteka, ime):
    stevec = 0
    with open(datoteka) as dat:
        for vrstica in dat:
            stevec += kolikokrat_se_pojavi(vrstica, ime)
        return stevec

def imena(datoteka):
    neponovljena = []
    with open(datoteka) as dat:
        for line in dat:
            vrsta = line.strip()
            for sign in vrsta.split(","):
                if sign not in neponovljena:
                    neponovljena.append(sign)
        return neponovljena
    
def koliko_iz_datoteke(vhodna, izhodna):
    brez_ponovitev = imena(vhodna)
    with open(izhodna, 'w') as dat:
        for name in brez_ponovitev:
            stevec = pojavitve(vhodna, name)
            print(name, stevec, file=dat)

# Veliko krajsa in verjetno tudi ucinkovitejsa resitev:
# def koliko_iz_datoteke(vhodna, izhodna):
#     vrstice = [] # Seznam vseh vrstic v datoteki vhodna
#     with open(vhodna) as f:
#         for vrstica in f:
#             vrstice.append(vrstica.strip()) # Odstranimo '\n' s konca vrstice
#     imena = ','.join(vrstice) # Niz z vsemi imeni iz datoteke
#     koliko(imena, izhodna)

#
# 4. naloga
# Sestavite funkcijo `koliko_urejen(vhodna, izhodna)`, ki na izhodno
# datoteko z imenom `izhodna` za vsako ime zapiše, kolikokrat se pojavi v
# datoteki z imenom `vhodna`. Imena naj bodo urejena padajoče po frekvenci
# pojavitev. Imena, ki imajo enako frekvenco, naj bodo nadalje urejena
# leksikografsko (tj. po abecednem vrstnem redu).
# 
# Primer: Če je na datoteki imena_vhod.txt vsebina
# 
#     Luka,Jaka
#     Luka,Miha,Miha
#     Miha,Aleš,Aleš
# 
# naj bo po klicu funkcije `koliko_urejen('imena_vhod.txt', 'imena_izhod.txt')`
# na datoteki imena_izhod.txt naslednja vsebina:
# 
#     Miha 3
#     Aleš 2
#     Luka 2
#     Jaka 1
#
from operator import itemgetter

def koliko_seznam(datoteka):
    with open(datoteka) as dat:
        brez_ponovitev = imena(datoteka)
        seznam = []
        for name in brez_ponovitev:
            stevec = pojavitve(datoteka, name)
            seznam.append((name, stevec))
        return seznam

def koliko_urejen(vhodna, izhodna):
    with open(izhodna, 'w') as dat:
        seznam1 = sorted(koliko_seznam(vhodna), key=itemgetter(0))
        seznam2 = sorted(seznam1, key=itemgetter(1), reverse=True)
        for key, counter in seznam2:
            print(key, counter, file=dat)

#Thank you python documentation


## Pogoste besede
#
# V tej nalogi preštejmo najpogostejše besede v Cankarjevem romanu
# [Na klancu](https://sl.wikisource.org/wiki/Na_klancu).
# Vsebino romana najprej shranite v datoteko `na_klancu.txt`.
#
# 1. naloga
# Sestavite funkcijo `najpogostejse_besede(vhod, st_besed, izhod)`, 
# ki iz dane datoteke `vhod` določi tistih `st_besed` besed, ki se pojavijo
# najpogosteje. Te besede (skupaj z njhovim številom pojavitev) naj funkcija zapiše v datoteko `izhod`, urejene
# po padajočem vrstnem redu glede na število pojavitev.
# 
# Klic funkcije `najpogostejse_besede("na_klancu.txt", 2, "pogosti.txt")`
# bo v datoteko `pogosti.txt` tako zapisal naslednje:
# 
#     je 5692
#     in 3014
#
def najpogostejse_besede(vhodna, st_besed, izhodna):
    brez_ponovitev = []
    besede = []
    pari = []
    with open(vhodna) as vhod:
        with open(izhodna, 'w') as izhod:
            for vrsta in vhod:
                for beseda in vrsta.lower().strip().replace(',', '').replace('.','').split(''):
                    if beseda != '':
                        besede.append(beseda)
                        if beseda not in brez_ponovitev:
                            brez_ponovitev.append(beseda)
            for beseda in brez_ponovitev:
                pari.append((-besede.count(beseda), beseda))
            pari.sort()
            pari = pari[:st_besed]
            for number, beseda in pari:
                print(beseda, -number, file=izhod)
                    
                    

## Kolokviji
#
# V vsaki vrstici datoteke imamo shranjene rezultate kolokvija v obliki:
# 
#     Ime Priimek,N1,N2,N3,N4,N5
# 
# Cela števila od `N1` do `N5` predstavljajo število točk pri posamezni
# nalogi. Zgled:
# 
#     Janez Novak,1,3,3,0,2
#
# 1. naloga
# Sestavite funkcijo `nabor(niz)`, ki kot parameter dobi niz z vejico
# ločenih vrednosti v taki obliki, kot je opisano zgoraj. Funkcija naj
# vrne nabor s temi vrednostmi. Pri tem naj točke za posamezne naloge
# spremeni v števila (tj. naj jih ne vrača kot nize). Primer:
# 
#     >>> nabor('Janez Novak,1,3,3,0,2')
#     ('Janez Novak', 1, 3, 3, 0, 2)
#     >>> nabor('Janez Horvat,2,4,0')
#     ('Janez Horvat', 2, 4, 0)
# 
# Predpostavite lahko, da so vsi podatki razen prvega res števila. Ni pa
# nujno, da imenu sledi natanko 5 števil.
#

def nabor(niz):
    seznam = []
    razbiti_niz = niz.strip().split(',')
    ime = razbiti_niz[0]
    seznam.append(ime)
    for i in razbiti_niz[1:]:
        seznam.append(int(i))
    return tuple(seznam)

# Krajse:
# def nabor(niz):
#     s = niz.split(',')
#     for i in range(1, len(s)):
#         s[i] = int(s[i])
#     return tuple(s)

#
# 2. naloga
# Sestavite funkcijo `nalozi_csv(ime)`, ki kot parameter dobi ime datoteke,
# v kateri se nahajajo rezultati kolokvija. Vrstice v tej datoteki so take
# oblike, kot je opisano zgoraj. Funkcija naj vrne seznam naborov; za vsako
# vrstico po enega.
# 
# Primer: Če so v datoteki kolokviji.txt shranjeni naslednji podatki:
# 
#     Janez Novak,1,3,3,0,2
#     Peter Klepec,1,0,1,2,1,3
#     Drago Dragić,7
# 
# potem
# 
#     >>> nalozi_csv('kolokviji.txt')
#     [('Janez Novak', 1, 3, 3, 0, 2), ('Peter Klepec', 1, 0, 1, 2, 1, 3), ('Drago Dragić', 7)]
#

def nalozi_csv(ime):
    seznam = []
    with open(ime) as d:
        for vrstica in d:
            seznam.append(nabor(vrstica))
        return seznam

# def nalozi_csv(ime):
#     rezultat = []
#     with open(ime) as f:
#         for vrstica in f:
#             rezultat.append(nabor(vrstica.strip()))
#         return rezultat

#
# 3. naloga
# Sestavite funkcijo `vsote(vhodna, izhodna)`, ki kot parametra dobi
# imeni dveh datotek. Iz prve naj prebere vrstice s podatki (ki so v taki
# obliki, kot je opisano zgoraj), nato pa naj izračuna vsoto točk za
# vsakega študenta in v drugo datoteko shrani podatke v obliki:
# 
#     Ime Priimek,vsota
# 
# Za vsako vrstico v vhodni datoteki morate zapisati ustrezno vrstico v
# izhodno datoteko.
# 
# Primer: Če je v datoteki kolokviji.txt enaka vsebina kot pri prejšnji
# podnalogi, potem naj bo po klicu `vsote('kolokviji.txt', 'sestevki.txt')`
# v datoteki sestevki.txt naslednja vsebina:
# 
#     Janez Novak,9
#     Peter Klepec,8
#     Drago Dragić,7
#

def vsote(vhodna, izhodna):
    with open(vhodna) as vhod:
        with open(izhodna, 'w') as izhod:
            for vrstica in vhod:
                naborcek = nabor(vrstica)
                ime = naborcek[0]
                tocke = sum(naborcek[1:])
                print(ime+','+str(tocke), file=izhod)

# Alternativno:
# def vsote(vhodna, izhodna):
#     podatki = nalozi_csv(vhodna)
#     with open(izhodna, 'w') as f:
#         for student in podatki:
#             ime = student[0]
#             vsota_tock = sum(student[1:])
#             print(ime + ',' + str(vsota_tock), file=f)
# Se bolj alternativna rešitev (uporablja metodo format):
# def vsote_2(vhodna, izhodna):
#     podatki = nalozi_csv(vhodna)
#     with open(izhodna, 'w') as f:
#         for student in podatki:
#             print('{0},{1}'.format(student[0], sum(student[1:])), file=f)

#
# 4. naloga
# Sestavite funkcijo `rezultati(vhodna, izhodna)`, ki kot parametra dobi
# imeni dveh datotek. Iz prve naj prebere vrstice s podatki, v drugo pa
# naj zapiše originalne podatke, skupaj z vsotami (na koncu dodajte še en
# stolpec). Predpostavite, da je v vsaki vrstici enako število ocen po
# posameznih nalogah.
# 
# V zadnjo vrstico naj funkcija zapiše še povprečne ocene po posameznih
# stolpcih, zaokrožene in izpisane na dve decimalni mesti. Ime v tej vrstici
# naj bo `POVPRECEN STUDENT`.
# 
# V izhodni datoteki naj bodo vrstice urejene po priimkih (razen zadnje
# vrstice, v kateri so povprečja). Predpostavite, da ima vsak študent eno
# ime in en priimek, ki sta ločena s presledkom. Ne pozabite na povprečje
# vsot!
# 
# Primer: Če je na datoteki kolokviji.txt vsebina
# 
#     Janez Novak,1,3,3,2,0
#     Micka Kovačeva,0,3,2,2,3
#     Peter Klepec,1,0,1,2,1
# 
# naj bo po klicu funkcije `rezultati('kolokviji.txt', 'rezultati.txt')`
# na datoteki rezultati.txt naslednja vsebina:
# 
#     Peter Klepec,1,0,1,2,1,5
#     Micka Kovačeva,0,3,2,2,3,10
#     Janez Novak,1,3,3,2,0,9
#     POVPRECEN STUDENT,0.67,2.00,2.00,2.00,1.33,8.00
#

def seznam_nizov(seznam):
    nizi = []
    for element in seznam:
        nizi.append(str(element))
    return nizi

def rezultati(vhodna, izhodna):
    podatki = nalozi_csv(vhodna)
    seznam = []
    for student in podatki:
        ime, priimek = student[0].split(' ')
        tocke = student[1:]
        vsota = sum(tocke)
        seznam.append((priimek, ime, tocke, vsota))
        seznam.sort() # sortiramo po priimkih
        o = len(seznam) # stevilo oseb
        k = len(seznam[0][2]) # stevilo kolokvijev
        skupaj_vsota = 0
        vsote_tock = [0] * k
        for priimek, ime, tocke, vsota in seznam:
            skupaj_vsota += vsota
            for i in range(k):
                vsote_tock[i] += tocke[i]
        skupno_povprecje = '{0:.2f}'.format(skupaj_vsota / o) #dobimo nize stevil z 2 decimalkama
        povprecne_tocke = []
        for t in vsote_tock:
            povprecne_tocke.append('{0:.2f}'.format(t / o)) #poracuna povprecje za vsak kolokvij
        with open(izhodna, 'w') as izhod:
            for priimek, ime, tocke, vsota in seznam:
                niz_tock = ','.join(seznam_nizov(tocke))
                oseba = ime + ' ' + priimek
                print(oseba + ',' + niz_tock + ',' + str(vsota), file=izhod)
            print('POVPRECEN STUDENT,' + ','.join(povprecne_tocke) + ',' + skupno_povprecje, file=izhod) 





## HTML datoteke
#
# 1. naloga
# Sestavite funkcijo `html2txt(vhodna, izhodna)`, ki bo vsebino datoteke
# z imenom `vhodna` prepisala v datoteko z imenom `izhodna`, pri tem pa
# odstranila vse značke.
# 
# Značke se začnejo z znakom `'<'` in končajo z znakom `'>'`. Pozor: Začetek
# in konec značke nista nujno v isti vrstici.
# 
# Na primer, če je v datoteki vreme.html zapisano:
# 
#     <h1>Napoved vremena</h1>
#     <p>Jutri bo <i><b>lepo</b></i> vreme.
#     Več o vremenu preberite <a
#     href="http://www.arso.gov.si/">tukaj</a>.</p>
# 
# bo po klicu `html2txt('vreme.html', 'vreme.txt')` v datoteki vreme.txt
# zapisano:
# 
#     Napoved vremena
#     Jutri bo lepo vreme.
#     Več o vremenu preberite tukaj.
#

def html2txt(vhodna, izhodna):
    pisi = True 
    with open(vhodna) as vhod:
        with open(izhodna, 'w') as izhod:
            for vrstica in vhod:
                nova_vrstica = ''
                for znak in vrstica:
                    if znak in '<>':
                        pisi = not pisi
                    elif pisi:
                        nova_vrstica += znak 
                print(nova_vrstica, file=izhod, end='')

#
# 2. naloga
# Sestavite funkcijo `tabela(ime_vhodne, ime_izhodne)`, ki bo podatke
# iz vhodne datoteke zapisala v obliki HTML tabele v izhodno datoteko.
# 
# V vhodni datoteki so podatki shranjeni po vrsticah ter ločeni z vejicami.
# Na primer, če je v datoteki tabela.txt zapisano:
# 
#     ena,dva,tri
#     17,52,49.4,6
#     abc,xyz
# 
# bo po klicu `tabela('tabela.txt', 'tabela.html')` v datoteki tabela.html
# zapisana naslednja vsebina:
# 
#     <table>
#       <tr>
#         <td>ena</td>
#         <td>dva</td>
#         <td>tri</td>
#       </tr>
#       <tr>
#         <td>17</td>
#         <td>52</td>
#         <td>49.4</td>
#         <td>6</td>
#       </tr>
#       <tr>
#         <td>abc</td>
#         <td>xyz</td>
#       </tr>
#     </table>
# 
# Pozor: Pazi na zamik (število presledkov na začetku vrstic) v izhodni
# datoteki.
#

def tabela(ime_vhodne, ime_izhodne):
    with open(ime_vhodne) as vhod:
        with open(ime_izhodne, 'w') as izhod:
            print('<table>', file=izhod)
            for vrstica in vhod:
                znacka1 = 2 * ' ' + '<tr>'
                znacka2 = 2 * ' ' + '</tr>'
                elementi = vrstica.strip().split(',')
                print(znacka1, file=izhod)
                for niz in elementi:
                    element = 4 * ' ' + '<td>' + niz + '</td>'
                    print(element, file=izhod)
                print(znacka2, file=izhod)
            print('</table>', file=izhod)

#
# 3. naloga
# Sestavite funkcijo `seznami(ime_vhodne, ime_izhodne)`, ki bo podatke
# iz vhodne datoteke zapisala v izhodno datoteko v obliki neurejenega
# seznama. V vhodni datoteki se vrstice seznamov začnejo z zvezdico.
# 
# Na primer, če je v datoteki seznami.txt zapisano:
# 
#     V trgovini moram kupiti:
#     * jajca,
#     * kruh,
#     * moko.
#     Na poti nazaj moram:
#     * obiskati sosedo.
# 
# bo po klicu funkcije `seznami('seznami.txt', 'seznami.html')` v datoteki
# seznami.html naslednja vsebina:
# 
#     V trgovini moram kupiti:
#     <ul>
#       <li>jajca,</li>
#       <li>kruh,</li>
#       <li>moko.</li>
#     </ul>
#     Na poti nazaj moram:
#     <ul>
#       <li>obiskati sosedo.</li>
#     </ul>
#

def seznami(ime_vhodne, ime_izhodne):
    seznam = False # Stikalo, ki pove, če smo znotraj seznama.
    with open(ime_vhodne) as vhod:
        with open(ime_izhodne, 'w') as izhod:
            for vrstica in vhod:
                if vrstica[0] == '*':
                    if not seznam:
                        seznam = True
                        print('<ul>', file=izhod)
                    print('  <li>' + vrstica[1:].strip() + '</li>', file=izhod)
                else:
                    if seznam:
                        seznam = False
                        print('</ul>', file=izhod)
                    print(vrstica, file=izhod, end='')
            if seznam:
                print('</ul>', file=izhod)

#
# 4. naloga
# Sestavite funkcijo `gnezdeni_seznami(ime_vhodne, ime_izhodne)`, ki bo
# podatke iz vhodne datoteke zapisala v izhodno datoteko v obliki neurejenega
# gnezdenega seznama. V vhodni datoteki je vsak element seznama v svoji
# vrstici, zamik pred elementom pa določa, kako globoko je element gnezden.
# Zamik bo vedno večkratnik števila 2. 
# 
# Na primer, če je v datoteki seznami.txt zapisano:
# 
#     zivali
#       sesalci
#         slon
#       ptiči
#         sinička
#     rastline
#       sobne rastline
#         difenbahija
# 
# bo po klicu `gnezdeni_seznami('seznami.txt', 'seznami.html')` v datoteki
# seznami.html zapisano:
# 
#     <ul>
#       <li>živali
#         <ul>
#           <li>sesalci
#             <ul>
#               <li>slon
#             </ul>
#           <li>ptiči
#             <ul>
#               <li>sinička
#             </ul>
#         </ul>
#       <li>rastline
#         <ul>
#           <li>sobne rastline
#             <ul>
#               <li>difenbahija
#             </ul>
#         </ul>
#     </ul>
# 
# Značk `<li>` ne zapirajte.
#

#Uradna resitev, ker sem bil len

def gnezdeni_seznami(ime_vhodne, ime_izhodne):
    nivo = 0
    zamik = 2
    with open(ime_vhodne) as vhod:
        with open(ime_izhodne, 'w') as izhod:
            for vrstica in vhod:
                prvi = 0 # Prvi znak, ki ni presledek.
                while vrstica[prvi] == ' ':
                    prvi += 1
                n = prvi // zamik + 1
                vrstica = vrstica.strip()
                if n > nivo:
                    print(2*zamik*nivo*' ' + '<ul>', file=izhod)
                    nivo += 1
                while n < nivo:
                    nivo -= 1
                    print(2*zamik*nivo*' ' + '</ul>', file=izhod)
                print((2*zamik*nivo - zamik)*' ' + '<li>' + vrstica, file=izhod)
            while nivo > 0:
                nivo -= 1
                print(2*zamik*nivo*' ' + '</ul>', file=izhod)

# pa znal tud nisem :P

## Gibanje cen finančnih instrumentov
#
# V tej nalogi si bomo ogledali, kako s Pythonom z interneta periodično
# prenašati cene popularnih finančnih instrumentov in jih shranjevati. Pri tem
# bomo uporabili modul `ystockquote`, ki bo podatke pridobil s spletne
# strani [Yahoo Finance](http://finance.yahoo.com). 
# 
# Ker ta modul ni vgrajen v Python, ga moramo najprej namestiti; 
# to storimo tako, da v ukazno vrstico vpišemo:
# 
#     pip install --user ystockquote
# 
# Primeri uporabe:
# 
#     >>> import ystockquote
#     >>> ystockquote.get_today_open("CL=F")
#     '49.60'
#     >>> ystockquote.get_last_trade_price("EURGBP=X")
#     '0.8644'
#
# 1. naloga
# Sestavite funkcijo `pridobi_zadnjo_ceno(oznaka)`, ki vrne zadnjo ceno
# instrumenta `oznaka` kot realno število.
#

#
# 2. naloga
# Sestavite funkcijo `podatek_o_casu()`, ki vrne niz, ki predstavlja trenutni
# čas v naslednjem formatu:
# 
#     >>> podatek_o_casu()
#     '29.03.2017 16:23:22'
#       
# Pomagate si lahko z modulom `datetime`. Kaj naredi `datetime.datetime.now()`?
# Poglejte si še metodo `strftime`.
#

#
# 3. naloga
# Sestavite funkcijo `pridobljaj_cene(oznaka, perioda, izhod)`, ki vsakih
# `perioda` sekund pridobi zadnjo ceno instrumenta `oznaka` in jo shrani
# v datoteko `izhod`. Pri tem naj zabeleži še čas pridobitve cene.
# 
# Pomagate si lahko z modulom `time`. Kaj naredi funkcija `time.sleep(1)`?
# 
# Če pokličemo funkcijo `pridobljaj_cene("EURGBP=X", 3, "evro_funt.txt")`, se v izhodno
# datoteko pričnejo pisati naslednji podatki:
# 
#     29.03.2017 16:27:07 0.8651
#     29.03.2017 16:27:12 0.8651
#     29.03.2017 16:27:15 0.8651
#     29.03.2017 16:27:18 0.8652
#     29.03.2017 16:27:22 0.8652
#     29.03.2017 16:27:25 0.8653
#





