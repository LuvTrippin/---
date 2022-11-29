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


def calc_c(new_x: list, xi: list) -> float:
    c = 0
    for k in range(N):
        c = sum([calc_omega(i, xi)/(i - xi[k])/calc_d_omega(xi[k], xi) for i in new_x])
    return c


def calc_integral(new_x: list, xi: list) -> float:
    I = sum([calc_c(new_x, xi) * f[i] for i in range(N)])


f = []
seg = [0.2, 1]
a, b = 0.2, 1
step = 0.2
N = 5
h = (b - a)/N
x = [a+i*h for i in range(N + 1)]
x_new = [i - 0.5*h for i in x]
D_omg = [i - j for i in x for j in x if j != i]
C = sum([])
