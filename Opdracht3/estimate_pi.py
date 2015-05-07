import random
import math
import sys

if len(sys.argv)==4:
    random.seed(sys.argv[3])

def drop_neelde(L):
    x = random.random()
    y = random.random()
    a = random.vonmisesvariate(0,0)
    xEnd = x+L*math.cos(a)
    yEnd = y+L*math.sin(a)
    if xEnd<0 or xEnd>1:
          return True
    else:
          return False
     
def count_hits(N,L):
    count = 0
    for i in range(0,N):
        if drop_neelde(L):
            count = count +1
    return count
            
def est_pi(N, L):
    if L<=1:
        hits = count_hits(N,L)
        pi_res = 2*L*N/hits
        return pi_res, hits
    else : 
        return 'Nog niet klaar'

print("Pi = " + str(est_pi(int(sys.argv[1]), int(sys.argv[2]))))
    