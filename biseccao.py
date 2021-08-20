import math


def f(x):
    return math.exp(-x**2) - math.cos(x)


# Aplicando o método da bissecção:
a = 1
b = 2
L = 10**(-4)
x0 = (a + b)/2

while(True):
    if(abs(f(x0)) <= L):
        print(x0)
        break

    else:
        if((f(a) * f(x0)) < 0):
            b = x0
            x0 = (a + b)/2

        elif((f(b) * f(x0)) < 0):
            a = x0
            x0 = (a + b)/2

