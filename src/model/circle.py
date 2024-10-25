import pygame
from model.form import Form



class Circle(Form) :
    
    def __init__(self, window, position, radius = 30) :
        
        super().__init__(window, position)
        self.radius = radius
        # self.radius = 30
        # self.position = position
        # self.position = pygame.Vector2(self.window.getScreenWidth() / 2, self.window.getScreenHeight() / 2)
    
    def drawSprite(self) :
        
        pygame.draw.circle(self.window.screen, "green", self.position, self.radius)
    
    def getRadius(self) :
        
        return self.radius