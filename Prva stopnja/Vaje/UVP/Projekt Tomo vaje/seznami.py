## Primerjanje
#
# 1. naloga
# Definirajte funkcijo `vecji_element(seznam, x)` ki sprejme seznam `seznam` in 
# število `x` in kot rezultat vrne ali `seznam` vsebuje število večje od `x`.
# 
#     >>> vecji_element([3,6,2], 5)
#     True
#     >>> vecji_element([7,5,1], 8)
#     False
#     >>> vecji_element([3], 3)
#     False
#
def vecji_element(seznam, x):
    for y in seznam:
        if y > x:
            return True
    return False
#
# 2. naloga
# Definirajte funkcijo `prvi_najvecji(seznam)`, ki kot rezultat vrne `True`, če 
# je prvi element seznama večji ali enak preostalim elementom seznama, sicer 
# vrne `False`.
# 
#     >>> prvi_najvecji([5,3,6,2])
#     False
#     >>> prvi_najvecji([8,7,5,1])
#     True
#
def prvi_najvecji(seznam):
    for x in seznam[1:]:
        if x > seznam[0]:
            return False
    return True
#
# 3. naloga
# Definirajte funkcijo `vsi_vecji(seznam1, seznam2)`, ki sprejme dva seznama,
# `seznam1` in `seznam2`, ter preveri ali je vsak element seznama `seznam1` 
# strogo večji od vseh elementov seznama `seznam2`.
# 
#     >>> vsi_vecji([2,4], [1,3])
#     False
#     >>> vsi_vecji([5,8], [1,2,4])
#     True
#
def vsi_vecji(seznam1, seznam2):
    for x in seznam1:
        for y in seznam2:
            if y >= x:
                return False
    return True


## Seznami
#
# 1. naloga
# Sestavite funkcijo `razpolovi(l)`, ki seznam `l` čim bolj enakomerno razdeli
# na dva podseznama in vrne nabor, ki vsebuje ta dva podseznama. Pri tem naj bo
# dolžina prvega podseznama krajša ali enaka dolžini drugega podseznama.
# 
#     >>> razpolovi(["a", "b", "c", "d"])
#     (["a", "b"], ["c", "d"])
#
def razpolovi(l):
    polovica = (len(l) - (len(l) % 2)) // 2
    return l[:polovica], l[polovica:]
#
# 2. naloga
# Sestavite funkcijo `zamenjaj(l,i,j)`, ki iz seznama `l` sestavi nov seznam,
# v katerem sta elementa na mestih `i` in `j` zamenjana med sabo. Če indeksa
# `i` in `j` ne ustrezata nobenemu elementu, naj funkcija vrne kar seznam `l`.
# 
#     >>> zamenjaj([1,2,3,4], 1, 2)
#     [1,3,2,4]
#     >>> zamenjaj([1,2,3,4], 1, 2017)
#     [1,2,3,4]
#
def zamenjaj(l,i,j):
    if not (i in range(len(l)))  or not (j in range(len(l))):
        return l
    else:
        zacasni_clen = l[i]
        l[i] = l[j]
        l[j] = zacasni_clen
        return l
        
#
# 3. naloga
# Sestavite funkcijo `porezi(l)`, ki seznamu `l` po vrsti odstranjuje elemente
# z leve in vrne seznam podseznamov, ki jih na ta način dobimo.
# 
#     >>> porezi([1,2,3,4])
#     [[1,2,3,4], [2,3,4], [3,4], [4], []]
#
def porezi(l):
    if l == []:
        return [l]
    else:
        return [l] + porezi(l[1:])
#
# 4. naloga
# Sestavite funkcijo `najvecji_element(l)`, ki vrne največji element seznama `l`.
# Če je seznam `l` prazen, naj funkcija vrne `None`.
# 
#     >>> najvecji_element([2,4,3,1])
#     4
#
def najvecji_element(l):
    so_far = None
    for x in l:
        if (so_far is None) or x > so_far:
            so_far = x
    return so_far
            

