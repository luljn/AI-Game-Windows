import pygame
from sys import exit
from model.circle import *
from model.square import *
from model.factory import *
from view.window import *



class Controller :
    
    def __init__(self) :
        
        #Pygame initailization
        pygame.init()
        pygame.mixer.init()
        
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
        pygame.mixer.music.load("resources\sounds\map_music.wav")
        pygame.mixer.music.play(-1)
        buttons = self.factory.buttonFactory(self.window)
        
        while self.running :
            
            for event in pygame.event.get() :
                
                if event.type == pygame.QUIT :
                    
                    self.running = False
                
                for button in buttons :
                    
                    #Click event management 
                    if(event.type == pygame.MOUSEBUTTONDOWN) :
                        
                        #Launch the game view.
                        if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Jouer") :
                            
                            self.window.setView("game")
                        
                        #Launch the options view.
                        if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Options") :
                            
                            self.window.setView("options")
                            
                        #Launch the options view.
                        if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Retour") :
                            
                            self.window.setView("welcome")
                        
                        #Close the window and quit the game
                        if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Quitter") :
                        
                            self.running == False
                            self.quit()
                            exit()
            
            if(self.window.getView() == "welcome") : 
                
                self.window.welcomeView(buttons)
                pygame.display.flip()
                pygame.display.update()
            
            if(self.window.getView() == "game") : 
                
                self.window.gameView(buttons)
                self.square.drawSprite()
                self.circle.drawSprite()
                self.square.move(self.window.dt)
                self.circle.move(self.window.dt)
                pygame.display.flip()
                pygame.display.update()
                
            if(self.window.getView() == "options") : 
                
                self.window.optionsView(buttons)
                pygame.display.flip()
                pygame.display.update()
            
        self.quit()
    
    def quit(self):
        
        pygame.quit()