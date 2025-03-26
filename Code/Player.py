import pygame

from Code.Const import ENTITY_SPEED
from Code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_DOWN] and self.rect.bottom < 324:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_RIGHT] and self.rect.right < 576:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass
