# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:55:52 2019

@author: Rogelio Garcia
"""

class Settings():
    def __init__(self):
        self.player_speed = .5
        self.jump_height = 2
        self.player_color = (0, 0, 255)
        
        self.player_width = 20
        self.player_height = 20
        
        self.bg_color = (0, 0, 0)
        
        self.platform_color = (0, 255, 0)
        self.platform_width = 50
        self.platform_height = 10
        self.platform_fall_factor = .2
        
        self.platform_x = [200, 300, 100]
        self.platform_y = [500, 400, 200]