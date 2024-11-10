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
        
        self.keys = pygame.key.get_pressed()
        #squares dimensions
        square_width = self.window.getScreenWidth() / 16
        square_height = self.window.getScreenHeight() / 10
        # distance between the center of squares on the same line/column.
        distance = square_width + 10
        #base position circle(the position of the central circle on the square id 4).
        position_x = self.window.getScreenWidth() / 2
        position_y = self.window.getScreenHeight() / 2
        
        if self.keys[pygame.K_UP] : 
            
            self.moveUP(position_y, square_width)
        
        if self.keys[pygame.K_DOWN] : 
            
            self.moveDown(position_y, square_width)
        
        if self.keys[pygame.K_LEFT] : 
            
            self.moveLeft(position_x, distance)
        
        if self.keys[pygame.K_RIGHT] : 
            
            self.moveRight(position_x, distance)
    
    def moveUP(self, position_y, square_width) : 
        
        #If the square is not on the first line, we can move up.
        if (self.id != 0 and self.id != 1 and self.id != 2 
            and Square.empty_square_id == self.id - 3) :
            
            # self.position.y = position_y
            self.position.y = (self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2
            
            if (self.id == 3 or self.id == 4 or self.id == 5 
            and Square.empty_square_id == self.id - 3) :
                
                # self.position.y = position_y - square_width
                self.position.y = ((self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2) - ((self.window.getScreenHeight() / 10) + 10)
            
            self.id -= 3
            Square.empty_square_id += 3
    
    def moveDown(self, position_y, square_width) : 
        
        #If the square is not on the 3rd line, we can move down.
        if (self.id != 6 and self.id != 7 and self.id != 8 
            and Square.empty_square_id == self.id + 3) :
            
            # self.position.y = position_y + square_width
            self.position.y =  ((self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2) + ((self.window.getScreenHeight() / 10) + 10)
            
            if (self.id == 0 or self.id == 1 or self.id == 2 
            and Square.empty_square_id == self.id + 3) :
                
                # self.position.y = position_y
                self.position.y =  (self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2
            
            self.id += 3
            Square.empty_square_id -= 3
    
    def moveLeft(self, position_x, distance) :
        
        #If the square is not on the 1st column, we can move left.
        if (self.id != 0 and self.id != 3 and self.id != 6 
            and Square.empty_square_id == self.id - 1) :
            
            # self.position.x = position_x -  distance
            self.position.x = ((self.window.getScreenWidth() / 2) -  (self.window.getScreenWidth() / 16) / 2) - ((self.window.getScreenWidth() / 16) + 10)
            
            if (self.id == 2 or self.id == 5 or self.id == 8 
                and Square.empty_square_id == self.id - 1) :
                
                # self.position.x = position_x
                self.position.x = (self.window.getScreenWidth() / 2) - (self.window.getScreenWidth() / 16) / 2
                
            self.id -= 1
            Square.empty_square_id += 1
    
    def moveRight(self, position_x, distance) :
        
        #If the square is not on the 3rd column, we can move right.
        if (self.id != 2 and self.id != 5 and self.id != 8 
            and Square.empty_square_id == self.id + 1) :
            
            # self.position.x = position_x
            self.position.x = (self.window.getScreenWidth() / 2) - ((self.window.getScreenWidth() / 16) / 2)
            
            if (self.id == 1 or self.id == 4 or self.id == 7 
                and Square.empty_square_id == self.id + 1) :
                
                # self.position.x = position_x + distance
                self.position.x = ((self.window.getScreenWidth() / 2) -  (self.window.getScreenWidth() / 16) / 2) + ((self.window.getScreenWidth() / 16) + 10)
                
            self.id += 1
            Square.empty_square_id -= 1
