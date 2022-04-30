class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda row: '   '.join(map(str, row)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda row_1, row_2: map(lambda x, y: x + y, row_1, row_2), self.matrix, other.matrix))


matrix_1 = Matrix([[9, -2, 13], [5, 21, 1], [65, 4, -34]])
matrix_2 = Matrix([[88, 2, 7], [23, 7, -6], [4, 54, 3]])
print(matrix_1, end='-первая матрица.\n\n')
print(matrix_2, end='-вторая матрица.\n\n')
sum_of_matrices = matrix_1 + matrix_2
print(sum_of_matrices, end='-результат сложения матриц.')
