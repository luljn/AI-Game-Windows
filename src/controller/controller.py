import pygame
from pygame_textinput import TextInputVisualizer, TextInputManager
from sys import exit

from model.buttonAction import ButtonAction
from model.factory import *
from model.config import Config
from model.sound import Sound

from view.view import View
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
        
        #Buttons
        self.buttons = self.factory.buttonFactory(self.window, View.WELCOME.value)
    
    #main controller method
    def run(self) :
        
        pygame.display.set_caption(self.window.getTitle())
        forms = self.factory.formFactory(self.window)
        
        #Load previous configs.
        configs = Config.loadConfig()
        
        #Check if the music must be enabled at the starting or not.
        if(configs[3] == "ON") :
            
            Sound.getAndPlaySound(Sound.default_music)
        
        """Text input management"""
        #Creation of the manager and the visualizer of the text input.
        text_manager = TextInputManager()  #manage the text input.
        text_input = TextInputVisualizer(manager=text_manager)  #display the text input.

        # Position of the text input
        text_input.cursor_visible = True  #Set the cursor visible.
        text_input.cursor_color = (255, 255, 255)
        text_input.font_color = (255, 255, 255)  #Set the colot of the text input.
        """"""
        
        #Game loop
        while self.running :
            
            self.clickEventHandler(self.buttons)
            # self.KeyEventHandler()
            self.viewsManager(forms, text_input)
            
        
        self.quit()
    
    #To display the rigth view.
    def viewsManager(self, forms, text_input) :
        
        if(self.window.getView() == View.WELCOME.value) : 
            
            self.buttons = self.factory.buttonFactory(self.window, View.WELCOME.value)
            self.welcome(self.buttons)
        
        elif(self.window.getView() == View.GAME.value) : 
            
            self.buttons = self.factory.buttonFactory(self.window, View.GAME.value)
            self.game(forms, self.buttons)
        
        elif(self.window.getView() == View.OPTIONS.value) : 
            
            self.buttons = self.factory.buttonFactory(self.window, View.OPTIONS.value)
            self.options(self.buttons, text_input)
        
        elif(self.window.getView() == View.CREDITS.value) : 
            
            self.buttons = self.factory.buttonFactory(self.window, View.CREDITS.value)
            self.credits(self.buttons)
    
    ''' Events management. '''
    #Click events management.
    def clickEventHandler(self, buttons) : 
        
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                
                self.quit()
            
            for button in buttons :
                
                if(event.type == pygame.MOUSEBUTTONDOWN) :
                    
                    #Launch the game view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.PLAY.value) :
                        
                        #To load the configs before starting the game.
                        Config.loadConfig()
                        self.window.setView(View.GAME.value)
                    
                    #Launch the options view.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.OPTIONS.value) :
                        
                        self.window.setView(View.OPTIONS.value)
                    
                    #Change the color of the user's pawns to green.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.GREEN.value) :
                        
                        Config.changeColor("GREEN")
                    
                    #Change the color of the user's pawns to red.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.RED.value) :
                        
                        Config.changeColor("RED")
                    
                    #Change the mode of the game to : PLAYER vs CPU.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.PLAYER_VS_CPU.value) :
                        
                        Config.changeMode("1")
                    
                    #Change the mode of the game to : CPU vs CPU.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.CPU_VS_CPU.value) :
                        
                        Config.changeMode("2")
                    
                    #Change the music to ON.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.MUSIC_ON.value) :
                        
                        Config.stopOrEnableMusic("ON")
                        Sound.getAndPlaySound(Sound.default_music)
                    
                    #Change the music to OFF.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.MUSIC_OFF.value) :
                        
                        Config.stopOrEnableMusic("OFF")
                        Sound.stopSound()
                    
                    #Launch the credits view.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.CREDITS.value) :
                        
                        self.window.setView(View.CREDITS.value)
                    
                    #Save the options(in the options view).
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.SAVE.value) :
                        
                        #action to save the options chose by the user (to define).
                        pass
                    
                    #Launch the options view.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.BACK.value) :
                        
                        self.window.setView(View.WELCOME.value)
                    
                    #Close the window and quit the game.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.QUIT.value) :
                        
                        self.quit()
    
    #Keys event management.
    def KeyEventHandler(self) : 
        
        pass
    
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
    
    def options(self, buttons, text_input) :
        
        self.window.optionsView(buttons, text_input)
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