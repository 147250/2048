import random
import constant as c


class Matrix:

    def __init__(self, row, column):
        self.field = [[0] * column for _ in range(row)]
        i, j = random.randint(0, row - 1), random.randint(0, column - 1)
        self.field[i][j] = 2
        self.score = 0
        self.row = row
        self.column = column

    def add_numbers(self, matrix: list) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - 1):
                if matrix[i][j] == matrix[i][j + 1]:
                    matrix[i][j] *= 2
                    matrix[i][j + 1] = 0
                    self.score += matrix[i][j]

    def get_matrix_left(self, matrix: list) -> list:
        matrix = [[elem for elem in row] for row in matrix]
        self.compress(matrix)
        self.add_numbers(matrix)
        self.compress(matrix)
        return matrix

    def get_matrix_right(self, matrix: list) -> list:
        matrix = [[elem for elem in row] for row in matrix]
        self.reverse_row_matrix(matrix)
        matrix = self.get_matrix_left(matrix)
        self.reverse_row_matrix(matrix)
        return matrix

    def get_matrix_up(self, matrix: list) -> list:
        matrix = self.transpose_matrix(matrix)
        self.reverse_row_matrix(matrix)
        matrix = self.get_matrix_right(matrix)
        self.reverse_row_matrix(matrix)
        matrix = self.transpose_matrix(matrix)
        return matrix

    def get_matrix_down(self, matrix: list) -> list:
        matrix = self.transpose_matrix(matrix)
        self.reverse_row_matrix(matrix)
        matrix = self.get_matrix_left(matrix)
        self.reverse_row_matrix(matrix)
        matrix = self.transpose_matrix(matrix)
        return matrix

    @staticmethod
    def get_num():
        num = random.randint(1, 100)
        if num > c.CHANCE_GET_FOUR:
            return 2
        else:
            return 4

    @staticmethod
    def reverse_row_matrix(matrix: list) -> None:
        for elem in matrix:
            elem.reverse()

    @staticmethod
    def transpose_matrix(matrix: list) -> list:
        return [list(elem) for elem in zip(*matrix)]

    @staticmethod
    def compress(matrix: list) -> None:
        for elem in matrix:
            elem.sort(key=bool, reverse=True)

    @staticmethod
    def get_empty_cells(matrix: list) -> list:
        empty_cells_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    empty_cells_list.append((i, j))
        return empty_cells_list
