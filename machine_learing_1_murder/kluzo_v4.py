# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:35:13 2018

@author: Natala
"""

import numpy as np
from klasa import Variable
from klasa import Potential 


#---------------------------------------------------------------------------------------------------------- Zmienne

rzeznik = 2
sprzataczka = 1
noz = 0

morderca = 1
niemorderca = 0

uzyty = 1
nieuzyty = 0

#---------------------------------------------------------------------------------------------------------- Stany

variable = [Variable() for i in range(3)]

variable[rzeznik].name = 'rzeznik';
variable[rzeznik].domain = ['muorderca', 'niemorderca']

variable[sprzataczka].name = 'sprzataczka';
variable[sprzataczka].domain = ['morderca', 'niemorderca']

variable[noz].name = 'noz';
variable[noz].domain = ['uzyty', 'nieuzyty']

#---------------------------------------------------------------------------------------------------------- Potencjaly

pot = [potential() for i in range(3)]
pot[rzeznik].variables = np.array([rzeznik])
table = np.zeros((2))
table[morderca] = 0.6
table[niemorderca] = 0.4
pot[rzeznik].table = table

print ("Rzeznik:", pot[rzeznik].table)

pot[sprzataczka].variables = np.array([sprzataczka])
table = np.zeros((2))
table[morderca] = 0.2
table[niemorderca] = 0.8
pot[sprzataczka].table = table

print ("Sprzataczka:", pot[sprzataczka].table)

pot[noz].variables = np.array([noz, rzeznik, sprzataczka]) # kolejnosc
table = np.zeros([2, 2, 2])
table[uzyty, niemorderca, niemorderca] = 0.3
table[uzyty, niemorderca, morderca] = 0.2
table[uzyty, morderca, niemorderca] = 0.6
table[uzyty, morderca, morderca] = 0.1
pot[noz].table = table
pot[noz].table[nieuzyty][:][:]=1-pot[noz].table[uzyty][:][:] # dopelnienie p-bienstw

print ("Noz:", pot[noz].table)

multpot=Potential()
multpot.Variables = np.array([noz, rzeznik,sprzataczka])
table = np.zeros((2,2,2))

#------------------------------------------------------------------------------------------------------- Rozklad laczny

p100 = table[uzyty, niemorderca, niemorderca] = pot[noz].table[uzyty, niemorderca, niemorderca]* pot[rzeznik].table[niemorderca] * pot[sprzataczka].table[niemorderca]
p101 = table[uzyty, niemorderca, morderca] = pot[noz].table[uzyty, niemorderca, morderca]* pot[rzeznik].table[niemorderca] * pot[sprzataczka].table[morderca]
p111 = table[uzyty, morderca, morderca] = pot[noz].table[uzyty, morderca, morderca]* pot[rzeznik].table[morderca] * pot[sprzataczka].table[morderca]
p110 = table[uzyty, morderca, niemorderca] = pot[noz].table[uzyty, morderca, niemorderca] * pot[rzeznik].table[morderca] * pot[sprzataczka].table[niemorderca]
p000 = table[nieuzyty, niemorderca, niemorderca] = pot[noz].table[nieuzyty, niemorderca, niemorderca] * pot[rzeznik].table[niemorderca] * pot [sprzataczka].table[niemorderca]
p001 = table[nieuzyty, niemorderca, morderca] = pot[noz].table[nieuzyty, niemorderca, morderca] * pot[rzeznik].table[niemorderca] * pot[sprzataczka].table[morderca]
p010 = table[nieuzyty, morderca, niemorderca] = pot[noz].table[nieuzyty, morderca, niemorderca] * pot[rzeznik].table[morderca] * pot[sprzataczka].table[niemorderca]
p011 = table[nieuzyty, morderca, morderca] = pot[noz].table[nieuzyty, morderca, morderca] * pot[rzeznik].table[morderca] * pot[sprzataczka].table[morderca]


print ("\n> Rozklad laczny:")
print ("000 | ", p000, "\n001 | ", p001, "\n010 | ", p010, "\n011 | ", p011, "\n100 | ", p100, "\n101 | ", p101, "\n110 | ", p110, "\n111 | ", p111, "\n")


#------------------------------------------------------------------------------------------------------------- Wynik

print ("Prawdopodobienstwo zdarzenia, ze rzeznik jest morderca przy zalozeniu ze noz zostal uzyty:")

print ("\t> a posteriori:", (p111 + p110)/(p111 + p110 + p101 + p100))
print ("\t> a priori:", pot[rzeznik].table[morderca])
