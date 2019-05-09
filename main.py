import math

def func(x):
    return x ** x + math.sqrt(x)

print("Here's the result of f(x): " + str(func(float(input("Type in x:")))))