## Praštevila
#
# 1. naloga
# Definirajte funkcijo `je_deljivo_s_katerim_od(n, seznam)`, ki vrne `True`
# natanko tedaj, ko je število `n` deljivo z vsaj kakšnim številom iz seznama
# števil `seznam`.
#
def je_deljivo_s_katerim_od(n, seznam):
    for x in seznam:
        if n % x == 0:
            return True
    return False
#
# 2. naloga
# Definirajte funkcijo `prastevila_do(n)`, ki vrne seznam vseh praštevil,
# ki so manjša ali enaka `n`.
#
def prastevila_do(n):
    if n <= 1:
        return []
    prejsnja = prastevila_do(n-1)
    if je_deljivo_s_katerim_od(n, prejsnja):
        return prejsnja
    else:
        return prejsnja + [n]
        
#
# 3. naloga
# Definirajte funkcijo `je_prastevilo(n)`, ki vrne `True` natanko tedaj, ko
# je število `n` praštevilo.
#
def je_prastevilo(n):
    return n in prastevila_do(n * n)


## Nizi
#
# 1. naloga
# Sestavite funkcijo `prezrcali(s)`, ki vrne niz, ki ga dobimo, če niz `s`
# preberemo z desne proti levi.
# 
#     >>> prezrcali("abeceda")
#     adeceba
#
def prezrcali(s):
    if s == "":
        return ""
    else:
        return s[-1] + prezrcali(s[:-1])
#
# 2. naloga
# Sestavite funkcijo `je_palindrom(s)`, ki preveri, če je niz `s` palindrom.
# 
#     >>> je_palindrom("maram")
#     True
#
def je_palindrom(s):
    return s == prezrcali(s)
#
# 3. naloga
# Sestavite funkcijo `odstrani_presledke(s)`, ki vrne niz, ki ga dobimo,
# če iz niza `s` odstranimo vse presledke.
# 
#     >>> odstrani_presledke("Ni vsak dan nedelja")
#     Nivsakdannedelja
#
def odstrani_presledke(s):
    if s == "":
        return ""
    elif s[0] == " ":
        return odstrani_presledke(s[1:])
    else:
        return s[0] + odstrani_presledke(s[1:])
        

## Krogi
#
# 1. naloga
# Sestavite funkcijo `v_uniji(x0, y0, krogi)`, ki vrne `True`, če točka
# `(x0, y0)` leži v vsaj enem krogu v danem seznamu `krogi`, in `False`
# sicer. Ta seznam je sestavljen iz trojic `(x, y, r)`, ki
# predstavljajo kroge s središči `(x, y)` in radiji `r`.
#
#((x0 - z[0]) ** 2) + ((y0 - z[1]) ** 2) == z[2] ** 2
def v_uniji(x0, y0, krogi):
    for z in krogi:
        if ((x0 - z[0]) ** 2) + ((y0 - z[1]) ** 2) <= z[2] ** 2:
            return True
    return False
#
# 2. naloga
# Sestavite funkcijo `v_preseku(x, y, krogi)`, ki vrne `True`, če točka
# `(x, y)` leži v vseh krogih v danem seznamu `krogi`, in `False`
# sicer.
#
def v_preseku(x, y, krogi):
    for z in krogi:
        if ((x - z[0]) ** 2) + ((y - z[1]) ** 2) > z[2] ** 2:
            return False
    return True
#
# 3. naloga
# Sestavite funkcijo `pravokotnik(krogi)`, ki poišče najmanjši pravokotnik,
# ki vsebuje unijo vseh krogov iz danega seznama `krogi`. Pravokotnik
# naj vrne kot nabor `(x_min, y_min, x_max, y_max)`, torej najprej
# koordinati oglišča spodaj levo, nato pa koordinati oglišča zgoraj desno.
#
# krog: [(x, y, r)]
def pravokotnik(krogi):
    x_min = krogi[0][0] - krogi[0][2] # x - r
    y_min = krogi[0][1] - krogi[0][2] # y - r
    x_max = krogi[0][0] + krogi[0][2] # x + r
    y_max = krogi[0][1] + krogi[0][2] # y + r
