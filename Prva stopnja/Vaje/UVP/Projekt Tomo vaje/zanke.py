## Vsote potenc
#
# 1. naloga
# Sestavite funkcijo `vsota_prvih(n)`, ki vrne vsoto prvih `n` naravnih števil.
# 
def vsota_prvih(n):
    vsota = 0
    for i in range(n + 1):
        vsota = vsota + i
    return vsota
#
# 2. naloga
# Sestavite funkcijo `vsota_prvih_kvadratov(n)`, ki vrne vsoto kvadratov
# prvih `n` naravnih števil.
#
def vsota_prvih_kvadratov(n):
    vsota = 0
    for i in range(n+1):
        vsota += (i ** 2)
    return vsota
#
# 3. naloga
# Sestavite funkcijo `vsota_prvih_potenc(n, k)`, ki vrne vsoto `k`-tih potenc
# prvih `n` naravnih števil. Argument `k` naj bo neobvezen in naj ima privzeto
# vrednost `1`.
#
def vsota_prvih_potenc(n, k=1):
    vsota = 0
    for i in range(n + 1):
        vsota += (i ** k)
    return vsota


## Vsote števk
#
# 1. naloga
# Sestavite funkcijo `vsota_stevk(n)`, ki vrne vsoto števk števila `n`.
#def vsota_stevk(n):
#    vsota = 0
#    i = 0 
#    for i in range(len(str(n + 1))):
#        vsota += ((n // (10 ** i)) % 10)
#        i += 1
#    return vsota
#rather:
def vsota_stevk(n):
    vsota = 0
    while n > 0:
        vsota += n % 10
        n //= 10
    return vsota
#
# 2. naloga
# Sestavite funkcijo `vsota_vecjih_stevk(n, k)`, ki vrne vsoto tistih števk
# števila `n`, ki so večje ali enake `k`. Če parametra `k` ne podamo, naj
# funkcija vrne vsoto vseh števk števila `n`.
#
def vsota_vecjih_stevk(n, k=1):
    summa = 0
    while n > 0:
        if (n % 10) >= k:
            summa += (n % 10)
        n //= 10
    return summa

#
# 3. naloga
# Sestavite funkcijo `vsota_stevk_stevil_med(m, n)`, ki vrne vsoto števk
# vseh števil med vključno `m` in `n`.
#
def vsota_stevk_stevil_med(m, n):
    summa = 0
    i = m
    while i <= n:
       summa += vsota_stevk(i)
       i += 1
    return summa


## Collatzovo zaporedje
#
# Collatzovo zaporedje tvorimo na sledeč način. Začnemo z nekim naravnim
# številom $n$, ki ga nato delimo z $2$, če je sodo, ali pa pomnožimo s $3$ in
# prištejemo $1$, če je liho. Postopek ponavljamo, dokler ne pridemo do števila
# $1$ (v tem primeru stvar ni več zanimiva, saj se začno ponavljati števila
# $1, 4, 2, 1, 4, 2, 1, \ldots$). Primer zaporedja, ki se začne z $6$ je tako
# $6, 3, 10, 5, 16, 8, 4, 2, 1$. Collatzova domneva, ki trdi, da za poljubno
# naravno število njegovo Collatzovo zaporedje sčasoma doseže $1$, je še vedno
# nerešena.
#
# 1. naloga
# Sestavite funkcijo `naslednji_clen(n)`, ki izračuna člen, ki v Collatzovemu
# zaporedju sledi številu `n`.
#
def naslednji_clen(n):
    while n >= 1 :
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1
        
#
# 2. naloga
# Sestavite funkcijo `dolzina_zaporedja(n)`, ki izračuna dolžino Collatzovega
# zaporedja, ki se začne s številom `n`.
#
def dolzina_zaporedja(n):
    dolzina = 0
    while n != 1:
        n = naslednji_clen(n)
        dolzina += 1
    return dolzina + 1
#
# 3. naloga
# Sestavite funkcijo `najvecji_clen(n)`, ki izračuna največji člen v
# Collatzovem zaporedju, ki se začne s številom `n`.
#
def najvecji_clen(n):
    largest_so_far = 1
    while n != 1:
        if n > largest_so_far:
            largest_so_far = n
        n = naslednji_clen(n)
    return largest_so_far
