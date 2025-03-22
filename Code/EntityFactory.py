#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.Background import Background


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1Bg{i}', (0,0)))
                return list_bg

