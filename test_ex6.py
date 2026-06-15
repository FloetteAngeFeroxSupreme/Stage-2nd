from ex6 import calculatrice
from random import *
a=randint(0,100)
b=randint(0,100)
l=["+","-","*","/"]
c=choice(l)
if calculatrice(a, b, c) == eval(str(a)+c+str(b)):
    print("Test passed")
else:
    print("Test failed")