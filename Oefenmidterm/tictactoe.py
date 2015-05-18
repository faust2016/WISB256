rij1= input()
rij2=input()
rij3=input()

if rij1=='111' or rij2=='111' or rij3=='111':
    print('Player 1 wins')
elif rij1=='222' or rij2=='222' or rij3=='222':
    print('Player 2 wins')
elif rij1[0]==rij2[1]==rij3[2] and rij2[1]!= '0':
    print('Player '+rij1[0]+' wins')
elif rij1[2]==rij2[1]==rij3[0] and rij1[2]!= '0':
    print('Player '+rij1[2]+' wins')
elif rij1[0]==rij2[0]==rij3[0] and rij1[0]!= '0':
            print('Player '+rij1[0]+' wins')
elif rij1[1]==rij2[1]==rij3[1] and rij1[1]!= '0':
            print('Player '+rij1[1]+' wins')
elif rij1[2]==rij2[2]==rij3[2] and rij1[2]!= '0':
            print('Player '+rij1[2]+' wins')
else:
    print('No winner')

# for i in range(0,3):
 #       if rij1[i]==rij2[i]==rij3[i] and rij1[i]!= '0':
  #          print('Player '+rij1[i]+' wins')
   #         break