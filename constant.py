from PyQt5 import QtCore
from pathlib import Path

ROW = 4
COLUMN = 4
CHANCE_GET_FOUR = 5
WIDTH_CELL = 40

# colors
GREY = 'background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0703518 rgba(172, 173, 172, 255), stop:0.884422 rgba(185, 187, 192, 255));'

# BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
#                          16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
#                          128: "#edcf72", 256: "#edcc61", 512: "#edc850",
#                          1024: "#edc53f", 2048: "#edc22e",
#
#                          4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
#                          32768: "#f59563", 65536: "#f67c5f", }
#
# CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
#                    32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
#                    256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
#                    2048: "#f9f6f2",
#
#                    4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
#                    32768: "#776e65", 65536: "#f9f6f2", }

DICT_COLOR = {
    0: 'black-white',
    2: 'background-color: rgb(211, 215, 207); font: 24pt;',
    4: 'lit grey',
    8: 'orange-white',
    16: 'orange-white',
    32: 'orange-white',
    64: 'red-white',
    128: 'yellow-white',
    256: 'yellow-white',
    512: 'yellow-white',
    1024: 'yellow-white',
}


BEST_LST = [
    ('game master', str(2 ** 18)),
    ('mind machine', str(2 ** 17)),
    ('king of nerds', str(2 ** 16)),
    ('nerd', str(2 ** 15)),
    ('your babushka', str(2 ** 14)),
    ('noob master', str(2 ** 13)),
    ('noob', str(2 ** 12)),
    ('random click', str(2 ** 11))
]

set_file = Path(Path.cwd(), 'set.ini')
settings = QtCore.QSettings(set_file.__str__(), QtCore.QSettings.IniFormat)
bst_players_lst = settings.value('best_players', BEST_LST)
max_score = int(bst_players_lst[0][1])
