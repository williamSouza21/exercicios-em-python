def derivada(x, y):
    return -x/y


def runge_kutta(x, y, h, a):
    Yn = tl = 0
    for item in range(a):
        k1 = derivada(x, y)
        k2 = derivada(x + h/2, y + (h/2)*k1)
        k3 = derivada(x+h/2, y + (h/2)*k2)
        k4 = derivada(x+h, y + h*k3)
        k = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        Yn = y + k*h
        y = tl
        y = Yn
        x = x + h
    return Yn


def e(x, y, h, a):
    yn = 0
    for item in range(a):
        yn = y + (h/2) * derivada(x, y) + \
            derivada(x+h, y+h*derivada(x, y)) * (h/2)
        y = yn
        x = x + h
    return yn


h = 8
x_0 = 1
n = 1
y_0 = 10
h2 = 8
while(abs(runge_kutta(x_0, y_0, h, n-1) - runge_kutta(x_0, y_0, h2, n)) > 0.00001):
    n = n + 1
    h = 8/(n-1)
    h2 = 8/(n)

n_0 = n
Ya = runge_kutta(x_0, y_0, h, (n-1))
x_0 = 1
y_0 = 10
h = 8
n = 0

while (abs(Ya - e(x_0, y_0, h, n)) > 0.001):
    n = n + 1
    h = 8/n

m = n
print(n_0*m)
