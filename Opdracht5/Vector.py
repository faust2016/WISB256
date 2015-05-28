class Vector:
   # __slots__ = ('_dim' , '_val')
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
        return new
        