from scipy.integrate import odeint
from numpy import arange

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