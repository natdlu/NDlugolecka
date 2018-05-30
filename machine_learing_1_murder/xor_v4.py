
import numpy as np
from klasa import Variable
from klasa import Potential

#------------------------------------------------------------------------------------------------------------ Zmienne

A = 2
B = 1
C = 0

one = 1
zero = 0


#----------------------------------------------------------------------------------------------------------- Stany

variable = [Variable() for i in range(3)]

variable[A].name = 'A';
variable[A].domain = ['one', 'zero']

variable[B].name = 'B';
variable[B].domain = ['one', 'zero']

variable[C].name = 'C';
variable[C].domain = ['one', 'zero']

#----------------------------------------------------------------------------------------------------------- Potencjaly

pot = [Potential() for i in range(3)]
pot[A].variables = np.array([A])
table = np.zeros((2))
table[one] = 0.65
table[zero] = 0.35
pot[A].table = table

print ("A:", pot[A].table)

pot[B].variables = np.array([B])
table = np.zeros((2))
table[one] = 0.77
table[zero] = 0.23
pot[B].table = table

print ("B:", pot[B].table)

pot[C].variables = np.array([C, A, B]) # kolejnosc
table = np.zeros([2, 2, 2])
table[one, zero, zero] = 0.1
table[one, zero, one] = 0.99
table[one, one, zero] = 0.8
table[one, one, one] = 0.25
pot[C].table = table
pot[C].table[zero][:][:]=1-pot[C].table[one][:][:] # dopelnienie p-bienstw

print ("C:", pot[C].table)

#------------------------------------------------------------------------------------------------ Rozklady i obliczenia

multpot = Potential()
multpot.variables = np.array([C, A, B])
table = np.zeros((2,2,2))

multpotA = Potential()
multpotA.variables = np.array([A, C])
tableA = np.zeros((2,2))

pa1c0 = tableA[one, zero] = pot[A].table[one] * (pot[C].table[zero, one, zero] * pot[B].table[zero] + pot[C].table[zero, one, one] * pot[B].table[one])
pa0c0 = tableA[zero, zero] = pot[A].table[zero] * (pot[C].table[zero, zero, zero] * pot[B].table[zero] + pot[C].table[zero, zero, one] * pot[B].table[one])

print ("\n> Rozklad laczny:")
print ("p(A = 1, C = 0) = ", pa1c0, "\np(A = 0, C = 0) = ", pa0c0)

multpotB = Potential()
multpotB.variables = np.array([B, C])
tableB = np.zeros((2,2))

pb1c0 = tableB[one, zero] = pot[B].table[one] * (pot[C].table[zero, zero, one] * pot[A].table[zero] + pot[C].table[zero, one, one] * pot[A].table[one])
pb0c0 = tableB[zero, zero] = pot[B].table[one] * (pot[C].table[zero, zero, zero] * pot[A].table[zero] + pot[C].table[zero, one, zero] * pot[A].table[one])

print ("p(B = 1, C = 0 = ", pb1c0, "\np(B = 0, C = 0) = ", pb0c0)

#---------------------------------------------------------------------------------------------------------- Rozwiazanie

pac = pa1c0/(pa1c0 + pa0c0)

print ("\nPrawdopodobienstwo zdarzenia A przy wiedzy o zdarzeniu C: \n\t> p(A = 1 | C = 0) = ", pac)