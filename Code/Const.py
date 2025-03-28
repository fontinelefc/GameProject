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
    'Enemy1': 1,
    'Enemy2': 1,

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
    'level1Bg0': 999,
    'level1Bg1': 999,
    'level1Bg2': 999,
    'level1Bg3': 999,
    'level1Bg4': 999,
    'level1Bg5': 999,
    'level1Bg6': 999,
    'level1Bg7': 999,
    'Player1': 45,
    'Player1Shot': 1,
    'Enemy1': 45,
    'Enemy2': 30,
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_LCTRL
}
