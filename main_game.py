# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:21:51 2019

@author: Rogelio Garcia
"""
###############
## Main Game ##
###############

import pygame
from jumper import Jumper
from settings import Settings
import game_functions as gf
from pygame.sprite import Group

def run():
    pygame.init()
    ai_set = Settings()
    platforms = Group()
    platforms_up = Group()
    
    screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
    pygame.display.set_caption('Jumper (Failure Is Required)')
    
    jumper = Jumper(screen, ai_set, platforms)
    clock = pygame.time.Clock()
    
    run = True 
    gf.create_platforms(screen, ai_set, platforms)
    gf.create_platforms_up(screen, ai_set, platforms_up)
    while run:
        clock.tick(330)
        gf.check_events(jumper)
        jumper.update()
        platforms.update()
        platforms_up.update()
        gf.update_screen(screen, ai_set, jumper, platforms, platforms_up)
        gf.find_touch_down(platforms, platforms_up, jumper, ai_set)
        
run()
    
    