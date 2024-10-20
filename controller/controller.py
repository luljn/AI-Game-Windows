import pygame
from model.circle import *
from model.square import *
from model.factory import *
from view.window import *



class Controller :
    
    def __init__(self) :
        
        #Pygame initailization
        pygame.init()
        
        #Game loop variable
        self.running = True
        
        #
        self.window = Window()
        self.circle = Circle(self.window)
        self.square = Square(self.window)
        self.factory = Factory()
    
    #main controller method
    def run(self) :
        
        pygame.display.set_caption(self.window.getTitle())
        buttons = self.factory.buttonFactory(self.window)
        
        while self.running :
            
            for event in pygame.event.get() :
                
                if event.type == pygame.QUIT :
                    
                    self.running = False
                
                for button in buttons :
                    
                    #Click event management 
                    if(event.type == pygame.MOUSEBUTTONDOWN) :
                        
                        if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Quitter") :
                        
                            self.running == False
                            pygame.quit()
            
            # self.window.gameView()
            self.window.welcomeView(buttons)
            self.square.move(self.window.dt)
            self.circle.move(self.window.dt)
            pygame.display.flip()
            pygame.display.update()
            
        self.quit()
    
    def quit(self):
        
        pygame.quit()