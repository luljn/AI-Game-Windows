import pygame
from os import path



class Window :
    
    def __init__(self):
        
        #screen dimensions
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        # self.screen_width = 1280
        # self.screen_height = 720
        
        #screen configurations
        self.title = "Pygame-UI"
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.dt = 0
        
        #Mouse
        self.mouse_position = 0
        
    def welcomeView(self, buttons) :
        
        menu = pygame.image.load("resources\img\menu.PNG").convert()
        
        self.screen.fill("white")
        self.screen.blit(menu, (self.getScreenWidth() / 1.55, self.getScreenHeight() / 10))
        self.mouse_position = pygame.mouse.get_pos()
        
        for button in buttons :
            
            button.changeColor(self.mouse_position)
            button.update(self.screen)
    
    def gameView(self) :
        
        self.screen.fill("black")
        self.dt = self.clock.tick(60) / 1000
    
    def getScreenWidth(self) :
        
        return self.screen_width
    
    def getScreenHeight(self) :
        
        return self.screen_height
    
    def getTitle(self) :
        
        return self.title
    
    def getPath(self) :
        
        return path.dirname(__file__)