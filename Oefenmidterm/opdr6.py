maxlevel= input()
aantal = input()
vrienden=0
level=0

for i in range(0,int(maxlevel)):
    level=level+int(aantal[i])
    if i+1>level and aantal[i+1]!='0':
        vriendenoud = vrienden
        vrienden = vrienden + (i+1- level)
        level = level+(vrienden-vriendenoud)

print(str(vrienden))