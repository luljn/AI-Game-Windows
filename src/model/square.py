import pygame
from model.form import Form



class Square(Form) :
    
    def __init__(self, window, width, height, position) :
        
        super().__init__(window, position)
        self.width = width
        self.height = height
        # self.width = self.window.getScreenWidth() / 16
        # self.height = self.window.getScreenHeight() / 10
        # self.position = pygame.Vector2((self.window.getScreenWidth() / 2) -  self.width / 2 , (self.window.getScreenHeight() / 2) - self.height /2)
    
    def drawSprite(self) :
        
        pygame.draw.rect(self.window.screen, "blue", (self.position.x, self.position.y, self.width, self.height))
    
    def getWidth(self) :
        
        return self.width
    
    def getHeigth(self) :
        
        return self.height