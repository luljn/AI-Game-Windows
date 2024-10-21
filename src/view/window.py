import pygame



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
        
        #A variable to know on with view we are
        self.view = "welcome"
    
    def welcomeView(self, buttons) :
        
        pygame_logo = pygame.image.load("resources\img\pygame_logo.PNG").convert()
        menu = pygame.image.load("resources\img\menu.PNG").convert()
        
        self.screen.fill("white")
        self.screen.blit(pygame.transform.scale(pygame_logo, (self.getScreenWidth(), self.getScreenHeight())), (0, 0))
        self.screen.blit(menu, (self.getScreenWidth() / 5.5, self.getScreenHeight() / 10))
        self.mouse_position = pygame.mouse.get_pos()
        
        for button in buttons :
            
            if (button.text_input != "Retour") :
                
                button.changeColor(self.mouse_position)
                button.update(self.screen)
    
    def gameView(self, buttons) :
        
        self.screen.fill("black")
        self.dt = self.clock.tick(60) / 1000
        self.mouse_position = pygame.mouse.get_pos()
        
        for button in buttons :
            
            if(button.text_input == "Retour") :
                
                button.changeColor(self.mouse_position)
                button.update(self.screen)
    
    def optionsView(self, buttons) :
        
        self.screen.fill("black")
        self.mouse_position = pygame.mouse.get_pos()
        
        for button in buttons :
            
            if(button.text_input == "Retour") :
                
                button.changeColor(self.mouse_position)
                button.update(self.screen)
    
    def getScreenWidth(self) :
        
        return self.screen_width
    
    def getScreenHeight(self) :
        
        return self.screen_height
    
    def getTitle(self) :
        
        return self.title
    
    def getView(self) :
        
        return self.view
    
    def setView(self, view) :
        
        self.view = view
        
    def getDT(self) :
        
        return self.dt
        
    def setDT(self, dt) :
        
        self.dt = dt