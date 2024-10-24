#The factory of the programm
import pygame

from model.button import *
from model.font import *



class Factory :
    
    def __init__(self):
        
        super().__init__()
    
    def buttonFactory(self, window) : 
        
        rect_img_path = "resources\img\Rect.png"
        position_x = window.getScreenWidth() / 3.05
        font = Font.getFont(25)
        
        start_game_button = Button(pygame.image.load(rect_img_path), (position_x, window.getScreenHeight() / 2.7), "Jouer", font, "White", "Blue")
        options_button = Button(pygame.image.load(rect_img_path), (position_x, start_game_button.position_y + 120), "Options", font, "White", "Blue")
        quit_button = Button(pygame.image.load(rect_img_path), (position_x, options_button.position_y + 120), "Quitter", font, "White", "Blue")
        back_button = Button(pygame.image.load(rect_img_path), (window.getScreenWidth() / 1.25, quit_button.position_y + 230), "Retour", font, "White", "Blue")
        
        buttons = [start_game_button, options_button, quit_button, back_button]
        
        return buttons