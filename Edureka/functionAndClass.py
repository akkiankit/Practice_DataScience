print("class")
class person:
    name = "elma"
    age = 34
    country= "phillipines"

x = getattr(person,'age')
print("age of : " +  str(x))

print("length of name inside class : " + str(len(getattr(person,"name"))))

def getLen(n):
    return len(n)

user = ('John', 'keth','eba', 'emila')
c = map(getLen, user)
print(c)

# lambda Function
lambdafunction = lambda a : a + 10
print(lambdafunction(10))
 
