import pygame
from view.window import *



class Circle :
    
    def __init__(self):
        
        self.window = Window()
        self.position = pygame.Vector2(self.window.getScreenWidth() / 2, self.window.getScreenHeight() / 2)
        self.sprite = pygame.draw.circle(self.window.screen, "green", self.position, 40)
        
        #Keyboard keys
        self.keys = 0
    
    def move(self, dt) :
        
        self.drawSprite()
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP] : 
            
            self.position.y -= 300 * dt
        
        if self.keys[pygame.K_DOWN] : 
            
            self.position.y += 300 * dt
            
        if self.keys[pygame.K_LEFT] : 
            
            self.position.x -= 300 * dt
            
        if self.keys[pygame.K_RIGHT] : 
            
            self.position.x += 300 * dt
            
        pygame.display.flip()
            
        dt = self.window.clock.tick(60) / 1000
        
    def drawSprite(self) :
        
        pygame.draw.circle(self.window.screen, "green", self.position, 40)