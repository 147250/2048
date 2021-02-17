from PyQt5 import QtWidgets, QtCore
from widget import MainWindow
from matrix import Matrix
from constant import ROW, COLUMN
import sys
import random


class GameManager(QtCore.QObject):

    def __init__(self):
        super(GameManager, self).__init__()

        self.matrix = None
        self.grid = None

        # draw main window
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow()
        self.window.resize(250, 250)
        self.window.setWindowTitle('2048')
        self.window.start_game_signal.connect(self.start_game)
        self.window.show()
        self.window.center_desktop()
        sys.exit(self.app.exec())

    def start_game(self):
        # draw game grid
        self.matrix = Matrix(ROW, COLUMN)
        self.grid = self.window.widget
        self.grid.change_labels_text(self.matrix.field)
        self.grid.key_signal.connect(self.key_press)

    def game_over(self):
        self.window.game_over_message()

    @QtCore.pyqtSlot(str)
    def key_press(self, key_signal):
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
                self.game_over()
            else:
                self.matrix.field = matrix
                self.grid.change_labels_text(self.matrix.field)
                self.grid.score_label.setText(f'Score: {self.matrix.score}')

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
    GameManager()