# tako dobimo za en krog maksimalne dimenzije, skozi koordinate.
    if len(krogi) == 1:
        return (x_min, y_min, x_max, y_max)
#v kolikor imamo več krogov, velja enak proces, a za več elementov.
# Torej najprej poračunamo koordinate za prvi krog, nato pa za naslednjega
#v seznamu in tako dalje. da to dosežemo, si pomagamo z rekurzijo.
#ker nas zanima najmanjši rezultat, za vsako koordinato izberemo minimum
    else:
        rest = pravokotnik(krogi[1:])
        return (min(x_min, rest[0]), min(y_min, rest[1]),
                max(x_max, rest[2]), max(y_max, rest[3]))



## Najkrajši seznami
#
# 1. naloga
# Sestavite funkcijo `najkrajsi_seznam(seznami)`, ki vrne najkrajši seznam
# v seznamu seznamov `seznami`. Če je takih seznamov več, naj funkcija vrne
# prvega. Če je seznam `seznami` prazen, naj funkcija vrne vrednost `None`.
# 
#     >>> najkrajsi_seznam([[3, 6], [17, 5, 2], [5], [6, 3]])
#     [5]
#
# [[1, 2, 3], [2, 2, 4], [], [3]]
def najkrajsi_seznam(seznami):
    if seznami == []:
        return None
    najkrajsi = None
    for seznam in seznami:
        if najkrajsi == None or len(seznam) < len(najkrajsi):
            najkrajsi = seznam
    return najkrajsi
#
# 2. naloga
# Sestavite funkcijo `najkrajsi_neprazen_seznam(seznami)`, ki vrne najkrajši
# neprazen seznam v seznamu seznamov `seznami`. Če je takih seznamov več, naj
# funkcija vrne prvega. Če v seznamu `seznami` ni nepraznega seznama, naj
# funkcija vrne vrednost `None`.
# 
#     >>> najkrajsi_neprazen_seznam([[3, 6], [17, 5, 2], [5], [6, 3]])
#     [5]
#
def najkrajsi_neprazen_seznam(seznami):
    najkrajsi = None
    for seznam in seznami:
        if seznam and (najkrajsi == None or len(seznam) < len(najkrajsi)):
            najkrajsi = seznam
    return najkrajsi
#
# 3. naloga
# Imejmo seznam seznamov seznamov … seznamov števil, na primer
# 
#     [[[8, 9], [6, 7]], [[5], [4]], [1, 2, 3]]
# 
# Predpostavite lahko, da vsak seznam vsebuje bodisi le števila bodisi le
# sezname.
# 
# Sestavite funkcijo `najkrajsi_vgnezden_seznam(seznam)`, ki vrne najkrajši
# seznam števil v seznamu gnezdenih seznamov `seznam`. Če je takih seznamov več,
# naj funkcija vrne prvega.
# 
#     >>> najkrajsi_vgnezden_seznam([[[8, 9], [6, 7]], [[5], [4]], [1, 2, 3]])
#     [5]
#     >>> najkrajsi_vgnezden_seznam([1, 2, 3])
#     [1, 2, 3]
#     >>> najkrajsi_vgnezden_seznam([[1, 2, 3], []])
#     []
#     >>> najkrajsi_vgnezden_seznam([])
#     []
#
# Didn't know how to do this one so I just #Hacked it
def najkrajsi_vgnezden_seznam(seznam):
    if len(seznam) == 0 or type(seznam[0]) == int:
        return seznam
    else:
        podseznami = []
        for podseznam in seznam:
            podseznami += [najkrajsi_vgnezden_seznam(podseznam)]
        return najkrajsi_seznam(podseznami)



