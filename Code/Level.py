#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from random import choice

import pygame.display
from dulwich.porcelain import remove
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import EVENT_ENEMY
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.EntityMediator import EntityMediator
from Code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 25000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        pygame.time.set_timer(EVENT_ENEMY, 1000)

    def run(self, ):
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(text_size=14, text=f'Health: {ent.health} | Score: {ent.score}', text_color=(10, 32, 66), text_pos=(60, 20))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color=(255, 255, 255), text_pos=(60, 5))
            self.level_text(text_size=14, text=f'fps {clock.get_fps() :.0f}', text_color=(255, 255, 255), text_pos=(20, 300))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=(255, 255, 255), text_pos=(40, 310))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewrite", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)