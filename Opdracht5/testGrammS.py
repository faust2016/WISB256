from vector import *
v0 = Vector(2,[3,1])
v1 = Vector(2,[2,2])
W = GrammSchmidt([v0,v1])
print(W[0])