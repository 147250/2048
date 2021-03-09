from PyQt5 import QtCore
from pathlib import Path

# constants
ROW = 4
COLUMN = 4
CHANCE_GET_FOUR = 5
WIDTH_CELL = 40

# settings
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
