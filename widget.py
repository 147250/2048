from PyQt5 import QtWidgets, QtCore, QtGui
from constant import *


class StartWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.label = QtWidgets.QLabel('2048')
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.enter_name = QtWidgets.QLineEdit('Player')
        self.enter_name.setMaxLength(8)
        self.enter_name.setPlaceholderText('Enter your name')
        self.enter_name.textChanged.connect(self.enable_start_button)

        self.start_btn = QtWidgets.QPushButton('Start')

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.label)
        self.vbox.addSpacing(50)
        self.vbox.addWidget(self.enter_name)
        self.vbox.addWidget(self.start_btn)
        self.vbox.addStretch(1)

        self.setLayout(self.vbox)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

    def enable_start_button(self, text):
        status = True
        if not len(text):
            status = False
        self.start_btn.setEnabled(status)


class Cell(QtWidgets.QLabel):

    def __init__(self, text: str, width: int = 40, parent: (QtWidgets, None) = None):
        super().__init__(text, parent)
        self.setMinimumSize(width, width)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Panel)


class ProgressBarThread(QtCore.QThread):
    progress_signal = QtCore.pyqtSignal(int)

    def __init__(self, maximum_score):
        super(ProgressBarThread, self).__init__()
        self.new_value = 0
        self.old_value = 0
        self.max_value = maximum_score

    def run(self):
        if self.old_value < self.max_value:
            start = self.old_value
            stop = self.new_value
            step = 2

            for i in range(start, stop + step, step):
                self.old_value = i
                self.progress_signal.emit(i)
                self.msleep(20)

    def change_new_value(self, value):
        self.new_value = value


class GameGrid(QtWidgets.QWidget):
    key_signal = QtCore.pyqtSignal(str)

    def __init__(self, row: int, column: int, parent: (QtWidgets, None) = None):
        super().__init__(parent)
        self.row = row
        self.column = column
        self.score_label = QtWidgets.QLabel('Score: ')
        self.place_label = QtWidgets.QLabel('1st Place')
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, MAX_SCORE)
        self.place_label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lst = [[Cell('', WIDTH_CELL) for _ in range(self.column)] for _ in range(self.row)]
        self.progress_bar_thread = ProgressBarThread(MAX_SCORE)
        self.progress_bar_thread.progress_signal.connect(self.progress_bar.setValue)

        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)
        for i in range(self.row):
            for j in range(self.column):
                self.grid.addWidget(self.label_lst[i][j], i, j)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.score_label)
        self.vbox.addWidget(self.place_label)
        self.vbox.addWidget(self.progress_bar)
        self.vbox.addLayout(self.grid)

        self.setLayout(self.vbox)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

    def change_progress_bar(self):
        pass

    def change_labels_text(self, matrix: list) -> None:
        for i in range(self.row):
            for j in range(self.column):
                num = matrix[i][j]
                num = str(num) if num else ''
                self.label_lst[i][j].setText(num)

    def keyPressEvent(self, evnt: QtGui.QKeyEvent) -> None:
        key = evnt.key()
        key_text = ''

        if key == QtCore.Qt.Key_Left:
            key_text = 'left'
        elif key == QtCore.Qt.Key_Right:
            key_text = 'right'
        elif key == QtCore.Qt.Key_Up:
            key_text = 'up'
        elif key == QtCore.Qt.Key_Down:
            key_text = 'down'

        if key_text:
            self.key_signal.emit(key_text)
            evnt.accept()
        else:
            evnt.ignore()
            QtWidgets.QWidget.keyPressEvent(self, evnt)


class MainWindow(QtWidgets.QMainWindow):
    start_game_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget = None
        self.init_start_menu()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

    def init_start_menu(self):
        self.widget = StartWindow()
        self.widget.start_btn.clicked.connect(self.start_game)
        self.setCentralWidget(self.widget)

    def start_game(self):
        self.widget = GameGrid(ROW, COLUMN)
        self.setCentralWidget(self.widget)
        self.start_game_signal.emit()

    def game_over_message(self):
        score = self.widget.score_label.text()

        message = QtWidgets.QMessageBox(self.widget)
        message.setIcon(message.NoIcon)
        message.setText(f'Game Over\n\nYour score {score}')
        message.addButton(message.Ok)
        message.exec()
        self.init_start_menu()

    def keyPressEvent(self, evnt: QtGui.QKeyEvent) -> None:
        evnt.ignore()
        self.widget.keyPressEvent(evnt)

    # TODO: uncomment code
    # def closeEvent(self, evnt: QtGui.QCloseEvent) -> None:
    #     msg_box = QtWidgets.QMessageBox(self)
    #     msg_box.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
    #     msg_box.setInformativeText('Close Application')
    #     msg_box.setIcon(QtWidgets.QMessageBox.Question)
    #     close_btn = msg_box.addButton('Yes', QtWidgets.QMessageBox.YesRole)
    #     abort_btn = msg_box.addButton('No', QtWidgets.QMessageBox.NoRole)
    #     msg_box.setDefaultButton(close_btn)
    #     msg_box.exec()
    #
    #     if msg_box.clickedButton() == close_btn:
    #         evnt.accept()
    #     elif msg_box.clickedButton() == abort_btn:
    #         evnt.ignore()

    def center_desktop(self):
        pos = QtWidgets.QApplication.desktop().availableGeometry().center()
        self.move(pos - QtCore.QPoint(self.width() // 2, self.height() // 2))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
