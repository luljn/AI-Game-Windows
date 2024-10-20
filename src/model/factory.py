#The factory of the programm
import pygame
from model.button import *
from model.font import *



class Factory :
    
    def __init__(self):
        
        self.font = Font()
    
    def buttonFactory(self, window) : 
        
        position_x = window.getScreenWidth() / 3.05
        start_game_button = Button(pygame.image.load("resources\img\Rect.png"), (position_x, window.getScreenHeight() / 2.7), "Jouer", self.font.getFont(25), "White", "Blue")
        options_button = Button(pygame.image.load("resources\img\Rect.png"), (position_x, start_game_button.position_y + 120), "Options", self.font.getFont(25), "White", "Blue")
        quit_button = Button(pygame.image.load("resources\img\Rect.png"), (position_x, options_button.position_y + 120), "Quitter", self.font.getFont(25), "White", "Blue")
        
        buttons = [start_game_button, options_button, quit_button]
        
        return buttons