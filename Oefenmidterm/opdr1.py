regels = int(input())
for regel in range(0,regels):
    regel = str(input())
    if len(regel.split())<5:
        print(regel+ " krAh!")
    else:
        print("Crackers!")
