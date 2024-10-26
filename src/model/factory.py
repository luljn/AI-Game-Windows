#The factory of the programm
import pygame

from model.button import *
from model.circle import Circle
from model.font import *
from model.square import Square



class Factory :
    
    def __init__(self):
        
        super().__init__()
    
    def buttonFactory(self, window, view = "") : 
        
        rect_img_path = "resources\img\\rect.png"
        position_x = window.getScreenWidth() / 3.05
        font = Font.getFont(25)
        
        start_game_button = Button(pygame.image.load(rect_img_path), (position_x, window.getScreenHeight() / 2.7), "Jouer", font, "White", "Blue")
        options_button = Button(pygame.image.load(rect_img_path), (position_x, start_game_button.position_y + 120), "Options", font, "White", "Blue")
        credits_button = Button(pygame.image.load(rect_img_path), (position_x, options_button.position_y + 120), "Crédits", font, "White", "Blue")
        quit_button = Button(pygame.image.load(rect_img_path), (position_x, credits_button.position_y + 120), "Quitter", font, "White", "Blue")
        save_button = Button(pygame.image.load(rect_img_path), (window.getScreenWidth() / 4.75, credits_button.position_y + 230), "Enregistrer", font, "White", "Blue")
        back_button = Button(pygame.image.load(rect_img_path), (window.getScreenWidth() / 1.25, credits_button.position_y + 230), "Retour", font, "White", "Blue")
        
        #Return a specific list of buttons, depending on the view we want to display. 
        if view == "welcome" :
            
            buttons = [start_game_button, options_button, credits_button, quit_button]
        
        elif view == "options" :
            
            buttons = [save_button, back_button]
        
        elif view == "game" or "credits" :
            
            buttons = [back_button]
        
        return buttons
    
    def formFactory(self, window) :
        
        circle = Circle(window, pygame.Vector2(window.getScreenWidth() / 2, window.getScreenHeight() / 2))
        square = Square(window, window.getScreenWidth() / 16, window.getScreenHeight() / 10,
                        pygame.Vector2((window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2 , (window.getScreenHeight() / 2) - (window.getScreenHeight() / 10) /2))
        
        forms = [square, circle]
        
        return forms