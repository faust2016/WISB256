import time
import sys
#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
priemlijst = []
def priemen(n): 
    #priemlijst = []
    zeef = [True] * (n + 1)
    for p in range(2, n + 1):
        if zeef[p]:
           priemlijst.append(p)
           for i in range(p**2, n + 1, p):
               zeef[i] = False
    bestand = open(sys.argv[2], 'w')
 # for num in priemlijst:
       # bestand.write(str(num))
    bestand.write('\n'.join(str(num) for num in priemlijst))
    

start = time.perf_counter()
priemen(int(sys.argv[1]))
eind = time.perf_counter()
#print('Time required', eind - start, 'sec.')
print('Found ' + str(len(priemlijst)) + ' Prime numbers smaller than ' + str(sys.argv[1]) + 'in ' + str(eind-start) )