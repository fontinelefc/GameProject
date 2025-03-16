#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from Code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(720, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

    #        for event in pygame.event.get():
    #           if event.type == pygame.QUIT:
    #               pygame.quit() # close window
    #               quit() # end pygame
