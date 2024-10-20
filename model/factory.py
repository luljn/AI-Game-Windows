#The factory of the programm
import pygame
from model.button import *
from model.font import *



class Factory :
    
    def __init__(self):
        
        self.font = Font()
    
    def buttonFactory(self, window) : 
        
        start_game_button = Button(pygame.image.load("resources\img\Rect.png"), (window.getScreenWidth() / 1.27, window.getScreenHeight() / 4), "Jouer", self.font.getFont(25), "White", "Blue")
        options_button = Button(pygame.image.load("resources\img\Rect.png"), (window.getScreenWidth() / 1.27, 420), "Options", self.font.getFont(25), "White", "Blue")
        quit_button = Button(pygame.image.load("resources\img\Rect.png"), (window.getScreenWidth() / 1.27, 540), "Quitter", self.font.getFont(25), "White", "Blue")
        
        buttons = [start_game_button, options_button, quit_button]
        
        return buttons