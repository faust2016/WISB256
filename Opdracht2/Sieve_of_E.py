def priemen(n): 
    priemlijst, zeef = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if zeef[p]:
           priemlijst.append(p)
           for i in range(p**2, n + 1, p):
               zeef[i] = False
    print(priemlijst)

priemen(9000)