import pygame

from model.buttonAction import ButtonAction
from model.font import Font

from view.view import View



class Window :
    
    def __init__(self):
        
        #screen dimensions
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        # self.screen_width = 1280
        # self.screen_height = 720
        
        #screen configurations
        self.title = "AI-GAME"
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.dt = 0
        
        #Mouse
        self.mouse_position = 0
        
        #A variable to know on with view we are.
        #The default view of the application is the welcome view.
        self.view = View.WELCOME.value
    
    #To display the welcome view.
    def welcomeView(self, buttons) :
        
        pygame_logo = pygame.image.load("resources\img\pygame_logo.png").convert()
        menu = pygame.image.load("resources\img\menu.png").convert()
        
        self.screen.blit(pygame.transform.scale(pygame_logo, (self.getScreenWidth(), self.getScreenHeight())), (0, 0))
        self.screen.blit(menu, (self.getScreenWidth() / 5.5, self.getScreenHeight() / 10))
        self.mouse_position = pygame.mouse.get_pos()
        
        for button in buttons :
            
            if (button.text_input != ButtonAction.BACK.value and button.text_input != ButtonAction.SAVE.value) :
                
                self.updateButton(button)
    
    #To display the game view.
    def gameView(self, buttons) :
        
        self.screen.fill("black")
        self.displayTitleOfTheView("Player 1 vs CPU")
        self.dt = self.clock.tick(60) / 1000
        self.mouse_position = pygame.mouse.get_pos()
        
        for button in buttons :
            
            if(button.text_input == ButtonAction.BACK.value) :
                
                self.updateButton(button)
    
    #To display the options(configurations) view.
    def optionsView(self, buttons) :
        
        self.screen.fill("black")
        self.displayTitleOfTheView(View.OPTIONS.value)
        self.mouse_position = pygame.mouse.get_pos()
        
        player_name = Font.getFont(25).render("Votre nom : ", True, "White")
        player_name_rect = player_name.get_rect(center = (self.screen_width / 2, self.screen_height / 3))
        self.screen.blit(player_name, player_name_rect)
        
        for button in buttons :
            
            if(button.text_input == ButtonAction.BACK.value or button.text_input == ButtonAction.SAVE.value) :
                
                self.updateButton(button)
    
    #To display the credits view.
    def creditsView(self, buttons) :
        
        self.screen.fill("black")
        self.displayTitleOfTheView(View.CREDITS.value)
        self.mouse_position = pygame.mouse.get_pos()
        
        self.displayTextOnTheView("Concepteur : Lula Jonathan (Luljn)", 25, (self.screen_width / 2, self.screen_height / 3))
        self.displayTextOnTheView("Musique : Treachery (Bleach OST) - Shiro SAGISU", 25, (self.screen_width / 2, self.screen_height / 2))
        
        for button in buttons :
            
            if(button.text_input == ButtonAction.BACK.value) :
                
                self.updateButton(button)
    
    #To display the title of the view.
    def displayTitleOfTheView(self, title) :
        
        title_ = Font.getFont(45).render(title.upper(), True, "White")
        title_rect = title_.get_rect(center = (self.screen_width / 2, self.screen_height / 15.2))
        self.screen.blit(title_, title_rect)
    
    #To display a text of the view.
    def displayTextOnTheView(self, text, text_size, position) : 
        
        text = Font.getFont(text_size).render(text, True, "White")
        text_rect = text.get_rect(center = (position[0], position[1]))
        self.screen.blit(text, text_rect)
    
    #To update a button on a viaw.
    def updateButton(self, button) : 
        
        button.changeColor(self.mouse_position)
        button.update(self.screen)
    
    #Getters and Setters.
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