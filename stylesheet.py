from pathlib import Path
start_window_img = Path(Path.cwd(), 'pictures', 'start.jpg').__str__()
start_btn_img = Path(Path.cwd(), 'pictures', 'start_btn.png').__str__()

stylesheet = f"""
QMainWindow {{
    border-image: url({start_window_img});
}}

#start_btn {{
    border-image: url({start_btn_img});
    border-radius: 50px;
}}

QLabel {{
    font-size: 18pt;
    color: white;
}}


QMessageBox QLabel{{
    color: black;
}}

QDialog {{
    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #cfecd0, stop: 1 limegreen);
}}

Cell {{
    background-color: white;
    border-radius: 10px;
    border: 5px solid green;
}}
"""

# background colors
WHITE = 'background-color: white;'
BG_GREY = 'background-color: #cccccc;'
BG_BROWN = 'background-color: rgb(233, 185, 110);'
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
FONT_MIN = 'font: 22pt;'
FONT_SMALLEST = 'font: 16pt;'

TEXT_BLACK = 'color: rgb(46, 52, 54);'
TEXT_WHITE = 'color: rgb(238, 238, 236);'

DICT_COLOR = {
    0: f'{WHITE}{FONT_MAX}{TEXT_BLACK}',
    2: f'{BG_GREY}{FONT_MAX}{TEXT_BLACK}',
    4: f'{BG_BROWN}{FONT_MAX}{TEXT_BLACK}',
    8: f'{BG_ORANGE_1}{FONT_MAX}{TEXT_WHITE}',
    16: f'{BG_ORANGE_2}{FONT_MAX}{TEXT_WHITE}',
    32: f'{BG_RED_1}{FONT_MAX}{TEXT_WHITE}',
    64: f'{BG_RED_2}{FONT_MAX}{TEXT_WHITE}',
    128: f'{BG_YELLOW_1}{FONT_MIDDLE}{TEXT_WHITE}',
    256: f'{BG_YELLOW_1}{FONT_MIDDLE}{TEXT_WHITE}',
    512: f'{BG_YELLOW_1}{FONT_MIDDLE}{TEXT_WHITE}',
    1024: f'{BG_YELLOW_2}{FONT_MIN}{TEXT_WHITE}',
    2048: f'{BG_YELLOW_2}{FONT_MIN}{TEXT_WHITE}',
    4096: f'{BG_YELLOW_2}{FONT_MIN}{TEXT_WHITE}',
    float('INF'): f'{BG_BLACK}{FONT_SMALLEST}{TEXT_WHITE}'
}
