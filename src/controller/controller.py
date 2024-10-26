import pygame
from sys import exit

from model.buttonAction import ButtonAction
from model.factory import *
from model.sound import Sound

from view.view import View
from view.window import *



class Controller :
    
    def __init__(self) :
        
        #Pygame initilization
        pygame.init()
        # pygame.mixer.init()
        
        #Game loop variable
        self.running = True
        
        #
        self.window = Window()
        self.factory = Factory()
        
        #Buttons
        self.buttons = self.factory.buttonFactory(self.window, View.WELCOME.value)
    
    #main controller method
    def run(self) :
        
        pygame.display.set_caption(self.window.getTitle())
        # Sound.getAndPlaySound("resources/sounds/Treachery.mp3")
        forms = self.factory.formFactory(self.window)
        
        #Game loop
        while self.running :
            
            self.eventHandler(self.buttons)
            
            if(self.window.getView() == View.WELCOME.value) : 
                
                self.buttons = self.factory.buttonFactory(self.window, View.WELCOME.value)
                self.welcome(self.buttons)
            
            elif(self.window.getView() == View.GAME.value) : 
                
                self.buttons = self.factory.buttonFactory(self.window, View.GAME.value)
                self.game(forms, self.buttons)
            
            elif(self.window.getView() == View.OPTIONS.value) : 
                
                self.buttons = self.factory.buttonFactory(self.window, View.OPTIONS.value)
                self.options(self.buttons)
            
            elif(self.window.getView() == View.CREDITS.value) : 
                
                self.buttons = self.factory.buttonFactory(self.window, View.CREDITS.value)
                self.credits(self.buttons)
            
        self.quit()
    
    #Events management.
    def eventHandler(self, buttons) : 
        
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                
                self.running = False
            
            for button in buttons :
                
                #Click event management.
                if(event.type == pygame.MOUSEBUTTONDOWN) :
                    
                    #Launch the game view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.PLAY.value) :
                        
                        self.window.setView(View.GAME.value)
                    
                    #Launch the options view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.OPTIONS.value) :
                        
                        self.window.setView(View.OPTIONS.value)
                    
                    #Launch the credits view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.CREDITS.value) :
                        
                        self.window.setView(View.CREDITS.value)
                    
                    #Save the options(in the options view).
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.SAVE.value) :
                        
                        #action to save the options chose by the user (to define).
                        pass
                    
                    #Launch the options view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.BACK.value) :
                        
                        self.window.setView(View.WELCOME.value)
                    
                    #Close the window and quit the game.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.QUIT.value) :
                        
                        self.quit()
    
    def welcome(self, buttons) :
        
        self.window.welcomeView(buttons)
        pygame.display.flip()
        pygame.display.update()
    
    def game(self, forms, buttons) :
        
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