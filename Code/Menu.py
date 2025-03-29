#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/orig_menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/sound_menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size= 80, text= "Aerial", text_color= (10, 32, 66), text_center_pos=  (288, 70))
            self.menu_text(text_size=80, text="Clash", text_color=(10, 32, 66), text_center_pos=(288, 125))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=40, text=MENU_OPTION[i],text_color=(1, 198, 255), text_center_pos=(288, 190 + 30 * i))
                else:
                    self.menu_text(text_size=40, text=MENU_OPTION[i], text_color=(225, 255, 255), text_center_pos=(288, 190 + 30 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit() # close window
                       quit() # end pygame
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_DOWN: # verificação de tecla seta para baixo
                           if menu_option < len(MENU_OPTION) - 1:
                               menu_option += 1
                           else:
                               menu_option = 0

                       if event.key == pygame.K_UP: # verificação de tecla seta para cima
                           if menu_option > 0:
                               menu_option -= 1
                           else:
                               menu_option = len(MENU_OPTION) - 1

                       if event.key == pygame.K_RETURN: # Enter
                           return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewrite", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
