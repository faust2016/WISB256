import sys

boodschap = sys.argv[1]
key = sys.argv[2]
keyz=len(boodschap)//len(key)*key
def letter(b,k):
    return chr((ord(b)-97 - (ord(k)-97))%26+97)
lijst= []
for i in range(0,len(boodschap)):
    l=letter(boodschap[i],key[i])
    lijst.append(l)
print("".join(lijst))