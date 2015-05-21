def findRoot(f,a,b,epsilon):
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