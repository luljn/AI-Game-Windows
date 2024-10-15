import pygame



class Window :
    
    def __init__(self):
        
        #screen dimensions
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        
        #screen configurations
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.dt = 0
    
    def show(self) :
        
        self.screen.fill("black")
        self.dt = self.clock.tick(60) / 1000
        
    def getScreenWidth(self) :
        
        return self.screen_width
    
    def getScreenHeight(self) :
        
        return self.screen_height