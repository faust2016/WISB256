from lorenz import Lorenz

sigma = 10
rho=28
beta = 8/3
L1 = Lorenz([-1,1,0],sigma,rho, beta)
u1=L1.solve(50,0.01)
print(u1)