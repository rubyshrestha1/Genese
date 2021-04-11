##WAP to change a string input by user into uppercase using parameterized decorator

def decorator(function):
    def toUpper(myString):
        func=function(myString)
        return func.upper()
    return toUpper
        

@decorator
def decorator_sample(myString):
    return myString

myString="abc"
print(decorator_sample(myString))
#decorated = decorator(decorator_sample)
#print(decorated(myString))
