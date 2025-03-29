# M
import pygame

ENTITY_SHOT_DELAY = {
    'Player1': 7
}

MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

ENTITY_DAMAGE = {
    'level1Bg0': 0,
    'level1Bg1': 0,
    'level1Bg2': 0,
    'level1Bg3': 0,
    'level1Bg4': 0,
    'level1Bg5': 0,
    'level1Bg6': 0,
    'level1Bg7': 0,
    'Player1': 1,
    'Player1Shot': 15,
    'Enemy1': 15,
    'Enemy2': 15,

}
ENTITY_SCORE = {
    'level1Bg0': 0,
    'level1Bg1': 0,
    'level1Bg2': 0,
    'level1Bg3': 0,
    'level1Bg4': 0,
    'level1Bg5': 0,
    'level1Bg6': 0,
    'level1Bg7': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Enemy1': 50,
    'Enemy2': 25,
}


EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 2,
    'level1Bg2': 1,
    'level1Bg3': 2,
    'level1Bg4': 1,
    'level1Bg5': 1,
    'level1Bg6': 1,
    'level1Bg7': 1,
    'Player1': 5,
    'Player1Shot': 7,
    'Enemy1': 6,
    'Enemy2': 4,
}
ENTITY_HEALTH = {
    'level1Bg0': 9999,
    'level1Bg1': 9999,
    'level1Bg2': 9999,
    'level1Bg3': 9999,
    'level1Bg4': 9999,
    'level1Bg5': 9999,
    'level1Bg6': 9999,
    'level1Bg7': 9999,
    'Player1': 800,
    'Player1Shot': 1,
    'Enemy1': 45,
    'Enemy2': 30,
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_LCTRL
}
