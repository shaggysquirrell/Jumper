# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:42:56 2019

@author: Rogelio Garcia
"""

import pygame
from pygame.sprite import Sprite

class Platform_up(Sprite):
    def __init__(self, screen, ai_set, x, y):
        super(Platform_up, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, ai_set.platform_width, ai_set.platform_height)
        self.screen_rect = self.screen.get_rect()
        
        self.color = ai_set.platform_up_color
        self.speed = ai_set.platform_up_speed
        
        self.rect.centerx = x
        self.rect.centery = y
        
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        
        self.top = True
        self.bottom = False
        
    def update(self):
        if self.top:
            if self.rect.top < 500:
                self.y += self.speed
            else:
                self.top = False
                self.bottom = True
                
            self.rect.centery = self.y
            
        if self.bottom:
            if self.rect.top > 100:
                self.y -= self.speed
            else:
                self.top = True
                self.bottom = False
            
            self.rect.centery = self.y
            
    def draw_me(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
            
            