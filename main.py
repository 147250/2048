from PyQt5 import QtWidgets, QtCore, QtMultimedia
from widget import MainWindow
from matrix import Matrix
from pathlib import Path
import sys
import random
import constant as c


class GameManager(QtCore.QObject):

    def __init__(self):
        super(GameManager, self).__init__()

        self.matrix = None
        self.grid = None
        self.player_name = None

        # draw main window
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow()
        self.window.resize(350, 350)
        self.window.setWindowTitle('2048')
        self.window.start_game_signal.connect(self.start_game)
        self.window.show()
        self.window.center_desktop()

        # connect sound tool bar
        self.window.mute_btn.clicked.connect(self.mute_sound)
        self.window.volume_slider.valueChanged.connect(self.change_volume)

        # sound
        self.media_player = QtMultimedia.QMediaPlayer(flags=QtMultimedia.QMediaPlayer.LowLatency)

        path = Path('sounds', 'complete.wav').absolute().__str__()
        sound_file = QtCore.QUrl.fromLocalFile(path)
        self.sound_score = QtMultimedia.QMediaContent(sound_file)

        path = Path('sounds', 'move.wav').absolute().__str__()
        sound_file = QtCore.QUrl.fromLocalFile(path)
        self.sound_move = QtMultimedia.QMediaContent(sound_file)

        path = Path('sounds', 'no_possible.wav').absolute().__str__()
        sound_file = QtCore.QUrl.fromLocalFile(path)
        self.sound_no_possible = QtMultimedia.QMediaContent(sound_file)

        path = Path('sounds', 'start.wav').absolute().__str__()
        sound_file = QtCore.QUrl.fromLocalFile(path)
        self.sound_start = QtMultimedia.QMediaContent(sound_file)

        # start application
        sys.exit(self.app.exec())

    def start_game(self, text):
        # draw game grid
        self.player_name = text
        self.play_sound(self.sound_start)
        self.matrix = Matrix(c.ROW, c.COLUMN)
        self.grid = self.window.centralWidget()
        self.grid.change_labels_text(self.matrix.field)
        self.grid.key_signal.connect(self.key_press)

    def game_over(self):
        self.players_lst()
        self.window.game_over_message()

    def players_lst(self):
        pos = (self.player_name, str(self.matrix.score))
        c.bst_players_lst.append(pos)
        c.bst_players_lst.sort(key=lambda x: int(x[1]), reverse=True)
        c.bst_players_lst.pop()
        c.settings.setValue('best_players', c.bst_players_lst)
        c.settings.sync()

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
                    self.play_sound(self.sound_score)
                else:
                    self.play_sound(self.sound_move)
                self.matrix.field = matrix
                self.grid.change_labels_text(self.matrix.field)
                self.grid.score_label.setText(f'Score: {self.matrix.score}')
                self.grid.progress_bar_thread.change_new_value(self.matrix.score)
                self.grid.progress_bar_thread.start()
        else:
            self.play_sound(self.sound_no_possible)

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

    def play_sound(self, sound):
        self.media_player.setMedia(sound)
        self.media_player.play()

    def mute_sound(self):
        state = not self.media_player.isMuted()
        self.media_player.setMuted(state)
        self.window.change_mute_icon(state)

    def change_volume(self, value):
        self.media_player.setVolume(value)
        self.media_player.setMuted(False)
        self.window.change_mute_icon(False)


if __name__ == '__main__':
    GameManager()
