import module1 as mod1
from module1 import sub
import random

print(sub(6,7))

addval = mod1.add(1,3)
print("addition of two number: " + str(addval))

subVal = mod1.sub(6,9)
print("subtraction of two number : " + str(subVal))

mulVal = mod1.mul(8,5)
print("Multiplication of two number : " + str(mulVal))

# print("factorial of a number " + str(mod1.fact(20))) 

print("factorial of a number " + str(mod1.factorial(6))) 

print(random.randrange(0,50))