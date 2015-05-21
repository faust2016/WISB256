def findRoot(f,a,b,epsilon):
    if f(a)*f(b)>=0:
        return None
    c = 0.5*(a+b)
    if f(a)*f(c)<0:
        if abs(c-a)<epsilon:
            return c
        else:
            return findRoot(f,a,c,epsilon)
    elif f(b)*f(c)<0:
        if abs(c-b)<epsilon:
            return c
        else:
            return findRoot(f,c,b,epsilon)
    else: return c
    
def findAllRoots(f,a,b,epsilon):
    output=[]
    for i in range(0,10):
        temp=findRoot(f,a+(i/5)*(b-a),(b-(4-i)/5*(b-a)),epsilon)
        if temp!= None:
            output.append(temp)
        print(str(a+(i/10)*(b-a))+' , '+ str(b-(9-i)/10*(b-a)))
    return output
    
