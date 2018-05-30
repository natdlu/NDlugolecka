# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:49:29 2018

@author: Natala

"""

import numpy as np
import funkcje as f
from klasa import Variable
from klasa import Potential
import matplotlib.pyplot as plt

liczba_sensorow = 20
sensory = f.losuj_punkty_pomiarowe(liczba_sensorow)
eksplozja = f.losuj_punkty_eksplozji()

#################################################################################### Stale

sigma_2 = 0.5 
delta = 0.05 # skok o siatce

eksplozja_x = 0
eksplozja_y = 1

pomiar = f.obserwacje(sensory, eksplozja, liczba_sensorow, sigma_2) ################ Eksperyment

print ("\nMiejsce wybuchu:\n", "\t> x = ", eksplozja[0], "\n\t> y = ", eksplozja[1])
print ("\t(", eksplozja[0], ",", eksplozja[1], ")")

f.zapisz_do_pliku(pomiar, sensory, liczba_sensorow) ################################ Zapis do pliku

#################################################################################### Tworzenie siatki

siatka = np.arange(-1, 1.001, delta)
siatka_rozmiar = len(siatka)

siatka_tab = [Variable(), Variable()]
siatka_tab[eksplozja_x].domain = siatka
siatka_tab[eksplozja_y].domain = siatka

pot = Potential()
pot.Variables = np.array([eksplozja_x, eksplozja_y])

siatka_rozmiar_tab = np.zeros((siatka_rozmiar, siatka_rozmiar))

################################################################################### Obliczanie wartosci 
################################################################################## dla punktow siatki
################################################################################### pstwa, odleglosci etc

for y in range(siatka_rozmiar): # petla po siatce
    for x in range(siatka_rozmiar):
        skok = [-1 + delta*y, -1 + delta*x] # skok o dana delte na siatce
        p = 1
        eksplozja_odleglosc = f.odleglosc_do_kwadratu(skok, eksplozja)
        
        if (eksplozja_odleglosc < 1.0 ):
            p_tab = f.obserwacje_p(sigma_2, p, sensory, skok, liczba_sensorow, pomiar)
            
            for i in range(liczba_sensorow):
                p = p * p_tab[i]
                #print(p)
        
        else:            
            p = 0
            
        siatka_rozmiar_tab[x, y] = p
    
    
pot.siatka_rozmiar_tab = siatka_rozmiar_tab

"""
suma = np.sum(pot.siatka_rozmiar_tab) ############################################ Dostosowanie pstwa do 1
pot.siatka_rozmiar_tab = (pot.siatka_rozmiar_tab)/suma
suma = np.sum(pot.siatka_rozmiar_tab)"""
#print(siatka_rozmiar_tab)
#print(suma)
#print(np.amax(siatka_rozmiar_tab))


estymacja_wspolrzedne = np.unravel_index(np.argmax(pot.siatka_rozmiar_tab), pot.siatka_rozmiar_tab.shape)
EX = round(-1 + delta * estymacja_wspolrzedne[1], 2)
EY = round(-1 + delta * estymacja_wspolrzedne[0], 2)

print('\nWybuch w: ', eksplozja[0], eksplozja[1])
print('Estymacja: ', EX, EY)
        
f.wykres(delta, pot.siatka_rozmiar_tab, eksplozja, EX, EY)
