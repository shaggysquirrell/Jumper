# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:15:00 2019

@author: Rogelio Garcia
"""
##############
## Settings ##
##############

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        
        self.jumper_color = (0, 0, 255)
        self.jumper_width = 20
        self.jumper_height = 20
        self.jumper_speed = .5
        self.fall_speed = .2
        self.jump_height = 80
        
        self.bg_color = (0, 0, 0)
        
        self.platform_color = (0, 255, 0)
        self.platform_width = 50
        self.platform_height = 10
        
        self.platform_up_color = (255, 0, 0)
        self.platform_up_speed = .1
        
        self.platform_speed = .2
        
        self.platform_x = [400, 600, 700, 100]
        self.platform_y = [300, 500, 400, 550]
        
        