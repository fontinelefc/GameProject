#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))
        self.timeout = 20000

    def run(self, ):
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color=(255, 255, 255), text_pos=(60, 5))
            self.level_text(text_size=14, text=f'fps {clock.get_fps() :.0f}', text_color=(255, 255, 255), text_pos=(20, 300))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=(255, 255, 255), text_pos=(40, 310))
            pygame.display.flip()
        pass
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewrite", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)