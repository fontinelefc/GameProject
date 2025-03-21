#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display

from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = listEntity = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
            pygame.display.flip()
        pass
