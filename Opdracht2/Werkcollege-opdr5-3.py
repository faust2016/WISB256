def check_fermat(a,b,c,n):
    if a**n+b**n == c**n and n>2:
        print("Holy smokes, Fermat was wrong")
    else:
        print("No, that doesn't work.")
        
nummers = input("What numbers?") 
check_fermat(int(nummers[0]),int(nummers[1]),int(nummers[2]),int(nummers[3]))