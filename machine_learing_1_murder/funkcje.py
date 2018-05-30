# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:48:21 2018

@author: Natala
"""

import numpy as np
import sys
import matplotlib.pyplot


def odleglosc_do_kwadratu(a, b, dim = 2):
	rob = [(a[i]-b[i])**2 for i in range(dim)]
	return sum(rob)
	
def losuj_punkty_pomiarowe(N):
	losuj = []
	for i in range (0, N):
		losuj.append(np.random.rand() *np.pi*2)
	katy=sorted(losuj)
	x = np.array ([np.sin(katy[i]) for i in range (N)])
	y = np.array ([np.cos(katy[i]) for i in range (N)])
		
	punkty_pomiarowe = []
	for i in range (0,N):
		rob = [x[i], y[i]]
		punkty_pomiarowe.append(rob)
	return punkty_pomiarowe
	
def losuj_punkty_eksplozji():
	ex=2
	ey=2
	odleglosc_e = odleglosc_do_kwadratu([ex, ey], [0, 0])
	while (odleglosc_e > 1):
		ex = np.random.rand()
		ey = np.random.rand()
		if (np.random.rand() < 0.5):
			ex = -ex
		if (np.random.rand() < 0.5):
			ey = -ey
		odleglosc_e = odleglosc_do_kwadratu([ex, ey],[0, 0])
	e = [ex, ey]
	return e
	
def obserwacje(punkty, e, N, sigma2):
	d2 = [odleglosc_do_kwadratu(punkty[i], e) for i in range(N)]
	obserwacje = [1/(d2[i] + 0.1) for i in range (N)]
	zaburzenie = [obserwacje[i] + np.random.normal(0, sigma2) for i in range(N)]
	return zaburzenie

def obserwacje_p(sigma_2, p, sensory, skok, N, pomiar):
    
    stala_sigma = 2 * (sigma_2**2)
    stala_pi = 1 / np.sqrt(2 * np.pi * (sigma_2**2))
    
    d2 = [odleglosc_do_kwadratu(sensory[i], skok) for i in range(N)]
    obserwacje = [1/(d2[i] + 0.1) for i in range (N)]
    p_tab = [stala_pi * np.exp((-1 / stala_sigma) * ((pomiar[i] - obserwacje[i]) ** 2)) for i in range(N)]
      
    return p_tab

def zapisz_do_pliku(pomiar, sensory, liczba_sensorow):

    file_measurement = open('pomiar_dane.txt', 'w') ########################### zapis do pliku
    print("\nDANE DO INTERFERENCJI:\n")
    print("Lp \t|\t\tWspolrzedne sensora\t\t|\t\tPomiar")
    print ("--------------------------------------------------------------------------------")

    for i in range(0, liczba_sensorow):
        line = str(sensory[i]) + "\t|\t" + str(pomiar[i])
        line2 = str(sensory[i]) + "\t|\t" + str(pomiar[i]) + "\n"
        collumn = "Wspolrzedne sensora [x, y]\t\t|Pomiar"

        print (i+1, "\t|", line)

        file_measurement.write(line2)

    file_measurement.write(collumn)
    file_measurement.close()


def wykres(delta, pot, eksplozja, EX, EY):
    
    import matplotlib.pyplot as plt
    
    x = np.arange(-1, 1.001, delta)
    y = np.arange(-1, 1.001, delta)
    
    X, Y = np.meshgrid(x,y)
    plt.figure(figsize=(10,8))
    plt.contourf(X, Y, pot)
    plt.colorbar()
    plt.ylabel('x')
    plt.xlabel('y')
    plt.title('Detekcja')
    plt.plot(eksplozja[0], eksplozja[1], 'ro')
    plt.plot(EX, EY, 'go')
    plt.annotate('wybuch', (eksplozja[0], eksplozja[1]))
    plt.annotate('estymacja', (EX, EY))
    plt.show()


