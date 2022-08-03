# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:22:34 2019

@author: Rogelio Garcia
"""
####################
## Game Functions ##
####################

import pygame
from platform_class import Platform
from going_up import Platform_up

def create_platforms(screen, ai_set, platforms):
    for i in range(int(len(ai_set.platform_x))):
        new_platform = Platform(screen, ai_set, ai_set.platform_x[i], ai_set.platform_y[i])
        platforms.add(new_platform)
        
def create_platforms_up(screen, ai_set, platforms_up):
    for i in range(int(len(ai_set.platform_x))):
        new_platform = Platform_up(screen, ai_set, ai_set.platform_x[i], ai_set.platform_y[i])
        platforms_up.add(new_platform)
        
def find_touch_down(platforms, platforms_up, jumper, ai_set):
    for platform in platforms.sprites():
        if jumper.rect.bottom == platform.rect.top and jumper.rect.left < platform.rect.right and jumper.rect.right > platform.rect.left:
            jumper.gravity = False
            jumper.x -= ai_set.platform_speed
            jumper.rect.centerx = jumper.x
            
    for platform in platforms_up.sprites():
        if jumper.rect.bottom == platform.rect.top and jumper.rect.left < platform.rect.right and jumper.rect.right > platform.rect.left:
            
            jumper.gravity = False
            jumper.y -= ai_set.platform_up_speed
            jumper.rect.bottom = jumper.y
            
def keydown(jumper, event):
    if event.key == pygame.K_RIGHT: ## moving right ##
        jumper.moving_right = True
    if event.key == pygame.K_LEFT: ## moving left ##
        jumper.moving_left = True
    if event.key == pygame.K_SPACE: ## jumping ##
        jumper.jump = True
    if event.key == pygame.K_q: ## quit ##
        pygame.quit()

def keyup(jumper, event):
    if event.key == pygame.K_RIGHT: ## moving right ##
        jumper.moving_right = False
    if event.key == pygame.K_LEFT: ## moving left ##
        jumper.moving_left = False
        
def check_events(jumper):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## quit ##
            pygame.quit()
            
        if event.type == pygame.KEYDOWN: ## check keydown ##
            keydown(jumper, event)
        if event.type == pygame.KEYUP: ## check keyup ##
            keyup(jumper, event)
            
def update_screen (screen, ai_set, jumper, platforms, platforms_up):
    screen.fill(ai_set.bg_color)
    jumper.draw_me()
    for platform in platforms.sprites():
        platform.draw_me()
    for platform in platforms_up.sprites():
        platform.draw_me()
    pygame.display.flip()