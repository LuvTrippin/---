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


def calc_c(new_x: list, xi: list) -> list:
    c = list()
    om = [calc_omega(i, xi) for i in new_x]
    for k in range(N + 1):
        d_om = calc_d_omega(xi[k], xi)
        tmp = [i - xi[k] for i in new_x]
        c.append(sum([i/(t*d_om)*h for i in om for t in tmp]))
    return c


def calc_integral(new_x: list, xi: list) -> float:
    c = calc_c(new_x, xi)
    I = sum([c[i] * f[i] for i in range(N + 1)])
    return I


seg = [1, 2]
a, b = 1, 2
step = 0.2
N = 5
h = (b - a)/N
x = [a+i*h for i in range(N + 1)]
x_new = [i - 0.5*h for i in x]
f = [i/(1 + i**2)**2 for i in x]
calc_integral(x_new, x)
