#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.Background import Background
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
                return Player('Player1', position=(10, 100))

            case 'Enemy1':
                return Player('Enemy1', position=(576 + 10, random.randint(0, 324)))
            case 'Enemy2':
                return Player('Enemy2', position=(576 + 10, random.randint(0, 324)))
