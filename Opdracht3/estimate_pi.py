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
        hits = count_hits(N,L)
        pi_res = 2*L*N/hits
        return pi_res, hits
        
def est_pi_long(N,L):
    hits = count_hits(N,L)
    P=hits/N
    pi_res_long = 2*L/(P -1) - 2*(math.sqrt((L**2-1)) + math.asin(1/L))/(P-1)
    #pi_res_long=2/P*math.acos(1/L)+2*L/P*(1-math.sqrt(1-(1/L)**2))
    return pi_res_long, hits
        

if len(sys.argv)==1 or len(sys.argv)==2:
    print('Use: estimate_pi.py N L')
elif float(sys.argv[2])>1:
    print('AssertionError: L should be smaller than 1')
    #pair = est_pi_long(int(sys.argv[1]), float(sys.argv[2]))
    #(res, hit) = pair
    #print(str(hit) +' hits in '+ str(sys.argv[1]) + ' tries\nPi = ' + str(res))
else:
   pair = est_pi(int(sys.argv[1]), float(sys.argv[2]))
   (res, hit) = pair
   print(str(hit) +' hits in '+ str(sys.argv[1]) + ' tries\nPi = ' + str(res))
    