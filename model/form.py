import pygame



class Form :
    
    def __init__(self, window):
        
        self.window = window
        self.position = pygame.Vector2(self.window.getScreenWidth() / 2, self.window.getScreenHeight() / 2)
    
    def move(self, dt) :
        
        pass