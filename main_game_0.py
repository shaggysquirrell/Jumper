# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:23:50 2019

@author: Rogelio Garcia
"""

import pygame
from settings_0 import Settings
from ship_class_0 import Player
import game_functions_0 as gf
from pygame.sprite import Group

def run():
    pygame.init()
    ai_set = Settings()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Jumper')
    
    platforms = Group()
    player = Player(screen, ai_set)

    run = True 
    while run:
        gf.check_events(player)
        
        for platform in platforms.copy():
            platforms.remove(platform)

        gf.update_platform(screen, ai_set, player, platforms)
        platforms.update(ai_set)

        gf.update_screen(screen, player, ai_set, platforms)
        
        for platform in platforms.copy():
            platforms.remove(platform)
                
        print(player.rect.centerx, player.rect.bottom)
        
run()