#
# 4. naloga
# Sestavite funkcijo `najdaljse_zaporedje(m, n)`, ki vrne dolžino najdaljšega
# zaporedja med vsemi tistimi Collatzovimi zaporedji, ki se začnejo s števili
# med (vključno) `m` in `n`.
#
def najdaljse_zaporedje(m, n):
    biggest = 0
    for i in range(m, n+1):
        biggest = max(dolzina_zaporedja(i), biggest)
    return biggest



#def najdaljse_zaporedje(m, n):
#    biggest = 1
#    i = m
#    while i <= n:
#        if dolzina_zaporedja(i) > biggest:
#            biggest = dolzina_zaporedja(i)
#        i += 1
#    return biggest


## Sprehod
#
# 1. naloga
# Sestavite funkcijo `celostevilski(sprehod)`, ki sprejme niz, ki
# predstavlja sprehod po celih številih, in vrne število, v katerem se
# sprehod konča.
# 
# Sprehod po celih številih se začne v številu 0, predstavimo pa ga z
# nizem, sestavljenim iz znakov `+` in `-`. Na ostale znake v nizu se
# ne oziramo.
#
def celostevilski(walk):
    position = 0
    for sign in walk:
        if sign == "+":
            position += 1
        elif sign == "-":
            position -= 1
    return position
#
# 2. naloga
# Napišite število, v katerem se konča sprehod, podan z:
# 
#     ++++-+--++---+-+--+++-++-+++---+++--+-+---+-+++--++-+++-++-++-++----+-
#     ++++-+--++---+-+--+++-++-+++---+++--+-+---+-+++--++-+++-++-++-++----+-
#     +++-+++++++-+++--+--+++--+++---+--+--+++--+-+-+++--++--+++-----+----+-
#     +++-+++++++-+++--+--+++--+++---+--+--+++--+-+-+++--++--+++-----+----+-
#     +++--++++++--+--+-++++++++-+++++-+++-----+-+-+++-+-++-----+--+-+++--++
#     +++--++++++--+--+-++++++++-+++++-+++-----+-+-+++-+-++-----+--+-+++--++
#     +++--+--+-+-+-+--+-++-+---++++-+--++-+--++-+-++---++-------+++++++--+-
#     +++--+--+-+-+-+--+-++-+---++++-+--++-+--++-+-++---++-------+++++++--+-
#     ++-++-+-----++----+++++-+-+++++-++-+--+-++-++++-----++-+--++---++++++-
#     ++-++-+-----++----+++++-+-+++++-++-+--+-++-++++-----++-+--++---++++++-
#     ++-+-++----+-++--++++++-++--+-+++-+-+--+++-++--+---++++-+--++-+++--+-+
#     ++-+-++----+-++--++++++-++--+-+++-+-+--+++-++--+---++++-+--++-+++--+-+
#     ++-+---+--+-+++--+++--+++-+--+-++++++--++++---+--+-----++-++-+-++-+--+
#     ++-+---+--+-+++--+++--+++-+--+-++++++--++++---+--+-----++-++-+-++-+--+
#     ++--+-+--+--+-----+-+-++-++-+++-+++-+-++---++--++-+-++++++-+++-++-+++-
#     ++--+-+--+--+-----+-+-++-++-+++-+++-+-++---++--++-+-++++++-+++-++-+++-
#     ++------+--++---+-+-+-----++++-++---++-+--+-++------+-+--++++-+-++----
#     ++------+--++---+-+-+-----++++-++---++-+--+-++------+-+--++++-+-++----
#     +-++++++---++--------+++-----++----+----+-+++---+-+-+---+++-+---++-+-+
#     +-++++++---++--------+++-----++----+----+-+++---+-+-+---+++-+---++-+-+
#     +-+-+--+-+++++----++---++--++++-+++-++--+-+-+-+++--+-+-+--+++---+-+-+-
#     +-+-+--+-+++++----++---++--++++-+++-++--+-+-+-+++--+-+-+--+++---+-+-+-
#     +--------+-+--+--++--+--+++-+--++++-----+---+++++++++++++-++-+-+-+-+--
#     +--------+-+--+--++--+--+++-+--++++-----+---+++++++++++++-++-+-+-+-+--
#     -++-+++---+-+--+-+--++++----+-+--+-+-+++++-+++-+--+---+-+--+++-++-++++
#     -++-+++---+-+--+-+--++++----+-+--+-+-+++++-+++-+--+---+-+--+++-++-++++
#     -+--++--+++++-++-+--++-+---+--++---+----+++-+-++++-+---+++-+++---++-+-
#     -+--++--+++++-++-+--++-+---+--++---+----+++-+-++++-+---+++-+++---++-+-
#     -+---+------+++-+++----+----+++-+-+-+-+++------++-+-++----+---++++++++
#     -+---+------+++-+++----+----+++-+-+-+-+++------++-+-++----+---++++++++
#     --++-++--+-+++++-+--+---++-+--++---+-++-+----++-+--++++------+--+---+-
#     --++-++--+-+++++-+--+---++-+--++---+-++-+----++-+--++++------+--+---+-
#     --++--+----+--+---+-+++-+--++++-+--++-+-+-+-++-+---+-+-++++++---+-+--+
#     --++--+----+--+---+-+++-+--++++-+--++-+-+-+-++-+---+-+-++++++---+-+---
#     --+-++++-+-++----++++-+++-++--+-++-+++++-+-+-++--++++++++--+++--+++++-
#     --+-++++-+-++----++++-+++-++--+-++-+++++-+-+-++--++++++++--+++--+++++-
#     --+--+++-+-++-+--++---+--+-++-----+--+++--+++--------+-+++---++++-+-+-
#     --+--+++-+-++-+--++---+--+-++-----+--+++--+++--------+-+++---++++-+-+-
#     -----++--------++++-+++-+-++---+++---+++-++--++++--++-++-----++----+--
#     -----++--------++++-+++-+-++---+++---+++-++--++++--++-++-----++----+--
#     -----+------+++--++----+----+++--+++--+---+-+--+--+++-++--+--+--++--+-
#     -----+------+++--++----+----+++--+++--+---+-+--+--+++-++--+--+--++--+-
#     ------+--+-+--+-++-+++-+-++-+++++--+--+++++-+-++-+-++-++-+---++-++--+-
#     ------+--+-+--+-++-+++-+-++-+++++--+--+++++-+-++-+-++-++-+---++-++--+-
#
42
#
# 3. naloga
# Sestavite funkcijo `ravninski(sprehod)`, ki sprejme niz, ki
# predstavlja zaporedje korakov v ravnini, in vrne točko, v kateri se
# sprehod konča.
# 
# Sprehod po ravnini se začne v izhodišču, predstavimo pa ga z nizem,
# sestavljenim iz črk `S`, `J`, `V` ali `Z`, odvisno od smeri
# (sever, jug, vzhod, zahod). Na ostale znake v nizu se ne oziramo.
#
def ravninski(sprehod):
    i = 0
    j = 0
    for sign in sprehod:
        if sign == "S":
            j += 1
        elif sign == "J":
            j -= 1
        elif sign == "V":
            i += 1
        elif sign == "Z":
            i -= 1
    return (i, j)
