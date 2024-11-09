import pygame
from model.form import Form



class Square(Form) :
    
    #Empty square (the central at the beginning of the game).
    empty_square_id = 4
    
    def __init__(self, id, window, width, height, position, color = "Blue") :
        
        super().__init__(window, position)
        self.id = id
        self.width = width
        self.height = height
        self.color = color
        self.image = None
        # self.width = self.window.getScreenWidth() / 16
        # self.height = self.window.getScreenHeight() / 10
        # self.position = pygame.Vector2((self.window.getScreenWidth() / 2) -  self.width / 2 , (self.window.getScreenHeight() / 2) - self.height /2)
    
    def drawSprite(self) :
        
        self.image = pygame.draw.rect(self.window.screen, self.color, (self.position.x, self.position.y, self.width, self.height))
    
    # def checkPosition(self, position) :
        
    #     if (position[0] in range (self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom)):
            
    #         return True
        
    #     return False
    
    def getId(self) :
        
        return self.id
    
    def getWidth(self) :
        
        return self.width
    
    def getHeigth(self) :
        
        return self.height
    
    def setColor(self, color) :
        
        self.color = color
    
    def getImage(self) : 
        
        return self.image
    
    def move(self) :
        
        pass
