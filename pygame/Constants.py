import os

class Paths:
    ANIMATIONS_PATH = os.path.join('data', 'animations')
    HERO_PATH = os.path.join('data', 'hero')
    BACKGROUNDS_PATH = os.path.join('data', 'backgrounds')
    LOGO_PATH = os.path.join('data', 'misc', 'logo.png')
    OK_BTN_PATH = os.path.join('data', 'buttons', 'btn_ok.png')
    BTNS_PATH = os.path.join('data', 'buttons', 'buttons.png')
    WINDOW_PATH = os.path.join('data', 'scenes', 'menusystem', 'window.png')
    ITEM_PATH = os.path.join('data', 'items')

    EQUIPMENT_SYSTEM = os.path.join('data', 'scenes', 'equipmentsystem')

    DB_FILES = tuple(os.path.join('data', 'db', i)
        for i in ['messages.sql', 'names.sql', 'game.sql',
                  'map.sql', 'atlas.sql'])

class Game:
    WORLD_ID = 1

class HERO_START:
    STARTING_ITEMS = {'a':10, 'b':20}