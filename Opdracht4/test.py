import bisection
import math
print(bisection.findRoot(lambda x:x*(x-1)-1,-1,3,.01))
print(bisection.findAllRoots(lambda x:x*(x-1)-1,-1,3,.01))
#print(bisection.findAllRoots(lambda x:x**2-2,-2,2,.01))
