from scipy.integrate import odeint
from numpy import *

class Lorenz:
    def __init__(self, start, sigma = 10, rho = 28, beta = 8/3):
        self.x0 = start[0]
        self.y0 = start[1]
        self.z0 = start[2]
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        self.begin = [self.x0,self.y0,self.z0]
        
    def func(self,init,t):
        [x,y,z]=init
        dx = self.sigma * (y-x)
        dy = x*(self.rho-z)-y
        dz = x*y-self.beta*z
        return [dx,dy,dz]    
        
    def solve(self, T, dt):
        tWaardes=arange(0,T+dt,dt)
        a=odeint(self.func,self.begin, tWaardes)
        return a
        
    def df(self,u):
        [x,y,z] = u
        b = arange(9).reshape(3,3)
        b[0,0] = -1*self.sigma
        b[0,1] = self.sigma
        b[0,2] = 0
        b[1,0] = self.rho-z
        b[1,1] = -1
        b[1,2] = x
        b[2,0] = y
        b[2,1] = x
        b[2,2] = -1*self.beta
        return b
        
    def isStable(self,u):
       eigv = linalg.eigvals(self.df(u))
       for i in range(len(eigv)):
           if eigv[i]>=0:
               return False
           return True