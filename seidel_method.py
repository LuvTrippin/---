import copy
import numpy as np


def seidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)

    converge = False
    while not converge:
        x_new = copy.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            s2 = sum(A[i][j] * x_new[j] for j in range(i))
            x_new[i] = (b[i] - s1 - s2)/A[i][i]

        converge = np.sqrt(sum((x[i] - x_new[i])**2 for i in range(n))) <= eps
        x = x_new
    return x


M1 = [[6.4, 1.3, -2.7],
      [3.8, 6.7, -1.2],
      [2.4, -4.5, 3.5]]

a = [3.8, 5.2, -0.6]
ep = 0.0005

print(seidel(M1, a, ep))

