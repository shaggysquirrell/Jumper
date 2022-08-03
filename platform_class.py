# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:22:11 2019
@author: Rogelio Garcia
"""

####################
## Platform Class ##
####################

import pygame
from pygame.sprite import Sprite

class Platform(Sprite):
    def __init__(self, screen, ai_set, x, y):
        super(Platform, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, ai_set.platform_width, ai_set.platform_height)
        self.screen_rect = self.screen.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.color = ai_set.platform_color
        self.speed = ai_set.platform_speed
        
        self.x = float(self.rect.x)
    
    def update(self):

        if self.rect.right < self.screen_rect.left:
            self.x = self.screen_rect.right
            
        else:
            self.x -= self.speed
            
        self.rect.x = self.x
        
    def draw_me(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        