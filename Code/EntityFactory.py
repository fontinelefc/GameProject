#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.Background import Background
from Code.Enemy import Enemy
from Code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'level1Bg{i}', (576,0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, 100))

            case 'Enemy1':
                return Enemy('Enemy1', (576 + 10, random.randint(0, 324 - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (576 + 10, random.randint(0, 324 - 40)))
