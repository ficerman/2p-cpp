import numpy
from numpy import random
a = int(input("Podaj liczbę kolumn i wierszy:"))
matryca1 = random.randint(100, size=(a, a))
matryca2 = random.randint(100, size=(a, a))
dod = matryca1 + matryca2
mn = matryca1 * matryca2

print("\nPierwsza macierz:")
print(matryca1)
print("\nDruga macierz:")
print(matryca2)
print("\nSuma macierzy:")
print(dod)
print("\nIloczyn macierzy:")
print(mn)