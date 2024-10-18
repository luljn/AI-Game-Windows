import pygame
from model.form import Form



class Square(Form) :
    
    def __init__(self, window) :
        
        super().__init__(window)
        self.position = pygame.Vector2(self.window.getScreenWidth() / 4, self.window.getScreenHeight() / 2)
        
    def drawSprite(self) :
        
        pygame.draw.rect(self.window.screen, "blue", (self.position.x, self.position.y, self.window.getScreenWidth() / 8, self.window.getScreenHeight() / 5))