#
# 4. naloga
# Sestavite funkcijo `hitri(tek)`, ki sprejme niz, ki predstavlja
# zaporedje korakov in skokov v ravnini, in vrne točko, v kateri se
# tek konča.
# 
# Tek po ravnini se začne v izhodišču, predstavimo pa ga, tako kot
# sprehod, z nizem, sestavljenim iz črk `S`, `J`, `V` ali `Z`, odvisno
# od smeri (sever, jug, vzhod, zahod).
# 
# Poleg tega lahko tek vsebuje tudi števke od `1` do `9`, ki povedo,
# koliko dolg naj bo naslednji korak. Tako niz `5S` pomeni skok
# na sever, dolg 5 korakov. Privzamete lahko, da zaporednih števk v
# nizu ni, ter da se na ostale znake v nizu ne oziramo.
#
def hitri(tek):
    k = 1
    i = j = 0
    cifre = str(123456789)
    for sign in tek:
        if sign == "S":
            j += k
        elif sign == "J":
            j -= k
        elif sign == "V":
            i += k
        elif sign == "Z":
            i -= k
        if sign in cifre:
            k = int(sign)
        elif sign in "SJVZ":
            k = 1
    return (i, j)        


## Kvadratni koren
#
# Približke za kvadratni koren števila $n$ lahko izračunamo po
# naslednjem postopku. Začetni približek $x_0$ je enak $n / 2$.
# Vsak naslednji približek $x_{k + 1}$ pa izračunamo kot
# $(x_k + n / x_k) / 2$.
#
# 1. naloga
# Sestavite funkcijo `priblizek_po_korakih(n, k)`, ki po zgornjem postopku
# izračuna `k`. približek korena števila `n`.
#
def priblizek_po_korakih(n, k):
    priblizek = (n / 2)
    i = 1
