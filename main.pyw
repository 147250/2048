from PyQt5 import QtWidgets
from widget import GameGrid
from matrix import Matrix
from constant import ROW, COLUMN
import sys
import random


class GameManager:

    def __init__(self, row, column):

        self.matrix = Matrix(row, column)

        # draw window
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = GameGrid(row, column)
        self.window.setWindowTitle('2048')
        self.window.change_labels_text(self.matrix.field)
        self.window.key_signal.connect(self.key_press)
        self.window.show()
        desktop_center = QtWidgets.QApplication.desktop().availableGeometry().center()
        rect = self.window.frameGeometry()
        rect.moveCenter(desktop_center)
        self.window.move(rect.topLeft())
        sys.exit(self.app.exec())

    def key_press(self, key_signal: str) -> None:
        if key_signal == 'left':
            matrix = self.matrix.get_matrix_left(self.matrix.field)
        elif key_signal == 'right':
            matrix = self.matrix.get_matrix_right(self.matrix.field)
        elif key_signal == 'up':
            matrix = self.matrix.get_matrix_up(self.matrix.field)
        elif key_signal == 'down':
            matrix = self.matrix.get_matrix_down(self.matrix.field)
        else:
            return

        if matrix != self.matrix.field:
            empty_list = self.matrix.get_empty_cells(matrix)
            i, j = random.choice(empty_list)
            matrix[i][j] = self.matrix.get_num()
            empty_cells = len(empty_list) - 1

            if not empty_cells and self.end_game(matrix):
                raise StopIteration('Конец игры')
            else:
                self.matrix.field = matrix
                self.window.change_labels_text(self.matrix.field)
                self.window.score_label.setText(f'Score: {self.matrix.score}')

    def end_game(self, matrix: list) -> bool:
        if self.matrix.get_matrix_left(matrix) != matrix:
            return False
        elif self.matrix.get_matrix_right(matrix) != matrix:
            return False
        elif self.matrix.get_matrix_up(matrix) != matrix:
            return False
        elif self.matrix.get_matrix_down(matrix) != matrix:
            return False
        else:
            return True


if __name__ == '__main__':
    GameManager(ROW, COLUMN)
