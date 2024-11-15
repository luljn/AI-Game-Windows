import pygame
from model.form import Form



class Square(Form) :
    
    #Empty square (the central at the beginning of the game).
    empty_square_id = 4
    canMove = False
    
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
        
        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_UP] : 
            
            self.moveUp()
        
        if self.keys[pygame.K_DOWN] : 
            
            self.moveDown()
        
        if self.keys[pygame.K_LEFT] : 
            
            self.moveLeft()
        
        if self.keys[pygame.K_RIGHT] : 
            
            self.moveRight()
    
    def moveUp(self) : 
        
        #If the square is not on the first line, we can move up.
        if (self.id != 0 and self.id != 1 and self.id != 2 
            and Square.empty_square_id == self.id - 3) :
            
            self.position.y = (self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2
            
            if (self.id == 3 or self.id == 4 or self.id == 5 
            and Square.empty_square_id == self.id - 3) :
                
                self.position.y = ((self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2) - ((self.window.getScreenHeight() / 10) + 10)
            
            self.id -= 3
            Square.empty_square_id += 3
    
    def moveDown(self) : 
        
        #If the square is not on the 3rd line, we can move down.
        if (self.id != 6 and self.id != 7 and self.id != 8 
            and Square.empty_square_id == self.id + 3) :
            
            self.position.y =  ((self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2) + ((self.window.getScreenHeight() / 10) + 10)
            
            if (self.id == 0 or self.id == 1 or self.id == 2 
            and Square.empty_square_id == self.id + 3) :
                
                self.position.y =  (self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2
            
            self.id += 3
            Square.empty_square_id -= 3
    
    def moveLeft(self) :
        
        #If the square is not on the 1st column, we can move left.
        if (self.id != 0 and self.id != 3 and self.id != 6 
            and Square.empty_square_id == self.id - 1) :
            
            self.position.x = ((self.window.getScreenWidth() / 2) -  (self.window.getScreenWidth() / 16) / 2) - ((self.window.getScreenWidth() / 16) + 10)
            
            if (self.id == 2 or self.id == 5 or self.id == 8 
                and Square.empty_square_id == self.id - 1) :
                
                self.position.x = (self.window.getScreenWidth() / 2) - (self.window.getScreenWidth() / 16) / 2
            
            self.id -= 1
            Square.empty_square_id += 1
    
    def moveRight(self) :
        
        #If the square is not on the 3rd column, we can move right.
        if (self.id != 2 and self.id != 5 and self.id != 8 
            and Square.empty_square_id == self.id + 1) :
            
            self.position.x = (self.window.getScreenWidth() / 2) - ((self.window.getScreenWidth() / 16) / 2)
            
            if (self.id == 1 or self.id == 4 or self.id == 7 
                and Square.empty_square_id == self.id + 1) :
                
                self.position.x = ((self.window.getScreenWidth() / 2) -  (self.window.getScreenWidth() / 16) / 2) + ((self.window.getScreenWidth() / 16) + 10)
            
            self.id += 1
            Square.empty_square_id -= 1
