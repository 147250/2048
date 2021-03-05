from PyQt5 import QtCore
from pathlib import Path

ROW = 4
COLUMN = 4
CHANCE_GET_FOUR = 5
WIDTH_CELL = 40

# CSS
# border
BORDER = ' border-radius: 5px;'

# background colors
BG_GREY_1 = 'background-color: rgb(211, 215, 207);'
BG_GREY_2 = 'background-color: rgb(233, 185, 110);'
BG_ORANGE_1 = 'background-color: rgb(245, 121, 0);'
BG_ORANGE_2 = 'background-color: rgb(252, 175, 62);'
BG_RED_1 = 'background-color: rgb(239, 41, 41);'
BG_RED_2 = 'background-color: rgb(239, 41, 41);'
BG_YELLOW_1 = 'background-color: #edcf72;'
BG_YELLOW_2 = 'background-color: #edc850;'
BG_BLACK = 'background-color: rgb(46, 52, 54);'

# text
FONT_MAX = 'font: 34pt;'
FONT_MIDDLE = 'font: 28pt;'
FONT_MIN = 'font: 24pt;'


TEXT_BLACK = 'color: rgb(46, 52, 54);'
TEXT_WHITE = 'color: rgb(238, 238, 236);'

DICT_COLOR = {
    0: f'{BG_GREY_1}{FONT_MAX}{TEXT_BLACK}',
    2: f'{BG_GREY_1}{FONT_MAX}{TEXT_BLACK}',
    4: f'{BG_GREY_2}{FONT_MAX}{TEXT_BLACK}',
    8: f'{BG_ORANGE_1}{FONT_MAX}{TEXT_WHITE}',
    16: f'{BG_ORANGE_2}{FONT_MAX}{TEXT_WHITE}',
    32: f'{BG_RED_1}{FONT_MAX}{TEXT_WHITE}',
    64: f'{BG_RED_2}{FONT_MAX}{TEXT_WHITE}',
    128: f'{BG_YELLOW_1}{FONT_MIDDLE}{TEXT_WHITE}',
    256: f'{BG_YELLOW_1}{FONT_MIDDLE}{TEXT_WHITE}',
    512: f'{BG_YELLOW_1}{FONT_MIDDLE}{TEXT_WHITE}',
    1024: f'{BG_YELLOW_2}{FONT_MIN}{TEXT_WHITE}',
    2048: f'{BG_YELLOW_2}{FONT_MIN}{TEXT_WHITE}',
    float('INF'): f'{BG_BLACK}{FONT_MIN}{TEXT_WHITE}'
}

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
