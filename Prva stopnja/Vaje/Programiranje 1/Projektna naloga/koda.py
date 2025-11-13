import csv
import os
import re
import sys

import requests


def pripravi_imenik(ime_datoteke):
        '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
        imenik = os.path.dirname(ime_datoteke)
        if imenik:
            os.makedirs(imenik, exist_ok=True)


def shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False):
        '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
        try:
            print('Shranjujem {} ...'.format(url), end='')
            sys.stdout.flush()
            if os.path.isfile(ime_datoteke) and not vsili_prenos:
                print('shranjeno že od prej!')
                return
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            print('stran ne obstaja!')
        else:
            pripravi_imenik(ime_datoteke)
            with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
                datoteka.write(r.text)
                print('shranjeno!')


def vsebina_datoteke(ime_datoteke):
        '''Vrne niz z vsebino datoteke z danim imenom.'''
        with open(ime_datoteke, encoding='utf-8') as datoteka:
            return datoteka.read()


def zapisi_csv(slovarji, imena_polj, ime_datoteke):
        '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
            writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
            writer.writeheader()
            for slovar in slovarji:
                writer.writerow(slovar)


vzorec = re.compile(
        r'<span class=".*?rank\d">(?P<rang>\d+?)</span>.*?'
        r'<a class=".*?" href=".*?" id="(?P<id>#area\d+?)" rel=".*?".*?'
        r'<div class=".*?"><a .*?>(?P<naslov>.*?)</a>.*?</div><br><div.*?>.*?'
        r'(?P<tip>\w+?) '
        r'(?P<st_epizod>\(\d* eps\))<br>.*?'
        r'(?P<leto>\d{4}) - .*?<br>.*?'
        r'(?P<ogledi>\d*?,*?\d*?,*?\d*?) members.*?</div></div>.*?'
        r'<td.*?>(?P<ocena>\d+?.\d+?).*?</div>.*?',
        re.DOTALL
)


def izloci_podatke_animeja(ujemanje_animeja):
        '''Zajete podatke pretvori v bolj primerno obliko'''
        podatki_animeja = ujemanje_animeja.groupdict()
        podatki_animeja['rang'] = int(podatki_animeja['rang'].strip())
        podatki_animeja['id'] = podatki_animeja['id'].strip()
        podatki_animeja['naslov'] = podatki_animeja['naslov'].replace("&amp;#039;", "'").strip()
        podatki_animeja['tip'] = podatki_animeja['tip'].strip()
        podatki_animeja['st_epizod'] = int(podatki_animeja['st_epizod'].replace(" eps", "").replace("(", "").replace(")", "").strip())
        podatki_animeja['leto'] = int(podatki_animeja['leto'])
        podatki_animeja['ogledi'] = int(podatki_animeja['ogledi'].replace(',', "").strip())
        podatki_animeja['ocena'] = float(podatki_animeja['ocena'].replace(',', '.'))
        return podatki_animeja


for i in range(60):
        k = 50 * i
        url = "https://myanimelist.net/topanime.php?limit={}".format(k)
        shrani_spletno_stran(url, 'htmlji/top-anime-{}.html'.format(i+1))


podatki_animeja = []
for i in range(60):
        vsebina = vsebina_datoteke(
                'htmlji/top-anime-{}.html'.format(i+1))
        for ujemanje_animeja in vzorec.finditer(vsebina):
                podatki_animeja.append(izloci_podatke_animeja(ujemanje_animeja))
        print('dodal {}'.format(i+1))
zapisi_csv(podatki_animeja, ['rang', 'id', 'naslov', 'tip', 'st_epizod', 'leto', 'ogledi', 'ocena'], 'obdelani-podatki/vsi-animeji.csv')

serije = []
for anime in podatki_animeja:
        if anime['tip'] == 'TV':
                serije.append(anime)
zapisi_csv(serije, ['rang', 'id', 'naslov', 'tip', 'st_epizod', 'leto', 'ogledi', 'ocena'], 'obdelani-podatki/vse-anime-serije.csv')
