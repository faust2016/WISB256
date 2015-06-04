from lorenz import Lorenz
from numpy import *

sigma = 10
rho=28
beta = 8/3
L1 = Lorenz([-1,1,0],sigma,rho, beta)
u1=L1.solve(50,0.01)
L2 = Lorenz([-1.001,1.001,.001],sigma,rho,beta)
u2 = L2.solve(50,.01)
print(u1[0,0],u2[0,0]) # print values of x at t=0
print(u1[-1,0],u2[-1,0])
print(linalg.eigvals(L1.df(L1.begin)))