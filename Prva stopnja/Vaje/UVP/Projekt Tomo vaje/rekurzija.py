## Vsote potenc
#
# 1. naloga:
# Sestavite funkcijo `vsota_prvih(n)`, ki vrne vsoto prvih `n` naravnih števil.
#
def vsota_prvih(n):
    if n == 0:
        return 0
    else:
        return n + vsota_prvih(n - 1)
#
# 2. naloga:
# Sestavite funkcijo `vsota_prvih_kvadratov(n)`, ki vrne vsoto kvadratov
# prvih `n` naravnih števil.
#
def vsota_prvih_kvadratov(n):
    if n == 0:
        return 0
    else:
        return n ** 2 + vsota_prvih_kvadratov(n - 1)
#
# 3. naloga:
# Sestavite funkcijo `vsota_prvih_potenc(n, k)`, ki vrne vsoto `k`-tih potenc
# prvih `n` naravnih števil. Argument `k` naj bo neobvezen in naj ima privzeto
# vrednost `1`.
#
def vsota_prvih_potenc(n, k=1):
    if n == 0:
        return 0
    else:
        return (n ** k) + vsota_prvih_potenc((n - 1), k)

## Vsote števk
#
# 1. naloga
# Sestavite funkcijo `vsota_stevk(n)`, ki vrne vsoto števk števila `n`.
#
def vsota_stevk(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + vsota_stevk(n // 10)
#
# 2. naloga
# Sestavite funkcijo `vsota_vecjih_stevk(n, k)`, ki vrne vsoto tistih števk
# števila `n`, ki so večje ali enake `k`. Če parametra `k` ne podamo, naj
# funkcija vrne vsoto vseh števk števila `n`.
#
def vsota_vecjih_stevk(n, k = 1):
    if n == 0:
        return 0
    elif (n % 10) >= k:
        return (n % 10) + vsota_vecjih_stevk((n // 10), k)
    else:
        return vsota_vecjih_stevk((n // 10), k)
#
# 3. naloga
# Sestavite funkcijo `vsota_stevk_stevil_med(m, n)`, ki vrne vsoto števk
# vseh števil med vključno `m` in `n`.
#
def vsota_stevk_stevil_med(m, n):
    if m == n:
        return vsota_stevk(m)
    elif 0 <= m < n:
        return vsota_stevk(m) + vsota_stevk_stevil_med(m + 1, n)
    elif 0 <= n < m:
        return 0
# Raje:
#def vsota_stevk_stevil_med(m, n):
#    if m > n:
#        return 0
#    else:
#        return vsota_stevk(m) + vsota_stevk_stevil_med(m + 1, n)

#
# 4. naloga
# Sestavite **učinkovito** funkcijo `najmanjse_stevilo_z_vsoto_stevk(n)`,
# ki izračuna točno to, kar piše v njenem imenu.
#
def najmanjse_stevilo_z_vsoto_stevk(n):
    if 0 <= n <= 9:
        return n
    else:
        return 9 + 10 * najmanjse_stevilo_z_vsoto_stevk((n - 9))
        

# (n - vsota_stevk(n)) 'first digit' * 9


## Binomski simbol
#
# 1. naloga
# Ena najbolj znanih formul za binomski simbol je
# $$\binom{n}{k} = \frac{n!}{k! \cdot (n - k)!}$$
# Definirajte funkcijo `binomski_fakulteta(n, k)`, ki s pomočjo te formule
# izračuna binomski simbol. Ne pozabite si definirati tudi funkcije `fakulteta`.
# 
def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)

def binomski_fakulteta(n, k):
    if n == k:
        return 1
    elif k < n:
        return fakulteta(n) / (fakulteta(k) * fakulteta(n - k))
# 
# 2. naloga
# Seveda to ni edini način za izračun binomskega simbola. Lahko ga izračunamo
# tudi kot:
# $$\binom{n}{k} = \binom{n - 1}{k} + \binom{n - 1}{k - 1}$$
# pri čemer je treba upoštevati, da velja $\binom{n}{0} = \binom{n}{n} = 1$.
# Definirajte funkcijo `binomski_rekurzija(n, k)`, ki binomski simbol definira
# po tej formuli.
# 
def binomski_rekurzija(n, k):
    if k == n or k == 0:
        return 1
    else:
        return binomski_rekurzija((n - 1), k) + binomski_rekurzija((n - 1), (k - 1))
# 
# 3. naloga
# Bolj učinkovit način za izračun binomskega simbola pa je:
# $$\binom{n}{k} = \frac{n - k + 1}{k} \binom{n}{k - 1}$$
# pri čemer je treba upoštevati, da velja $\binom{n}{0} = 1$.
# Definirajte še funkcijo `binomski_ucinkovit(n, k)`, ki binomski simbol
# definira po tej formuli. Pri tem pazite, da za rezultat vrnete celo število.
# 
def binomski_ucinkovit(n, k):
    if k == 0:
        return 1
    else:
        return (n - k + 1) * binomski_ucinkovit(n, (k - 1)) // k



## Prepisovanje
#
# 
# 1. naloga
# Pravimo, da sta si dva niza sumljivo podobna, če sta enako dolga in se 
# razlikujeta v kvečjemu eni črki. Napišite funkcijo `sumljivo_podobna(s, t)`,
# ki vrne  `True`, če sta si niza `s` in `t` sumljivo podobna, in `False` sicer.
# 
# _Namig_: pomagajte si z dodatno funkcijo, ki šteje število različnih 
# istoležnih znakov.
#
def stetje_znakov(s, t):
    if s == "" or t == "":
	    return 0
    elif s[0] == t[0]:
        return stetje_znakov(s[1:], t[1:])
    else:
        return 1 + stetje_znakov(s[1:], t[1:])
def dolzina(s):
    if s == "":
        return 0
    else:
        return 1 + dolzina(s[1:])
    
def sumljivo_podobna(s, t):
    if (stetje_znakov(s, t) <= 1) and dolzina(s) == dolzina(t):
        return True
    else:
        return False

# obstaja len(s), ki je ze vnaprej definirana,
# in naredi isto kot tvoja funkcija dolzina(s)
# Lepše:
# def sumljivo_podobna(s,t):
# return (stetje_znakov(s, t) <= 1) and dolzina(s) == dolzina(t)
# =====================================================================@012849=
# 2. naloga
# Razvijmo boljši način za primerjanje podobnosti dveh besedil. Na voljo imamo 
# tri operacije: vstavi črko, zbriši črko in zamenjaj črko. 
# Napišite funkcijo `stevilo_operacij(s, t)`, ki izračuna najmanjše število
# operacij, ki jih potrebujemo, da niz `s` pretvorimo v niz `t`.
# 
def stevilo_operacij(s, t):
    if s == "":
        return len(t)
    elif t == "":
        return len(s)
    else:
        if s[0] == t[0]:
            first_difference = 0
        elif s[0] != t[0]:
            first_difference = 1
        return min(stevilo_operacij(s[1:], t) + first_difference,
                   first_difference + stevilo_operacij(s[1:], t[1:]),
                   first_difference + stevilo_operacij(s, t[1:]))


# -*- coding: utf-8 -*-
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
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1
#
# 2. naloga
# Sestavite funkcijo `dolzina_zaporedja(n)`, ki izračuna dolžino Collatzovega
# zaporedja, ki se začne s številom `n`.
#
def dolzina_zaporedja(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + dolzina_zaporedja((n / 2))
    else:
        return 1 + dolzina_zaporedja(((3 * n) + 1))
# raje:
# def dolzina_zaporedja(n):
# if n == 1:
# return 1
# else:
# return 1 + dolzina_zaporedja(naslednji_clen(n))

#
# 3. naloga
# Sestavite funkcijo `najvecji_clen(n)`, ki izračuna največji člen v
# Collatzovem zaporedju, ki se začne s številom `n`.
#
def najvecji_clen(n):
    if n == 1:
        return 1
    else:
        return max(n, najvecji_clen(naslednji_clen(n)))
# Pomni: obstajata funkciji max in min, s katerima bi si lahko že na začetku
# pomagal in bi končal v roku 10 minut. Dana rešitev je uradna, stara pa je
# bila zbootlegana, da je dala rešitve za poskuse, ki jih je program hotel.
#
# 4. naloga
# Sestavite funkcijo `najdaljse_zaporedje(m, n)`, ki vrne dolžino najdaljšega
# zaporedja med vsemi tistimi Collatzovimi zaporedji, ki se začnejo s števili
# med (vključno) `m` in `n`.
#
def najdaljse_zaporedje(m, n):
    if m == n:
        return dolzina_zaporedja(m)
    else:
        return max(dolzina_zaporedja(m), najdaljse_zaporedje((m + 1), n))