#    x_(i + 1) = (x_i + (n / x_i)) / 2
    while i <= k:
        priblizek = (priblizek + (n / priblizek)) / 2
        i += 1
    return priblizek

#rather:
#def priblizek_po_korakih(n, k):
#    priblizek = n / 2
#    for i in range(k):
#        priblizek = (priblizek + (n / priblizek)) / 2
#    return priblizek
#
# 2. naloga
# Sestavite funkcijo `priblizek_do_natancnosti(n, eps)`, ki po zgornjem postopku
# izračuna prvi približek korena števila `n`, za katerega se kvadrat približka
# od `n` razlikuje za manj kot `eps`. Smislena vrednost za argument `eps` je
# npr. $10^{-6}$.
# 
def priblizek_do_natancnosti(n, eps=1e-6):
    priblizek = (n / 2)
    while abs(n - (priblizek ** 2)) >= eps:
        priblizek = (priblizek + (n / priblizek)) / 2
    return priblizek


## Gnezdenje oklepajev
#
# Oklepaji so pravilno gnezdeni, če uklepaji in zaklepaji nastopajo v
# parih in število zaklepajev nikoli ne preseže števila uklepajev, ko
# jih štejemo od leve proti desni.
# 
# 1. naloga
# Sestavite funkcijo `oklepaji(niz)`, ki bo preverila, ali so v danem
# nizu oklepaji pravilno gnezdeni. Na ostale znake naj se funkcija ne
# ozira. Zgled:
# 
#     >>> oklepaji('(a + b)^2 = (((a^2) + 2ab) + b^2)')
#     True
#     >>> oklepaji('())(()')
#     False
#

def oklepaji(niz):
    odprti_oklepaj = 0
    for znak in niz:
        if znak == "(":
            odprti_oklepaj += 1
        elif znak == ")":
            odprti_oklepaj -= 1
        if odprti_oklepaj < 0:
            return False
    return odprti_oklepaj == 0



## Zlati rez
#
# Pravimo, da sta števili $a$ in $b$ v razmerju _zlatega reza_, kadar je
# $a : b$ enako $(a + b) : a$, kar je takrat, ko je $\frac{a}{b}$ enako
# številu $\phi = \frac{1 + \sqrt{5}}{2}$.
# 
# Približek števila $\phi$ lahko izračunamo z zaporedjem
#   $\phi_0, \phi_1, \phi_2, \dots$,
# kjer je $\phi_0 = 1$, naslednji približek $\phi_{n + 1}$ pa izračunamo
# kot
#   $\phi_{n + 1} = 1 + 1 / \phi_n$.
#
# 1. naloga
# Sestavite funkcijo `naslednji_priblizek(x)`, ki iz približka `x` po
# zgornjem postopku izračuna naslednji približek števila $\phi$.
#
def naslednji_priblizek(x):
    return 1 + (1 / x)
#
# 2. naloga
# Sestavite funkcijo `priblizek(k)`, ki izračuna `k`. približek števila
# $\phi$. Za začetni približek (ko je `k` enak $0$) vzamite število $1$.
#
def priblizek(k):
    fi = 1
    for i in range(k):
        fi = (1 + (1 / fi))
    return fi
#
# 3. naloga
# Sestavite funkcijo `natancni_priblizek(eps)`, ki izračuna prvi približek
# števila $\phi$, ki se od prejšnjega približka razlikuje za manj kot
# pozitivno realno število `eps`.
#
def natancni_priblizek(eps):
    x = 1
    while abs(naslednji_priblizek(x) - x) >= eps:
        x = naslednji_priblizek(x)
    return naslednji_priblizek(x)
        


