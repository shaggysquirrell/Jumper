# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:21:53 2019

@author: Rogelio Garcia
"""
import pygame
from bullet import Platform

def check_keydown(player, event):
    if event.key == pygame.K_LEFT:
        player.moving_left = True
    
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
        
    if event.key == pygame.K_DOWN:
        player.fall =  True
        
    if event.key == pygame.K_SPACE:
        player.jump = True
        
    if event.key == pygame.K_q:
        pygame.quit()
        
def check_keyup(player, event):
    if event.key == pygame.K_LEFT:
        player.moving_left = False
    
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
        
    if event.key == pygame.K_DOWN:
        player.fall = False
        
    if event.key == pygame.K_SPACE:
        player.jump = False
        
def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            check_keydown(player, event)
        if event.type == pygame.KEYUP:
            check_keyup(player, event)
            
def update_platform(screen, ai_set, player, platforms):
    x_y = 0
    for i in range(0, 3):
        new_platform = Platform(screen, ai_set, x_y)
        platforms.add(new_platform)
        x_y += 1

    player.update(new_platform)
            
def update_screen(screen, player, ai_set, platforms):
    screen.fill(ai_set.bg_color)
    
    '''new_platform = Platform(screen, ai_set)
    platforms.add(new_platform)'''

    for platform in platforms.sprites():
        platform.draw_platform()

    player.draw_player()
    pygame.display.flip()
        
    