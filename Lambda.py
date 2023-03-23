# Python Lambda
# lambda arguments : expression

print("************1***********")
x = lambda a: a + 7
print(x(5))
print("************2***********")
lam = lambda c, d: c * d
print(lam(5, 7))
print("************3***********")
# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

def myLambda(n):
    return lambda f: f * n

resLambFunc = myLambda(7)
print(resLambFunc(7))
