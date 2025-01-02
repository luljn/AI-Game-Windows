# Base class of shapes used in the game.
from pygame import Vector2

from view.window import Window



class Form :
    
    def __init__(self, window:Window, position:Vector2):
        
        self.window = window
        self.position = position
        
        # Keyboard keys
        self.keys = 0
    
    def move(self) :
        
        pass
    
    def drawSprite(self) :
        
        pass
