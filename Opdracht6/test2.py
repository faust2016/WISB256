from scipy.integrate import odeint
from numpy import *

b = arange(9).reshape(3,3)
print(b)
b[2,1]=39
print(b)