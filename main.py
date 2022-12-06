import math


def calc_omega(x: float, X: list) -> float:
    omega = 1
    for i in X:
        omega *= (x-i)
    return omega


def calc_d_omega(x: float, X: list) -> float:
    d_omega = 1
    for i in X:
        if i != x:
            d_omega *= (x-i)
    return d_omega


def calc_c(new_X: list, X: list) -> list:
    c = list()
    for k in X:
        c.append(sum([calc_omega(i, X) / ((i - k) * calc_d_omega(k, X)) for i in new_X])*h)
    return c


def calc_integral(new_x: list, xi: list) -> float:
    c = calc_c(new_x, xi)
    I = sum([c[i] * f[i] for i in range(5)])
    return I


a, b = 0.2, 1
step = 0.2
N = 10000
h = (b - a)/N
x = [0.2, 0.4, 0.6, 0.8, 1]
xi = [a+i*h for i in range(N+1)]
x_new = [i - 0.5*h for i in xi]
f = [1/i for i in x]
print(calc_integral(x_new, x))
print(abs(calc_integral(x_new, x) - (-math.log(0.2))))
