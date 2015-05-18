draaiingen = input()

dobbelsteen= ["beneden", "links", "omhoog", "omlaag", "rechts", "boven"]
def omhoog():
    temp0 = dobbelsteen[0] 
    temp2 = dobbelsteen[2] 
    temp3 = dobbelsteen[3]
    temp5 = dobbelsteen[5]
    dobbelsteen[0] = temp3
    dobbelsteen[3] = temp5
    dobbelsteen[2] = temp0
    dobbelsteen[5] = temp2

def omlaag():
    temp0 = dobbelsteen[0] 
    temp2 = dobbelsteen[2] 
    temp3 = dobbelsteen[3]
    temp5 = dobbelsteen[5]
    dobbelsteen[0] = temp2
    dobbelsteen[3] = temp0
    dobbelsteen[2] = temp5
    dobbelsteen[5] = temp3
    
def links():
    temp1 = dobbelsteen[1] 
    temp2 = dobbelsteen[2] 
    temp3 = dobbelsteen[3]
    temp4 = dobbelsteen[4]
    dobbelsteen[1] = temp3
    dobbelsteen[2] = temp1
    dobbelsteen[3] = temp4
    dobbelsteen[4] = temp2
    
def rechts():
    temp1 = dobbelsteen[1] 
    temp2 = dobbelsteen[2] 
    temp3 = dobbelsteen[3]
    temp4 = dobbelsteen[4]
    dobbelsteen[1] = temp2
    dobbelsteen[2] = temp4
    dobbelsteen[3] = temp1
    dobbelsteen[4] = temp3

for i in range(0, int(draaiingen)):
    draai = input()
    if draai == 'omhoog':
        omhoog()
    elif draai =='omlaag':
        omlaag()
    elif draai=='rechts':
        rechts()
    elif draai=='links':
        links()

for i in range(0,6):
    if dobbelsteen[i]=='boven':
        print(str(i+1))