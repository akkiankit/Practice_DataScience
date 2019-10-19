def add(a,b):
    return a+b

def sub(a,b):
    if a > b:
        return a-b
    else:
        return b-a


def mul(a,b):
    return a*b

def div(a,b):
    return a/b  

# def fact(num):
#     mul = 1 
#     for i in range(1,num + 1):
#         mul = mul * i
#     return mul     

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)
