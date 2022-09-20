import numpy as np
import time


class Matrix:
    def __init__(self, n, m: int):
        self.matrix = [[0] * m for _ in range(n)]

    def assign_values(self, mat):
        self.matrix = mat

    def triangular_matrix(self):
        res = self.matrix
        for i in range(len(res)):
            for j in range(i + 1, len(res)):
                ratio = res[i][i] / res[j][i]
                for k in range(i, len(res[0])):
                    res[j][k] -= res[i][k] / ratio
        return res

    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j], end=" ")
            print()

    def det_matrix(self):
        triangular_matrix = self.triangular_matrix()
        det = 1
        for i in range(len(triangular_matrix)):
            det *= triangular_matrix[i][i]
        return det


matrix = Matrix(4, 4)
matrix.assign_values([[2.8, 2.1, -1.3, 0.3],
                      [-1.4, 4.5, -7.7, 1.3],
                      [0.6, 2.1, -5.8, 2.4],
                      [3.5, -6.5, 3.2, -7.9]])
start1 = time.time()
print(matrix.det_matrix())
end1 = time.time()
print(end1 - start1)

mas = np.array([[2.8, 2.1, -1.3, 0.3],
                [-1.4, 4.5, -7.7, 1.3],
                [0.6, 2.1, -5.8, 2.4],
                [3.5, -6.5, 3.2, -7.9]])

start2 = time.time()
print(np.linalg.det(mas))
end2 = time.time()
print(end2 - start2)
