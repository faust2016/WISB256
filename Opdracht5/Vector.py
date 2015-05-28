class Vector:
    def __init__(self,dim,val=0.0000):
        self._data=[] 
        if type(val)==list:
            for i in range(0,dim):
                self._data.append(val[i])
        else: 
            for i in range(0,dim):
                self._data.append(val)
   
    def __str__(self):
        draad = ''
        for i in range(0,len(self._data)):
           draad += str("{0:.5f}".format(self._data[i]))+'\n'
        return draad
    
    def __add__(self,other):
        new=[]
        for i in range(0,len(self._data)):
            new.append(self._data[i]+other._data[i])
        return Vector(len(new),new)
        
    def lincomb(self,other,alpha,beta):
        new=[]
        for i in range(0,len(self._data)):
            new.append(alpha *self._data[i]+ beta *other._data[i])
        return Vector(len(new),new)
    
    def scalar(self,alpha):
        new=[]
        for i in range(0,len(self._data)):
            new.append(alpha *self._data[i])
        return Vector(len(new),new)
        
    def inner(self,other):
        new=0
        for i in range(0,len(self._data)):
            new+=self._data[i]*other._data[i]
        return new
        
    def norm(self):
        new=0
        for i in range(0,len(self._data)):
            new+=self._data[i]**2
        return new**0.5
    
    def projection(self,other):
        new=[]
        for i in range(0,len(self._data)):
            new.append(self._data[i]*self.inner(other)/self.norm())
        return Vector(len(new),new)
    
    def __len__(self):
         return len(self._data)
    
    def __sub__(self, other):
        new=[]
        for i in range(0,len(self._data)):
            new.append(self._data[i]-other._data[i])
        return Vector(len(new),new)
        
        
def GrammSchmidt(V):
    new=[]
    for i in range(len(V)):
        a=V[i].scalar(1/(V[i].norm()))
        for j in range(0,i):
            if i!=0:
                a=a - V[i].projection(new[j])
        new.append(a)
    return new