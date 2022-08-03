# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:20:15 2019

@author: Rogelio Garcia
"""
############
## Jumper ##
############

import pygame

class Jumper():
    def __init__(self, screen, ai_set, platforms):
        self.screen = screen
        self.platforms = platforms
        
        self.rect = pygame.Rect(0, 0, ai_set.jumper_width, ai_set.jumper_height)
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - ai_set.jumper_height
        
        self.color = ai_set.jumper_color
        self.speed = ai_set.jumper_speed
        self.fall_speed = ai_set.fall_speed
        self.jump_height = ai_set.jump_height
        
        self.gravity = True
        self.jump = False
        self.moving_right = False
        self.moving_left = False
        self.move_down_off = False
        
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        
        self.platform_speed = ai_set.platform_speed
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
            
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
            
        if self.gravity and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.fall_speed
            
        if self.jump and self.rect.top > self.screen_rect.top:
            self.y -= self.jump_height
            self.jump = False
            
        if self.rect.right < self.screen_rect.left:
            self.x = self.screen_rect.right - float(1/2 * self.rect.width)
            
        else:
            self.gravity = True
        
        self.rect.centerx = self.x
        self.rect.bottom = self.y
        
    def draw_me(self):
        pygame.draw.rect(self.screen, self.color, self.rect)