rpn = input()
ding = rpn.split()
if ding[2]== '+':
    out = int(ding[0])+int(ding[1])
    print(str(out)+".000")
if ding[2]== '-':
    out = int(ding[0])-int(ding[1])
    print(str(out)+".000")
if ding[2]== '*':
    out = int(ding[0])*int(ding[1])
    print(str(out)+".000")
if ding[2]== '/':
    out = int(ding[0])/int(ding[1])
    print("{0:.3f}".format(out))