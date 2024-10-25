import pygame
from sys import exit

from model.factory import *
from model.sound import Sound

from view.window import *



class Controller :
    
    def __init__(self) :
        
        #Pygame initilization
        pygame.init()
        pygame.mixer.init()
        
        #Game loop variable
        self.running = True
        
        #
        self.window = Window()
        self.factory = Factory()
    
    #main controller method
    def run(self) :
        
        pygame.display.set_caption(self.window.getTitle())
        Sound.getAndPlaySound("resources/sounds/map_music.wav")
        buttons = self.factory.buttonFactory(self.window)
        forms = self.factory.formFactory(self.window)
        
        #Game loop
        while self.running :
            
            self.eventHandler(buttons)
            
            if(self.window.getView() == "welcome") : 
                
                self.welcome(buttons)
            
            elif(self.window.getView() == "game") : 
                
                self.game(buttons, forms)
            
            elif(self.window.getView() == "options") : 
                
                self.options(buttons)
            
            elif(self.window.getView() == "credits") : 
                
                self.credits(buttons)
            
        self.quit()
    
    def eventHandler(self, buttons) : 
        
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                
                self.running = False
            
            for button in buttons :
                
                #Click event management.
                if(event.type == pygame.MOUSEBUTTONDOWN) :
                    
                    #Launch the game view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Jouer") :
                        
                        self.window.setView("game")
                    
                    #Launch the options view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Options") :
                        
                        self.window.setView("options")
                        
                    #Launch the credits view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Crédits") :
                        
                        self.window.setView("credits")
                    
                    #Save the options(in the options view).
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Enregistrer") :
                        
                        #action to save the options chose by the user (to define).
                        pass
                    
                    #Launch the options view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Retour") :
                        
                        self.window.setView("welcome")
                    
                    #Close the window and quit the game.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == "Quitter") :
                        
                        self.quit()
    
    def welcome(self, buttons) :
        
        self.window.welcomeView(buttons)
        pygame.display.flip()
        pygame.display.update()
    
    def game(self, buttons, forms) :
        
        self.window.gameView(buttons)
        
        for form in forms :
            
            form.drawSprite()
            form.move(self.window.getDT())
        
        pygame.display.flip()
    
    def options(self, buttons) :
        
        self.window.optionsView(buttons)
        pygame.display.flip()
        pygame.display.update()
    
    def credits(self, buttons) : 
        
        self.window.creditsView(buttons)
        pygame.display.flip()
        pygame.display.update()
    
    #Close the window and quit the program
    def quit(self):
        
        self.running == False
        pygame.quit()
        exit()