boodschap = input()
key = input()
keyz= ((len(boodschap)//len(key))+1)*key

def letter(b,k):
 return chr((ord(b)-97 - (ord(k)-97))%26+97)
lijst= []
for i in range(0,len(boodschap)):
    l=letter(boodschap[i],keyz[i])
    lijst.append(l)
print("".join(lijst))