## Disemvoweling
#
# Matej je moderator na nekem manj znanem forumu, ki ima kar lepo število
# registriranih uporabnikov, vendar večina med njimi piše same neumnosti.
# Med takimi je še posebno dejaven Tomaž Majer. Če se zdi Mateju objava
# žaljiva, jo nemudoma zbriše. Če objava na forumu ni žaljiva, ampak je le
# precej neumna, pa naredi naslednje: Vse samoglasnike odstrani iz besedila
# in jih (v enakem vrstnem redu) doda nazaj na konec. Na primer sporočilo:
# 
#     Banana je najboljša! Izjemno dobra je tudi v kombinaciji z Nutelo!
# 
# postane
# 
#     Bnn j njbljš! zjmn dbr j td v kmbncj z Ntl!aaaeaoaIeooaeuioiaiiueo
# 
# Takó besedilo postane težko berljivo in večina bralcev ga ignorira. Če
# pa se najde kdo, ki ga vsebina resnično zanima, lahko z nekaj truda
# razvozla vsebino sporočila.
# 
# (Opisana transformacija besedila je znana pod imenom disemvoweling.)
#
# 1. naloga
# Napišite funkcijo `prvi_samoglasnik(niz)`, ki kot argument dobi niz `niz`
# in vrne položaj (indeks) prvega samoglasnika v danem nizu. Če v nizu ni
# samoglasnika, vrni -1
# 
#     >>> prvi_samoglasnik('Krščen matiček!')
#     4
#
def prvi_samoglasnik(niz):
    samoglasniki = "aeiouAEIOU"
    k = 0
    for znak in niz:
        if znak in samoglasniki:
            return k
        k += 1
    return -1
#
# 2. naloga
# Napišite funkcijo `disemvowel(sporocilo)`, ki kot argument prejme niz
# `sporocilo`. Funkcija naj sestavi in vrne nov niz, ki ga dobi iz niza
# `sporocilo` tako, da vse samoglasnike prestavi na konec niza.
# 
#     >>> disemvowel('Banana je dobra!')
#     'Bnn j dbr!aaaeoa'
#
def vsebuje_samoglasnik(niz):
    samoglasniki = "aeiouAEIOU"
    for x in niz:
        if x in samoglasniki:
            return True
    return False

def disemvowel(niz):
    niz_samoglasnikov = ""
    samoglasniki = "aeiouAEIOU"
    indeks = prvi_samoglasnik(niz)
    for znak in niz:
        while vsebuje_samoglasnik(niz):
            niz_samoglasnikov += niz[prvi_samoglasnik(niz)]
            niz = niz[:prvi_samoglasnik(niz)] + niz[prvi_samoglasnik(niz)+1:]
    return niz + niz_samoglasnikov

#alternativa:
#    def disemvowel(sporocilo):
#        '''desemvowlanje sporočila'''
#        brez = '' # niz brez samoglasnika
#        samoglasniki = '' # vsi samoglasniki iz niza
#        for c in sporocilo:
#            if c in 'aeiouAEIOU':
#                samoglasniki += c
#            else:
#                brez += c
#        return brez + samoglasniki #zlepimo v pravem redu
#        
#
# 3. naloga
# Včasih pa želimo sporočilo dešifrirati, saj nas zanima njegova vsebina.
# Ta naloga je vse prej kot enostavna, saj ne vemo kam točno je treba vriniti
# izgnane samoglasnike. Sporočilo `'Bnn j dbr!aaaeoa'` bi lahko dešifrirali
# tudi kot `'Banna ja debora!'`, kot `'Bnana aje dobar!'` ipd.
# 
# Matej je na mesta v besedilu, kjer predvideva, da bi morali stati
# samoglasniki, vstavil znake `'*'` (zvezdica). V sporočilu zvezdica nikoli
# ne bo imela drugega pomena. Prav tako bo število samoglasnikov enako številu
# zvezdic in vsi samoglasniki bodo na koncu niza.
# 
# Napišite funkcijo `razveljavi_disemvowel(niz)`, ki bo zvezdice v nizu
# nadomestila s samoglasniki, ki se v nizu `niz` nahajajo na koncu. Zgled:
# 
#     >>> razveljavi_disemvowel('B*n*n* j* d*br*!aaaeoa')
#     'Banana je dobra!'
#
def razveljavi_disemvowel(niz):
    '''zvezdice v disemvowlanem nizu nadosmesti s samoglasniki s konca niza'''
    st_zvezd = niz.count('*') #da bomo vedeli, kje se začno samoglasniki
    if st_zvezd == 0: # ni kaj delati
        return niz
    samoglasniki = niz[-st_zvezd:] # odrežemo ustrezen del niza
    counter = 0
    message = ''
    for znak in niz[:-st_zvezd]:
        if znak == '*':
            message += samoglasniki[counter]
            counter += 1
        else: message += znak
    return message


