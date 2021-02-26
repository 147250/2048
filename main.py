from PyQt5 import QtWidgets, QtCore, QtMultimedia
from widget import MainWindow
from matrix import Matrix
from constant import *
import sys
import random
from pathlib import Path


class GameManager(QtCore.QObject):

    def __init__(self):
        super(GameManager, self).__init__()

        self.matrix = None
        self.grid = None

        # draw main window
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow()
        self.window.resize(350, 350)
        self.window.setWindowTitle('2048')
        self.window.start_game_signal.connect(self.start_game)
        self.window.show()
        self.window.center_desktop()

        # sounds
        self.complete_sound = QtMultimedia.QSoundEffect()
        file = Path('sounds/complete.wav').__str__()
        sound_file = QtCore.QUrl.fromLocalFile(file)
        self.complete_sound.setSource(sound_file)

        self.move_sound = QtMultimedia.QSoundEffect()
        file = Path('sounds/move.wav').__str__()
        sound_file = QtCore.QUrl.fromLocalFile(file)
        self.move_sound.setSource(sound_file)

        self.no_possible_sound = QtMultimedia.QSoundEffect()
        file = Path('sounds/no_possible.wav').__str__()
        sound_file = QtCore.QUrl.fromLocalFile(file)
        self.no_possible_sound.setSource(sound_file)

        self.start_sound = QtMultimedia.QSoundEffect()
        file = Path('sounds/start.wav').__str__()
        sound_file = QtCore.QUrl.fromLocalFile(file)
        self.start_sound.setSource(sound_file)

        sys.exit(self.app.exec())

    def start_game(self):
        # draw game grid
        self.start_sound.play()
        self.matrix = Matrix(ROW, COLUMN)
        self.grid = self.window.centralWidget()
        self.grid.change_labels_text(self.matrix.field)
        self.grid.key_signal.connect(self.key_press)

    def game_over(self):
        self.window.game_over_message()

    @QtCore.pyqtSlot(str)
    def key_press(self, key_signal):
        cur_score = self.matrix.score

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

            if not empty_cells and self.no_moves(matrix):
                self.game_over()
            else:
                if cur_score < self.matrix.score:
                    self.complete_sound.play()
                else:
                    self.move_sound.play()
                self.matrix.field = matrix
                self.grid.change_labels_text(self.matrix.field)
                self.grid.score_label.setText(f'Score: {self.matrix.score}')
                self.grid.progress_bar_thread.change_new_value(self.matrix.score)
                self.grid.progress_bar_thread.start()
        else:
            self.no_possible_sound.play()

    def no_moves(self, matrix: list) -> bool:
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
