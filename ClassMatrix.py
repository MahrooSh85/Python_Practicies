import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def inverse(self):
        return np.linalg.inv(self.matrix)

    def determinant(self):
        return np.linalg.det(self.matrix)


matrix1 = Matrix(np.array([[1, 1], [5, 2]]))
print(matrix1.inverse())
print(matrix1.determinant())