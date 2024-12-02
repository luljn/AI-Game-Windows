# Class for circle pawns management.
import pygame

from model.form import Form
from model.square import Square



class Circle(Form) :
    
    def __init__(self, window, position, color, square, radius = 30) :
        
        super().__init__(window, position)
        self.color = color
        self.square = square
        self.radius = radius
        self.canMove = False
        # self.radius = 30
        # self.position = position
        # self.position = pygame.Vector2(self.window.getScreenWidth() / 2, self.window.getScreenHeight() / 2)
    
    def drawSprite(self) :
        
        pygame.draw.circle(self.window.screen, self.color, self.position, self.radius)
    
    def getRadius(self) :
        
        return self.radius
    
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
        
        if self.canMove :
            
            if self.keys[pygame.K_UP] : 
                
                self.moveUp(position_y, square_width)
            
            if self.keys[pygame.K_DOWN] : 
                
                self.moveDown(position_y, square_width)
            
            if self.keys[pygame.K_LEFT] : 
                
                self.moveLeft(position_x, distance)
            
            if self.keys[pygame.K_RIGHT] : 
                
                self.moveRight(position_x, distance)
    
    def moveUp(self, position_y, square_width) : 
        
        #If the square is not on the first line, we can move up.
        if (self.square.id != 0 and self.square.id != 1 and self.square.id != 2 
            and Square.empty_square_id == self.square.id - 3) :
            
            self.position.y = position_y
            self.square.position.y = (self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2
            
            if (self.square.id == 3 or self.square.id == 4 or self.square.id == 5 
            and Square.empty_square_id == self.square.id - 3) :
                
                self.position.y = position_y - square_width
                self.square.position.y = ((self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2) - ((self.window.getScreenHeight() / 10) + 10)
            
            self.square.id -= 3
            Square.empty_square_id += 3
    
    def moveDown(self, position_y, square_width) : 
        
        #If the square is not on the 3rd line, we can move down.
        if (self.square.id != 6 and self.square.id != 7 and self.square.id != 8 
            and Square.empty_square_id == self.square.id + 3) :
            
            self.position.y = position_y + square_width
            self.square.position.y =  ((self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2) + ((self.window.getScreenHeight() / 10) + 10)
            
            if (self.square.id == 0 or self.square.id == 1 or self.square.id == 2 
            and Square.empty_square_id == self.square.id + 3) :
                
                self.position.y = position_y
                self.square.position.y =  (self.window.getScreenHeight() / 2) - (self.window.getScreenHeight() / 10) /2
            
            self.square.id += 3
            Square.empty_square_id -= 3
    
    def moveLeft(self, position_x, distance) :
        
        #If the square is not on the 1st column, we can move left.
        if (self.square.id != 0 and self.square.id != 3 and self.square.id != 6 
            and Square.empty_square_id == self.square.id - 1) :
            
            self.position.x = position_x -  distance
            self.square.position.x = ((self.window.getScreenWidth() / 2) -  (self.window.getScreenWidth() / 16) / 2) - ((self.window.getScreenWidth() / 16) + 10)
            
            if (self.square.id == 2 or self.square.id == 5 or self.square.id == 8 
                and Square.empty_square_id == self.square.id - 1) :
                
                self.position.x = position_x
                self.square.position.x = (self.window.getScreenWidth() / 2) - (self.window.getScreenWidth() / 16) / 2
            
            self.square.id -= 1
            Square.empty_square_id += 1
    
    def moveRight(self, position_x, distance) :
        
        #If the square is not on the 3rd column, we can move right.
        if (self.square.id != 2 and self.square.id != 5 and self.square.id != 8 
            and Square.empty_square_id == self.square.id + 1) :
            
            self.position.x = position_x
            self.square.position.x = (self.window.getScreenWidth() / 2) - ((self.window.getScreenWidth() / 16) / 2)
            
            if (self.square.id == 1 or self.square.id == 4 or self.square.id == 7 
                and Square.empty_square_id == self.square.id + 1) :
                
                self.position.x = position_x + distance
                self.square.position.x = ((self.window.getScreenWidth() / 2) -  (self.window.getScreenWidth() / 16) / 2) + ((self.window.getScreenWidth() / 16) + 10)
            
            self.square.id += 1
            Square.empty_square_id -= 1
    
    def changeSquare(self, squares, new_square_id) :
        
        for pawn in squares : 
            
            if self.square.id == pawn.square.id and new_square_id == pawn.square.id :
                
                self.square = pawn.square
                squares.remove(pawn)
