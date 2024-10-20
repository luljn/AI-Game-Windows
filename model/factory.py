#The factory of the programm
import pygame
from view.button import *
from view.font import *



class Factory :
    
    def __init__(self):
        
        self.font = Font()
    
    def buttonFactory(self) : 
        
        quit_button = Button(pygame.image.load("resources\img\Rect.png"), (980, 540), "Quitter", self.font.getFont(25), "White", "Blue")
        
        buttons = [quit_button]
        
        return buttons