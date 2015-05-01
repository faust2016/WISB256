import time
import sys

def priemen(n): 
    priemlijst, zeef = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if zeef[p]:
           priemlijst.append(p)
           for i in range(p**2, n + 1, p):
               zeef[i] = False
    bestand = open('prime.dat', 'w')
    for num in priemlijst:
        bestand.write(str(num))

start = time.perf_counter()
priemen(90)
eind = time.perf_counter()
print('Time required', eind - start, 'sec.')