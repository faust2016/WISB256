import math

vuurkracht = input()
zwaartekracht = input()
horAfstand = input()
alpha = 0.5*math.asin(int(horAfstand)*int(zwaartekracht)/int(vuurkracht)**2)
print("{0:.2f}".format(alpha) )