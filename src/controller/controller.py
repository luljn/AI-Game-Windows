# Main Controller.
import pygame
from os import system
from pygame_textinput import TextInputVisualizer, TextInputManager
from sys import exit

from controller.checkWinner import *

from model.buttonAction import ButtonAction
from model.factory import *
from model.config import Config
from model.sound import Sound

from view.view import View
from view.window import *



class Controller :
    
    def __init__(self) :
        
        # Pygame initilization
        pygame.init()
        pygame.mixer.init()
        
        # Game loop variable
        self.running = True
        
        # Game configurations
        self.configs = Config.loadConfig()
        
        #
        self.window = Window()
        self.factory = Factory()
        
        # Set on squares, to construct the game board.
        self.forms = self.factory.formFactory(self.window)
        
        # Buttons
        self.buttons = self.factory.buttonFactory(self.window, View.WELCOME.value)
    
    # main controller method
    def run(self) :
        
        system("cls")
        pygame.display.set_caption(self.window.getTitle())
        
        # Check if the music must be enabled at the starting or not.
        if(self.configs[4] == "ON") :
            
            Sound.getAndPlaySound(Sound.default_music)
        
        # forms = self.factory.formFactory(self.window, configs)
        
        """Text input management"""
        # Creation of the manager and the visualizer of the text input.
        text_manager = TextInputManager()  # manage the text input.
        text_input = TextInputVisualizer(manager=text_manager)  # display the text input.
        
        # Position of the text input
        text_input.cursor_visible = True  # Set the cursor visible.
        text_input.cursor_color = (255, 255, 255)
        text_input.font_color = (255, 255, 255)  # Set the colot of the text input.
        """"""
        
        # Game loop
        while self.running :
            
            self.eventHandler(self.buttons, text_manager)
            # self.KeyEventHandler()
            self.viewsManager(self.forms, text_input)
            self.window.clock.tick(60)
            # pygame.display.flip()
        
        self.quit()
    
    # To display the rigth view.
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
    # Events management handler.
    def eventHandler(self, buttons, text_manager) : 
        
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                
                self.quit()
            
            # key(s) pressed
            if(event.type == pygame.KEYDOWN) :
                
                # Add player pawns on the board.
                self.factory.circleFactory(self.window, event, self.forms)
                # Add cpu pawns on the board.
                self.factory.cpuCircleFactory(self.window, self.forms)
                #
                self.factory.transparentCircles(Factory.circles, Factory.circles_cpu, self.forms, self.window)
                
                # If the key associated to the id of the pawn's square is pressed, we can move it.
                for circle in Factory.circles :
                    
                    if event.key == (circle.square.id + 48) :
                        
                        circle.canMove = True
                        print(circle.square.id + 48)
                
                # move squares without pawns.
                # for circle in Factory.squares_without_circle :
                    
                #     if event.key == (circle.square.id + 48) :
                        
                #         circle.canMove = True
                #         print(circle.square.id + 48)
                
                # To move two pawns at the same time.
                for circle in Factory.circles :
                    
                    if event.key == pygame.K_d :
                        
                        circle.canMove = True
                        print(event.key)
                
                # If the key 's' is pressed we can move the squares which don't have a pawn.
                for square in self.forms :
                    
                    if keys[pygame.K_s] and keys[square.id + 48]  :
                        
                        # Square.canMove = True
                        square.canMove = True
                        print(square.id + 48)
            
            # key(s) released.
            if(event.type == pygame.KEYUP) :
                
                # If the key associated to the id of the pawn's square is not pressed, we can't move it.
                for circle in Factory.circles :
                    
                    if event.key == circle.square.id + 48 :
                        
                        circle.canMove = False
                        print(f"False - {circle.square.id + 48}")
                    
                    else :
                        
                        circle.canMove = False
                
                # can't move squares without pawns.
                # for circle in Factory.squares_without_circle :
                    
                #     if event.key == circle.square.id + 48 :
                        
                #         circle.canMove = False
                #         print(f"False - {circle.square.id + 48}")
                    
                #     else :
                        
                #         circle.canMove = False
                
                # If the key 's' is not pressed we can't move the squares which don't have a pawn.
                for square in self.forms :
                    
                    if keys[pygame.K_s] and keys[square.id + 48]  :
                        
                        # Square.canMove = False
                        square.canMove = False
                        print(square.id + 48)
                    
                    else :
                        
                        # Square.canMove = False
                        square.canMove = False
            
            # Buttons click management
            for button in buttons :
                
                if(event.type == pygame.MOUSEBUTTONDOWN) :
                    
                    # Launch the game view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.PLAY.value) :
                        
                        # To load the configs before starting the game.
                        # Config.loadConfig()
                        self.window.setView(View.GAME.value)
                    
                    # Restart the game.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.RESTART.value) :
                        
                        Factory.circles = []
                        Factory.circles_cpu = []
                        self.forms = []
                        self.forms = self.factory.formFactory(self.window)
                        self.buttons = self.factory.buttonFactory(self.window, View.GAME.value)
                        self.game(self.forms, self.buttons)
                    
                    # Launch the options view.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.OPTIONS.value) :
                        
                        self.window.setView(View.OPTIONS.value)
                    
                    # Change the color of the user's pawns to green.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.GREEN.value) :
                        
                        Config.changeColor("GREEN")
                        Config.changeCpuColor("RED")
                        # Config.changeTurn(0)
                    
                    # Change the color of the user's pawns to red.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.RED.value) :
                        
                        Config.changeColor("RED")
                        Config.changeCpuColor("GREEN")
                        # Config.changeTurn(1)
                    
                    # Change the mode of the game to : PLAYER vs CPU.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.PLAYER_VS_CPU.value) :
                        
                        Config.changeMode("1")
                    
                    # Change the mode of the game to : CPU vs CPU.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.CPU_VS_CPU.value) :
                        
                        Config.changeMode("2")
                    
                    # Change the music to ON.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.MUSIC_ON.value) :
                        
                        Config.stopOrEnableMusic("ON")
                        Sound.getAndPlaySound(Sound.default_music)
                    
                    # Change the music to OFF.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.MUSIC_OFF.value) :
                        
                        Config.stopOrEnableMusic("OFF")
                        Sound.stopSound()
                    
                    # Launch the credits view.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.CREDITS.value) :
                        
                        self.window.setView(View.CREDITS.value)
                    
                    # Save the configurations (in the options view).
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.SAVE.value) :
                        
                        # action to save the options chose by the user.
                        if(text_manager.value != "") :
                            
                            Config.changePlayerName(text_manager.value)
                        
                        # Config.saveConfigs()
                        self.forms = self.factory.formFactory(self.window)
                        self.window.setView(View.WELCOME.value)
                        self.configs = Config.loadConfig()
                    
                    # Launch the options view.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.BACK.value) :
                        
                        self.window.setView(View.WELCOME.value)
                    
                    # Close the window and quit the game.
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
        
        # Player vs CPU mode.
        if self.configs[3] == "1" :
            
            # Draw the board.
            for form in forms :
                
                form.drawSprite()
                form.move()
                
                # if Square.canMove :
                    
                #     form.move()
            
            # Put pawns on the board.
            for circle in Factory.circles :
                
                circle.drawSprite()
                circle.move()
            
            for circle in Factory.circles_cpu :
                
                circle.drawSprite()
                circle.move()
            
            for circle in Factory.squares_without_circle :
                
                # circle.drawSprite()
                circle.move()
            
            # Check the winner of the game.
            winner = CheckWinner.checkPlayerVsAiWinner(Factory.circles, Factory.circles_cpu)
            
            if winner == "player" :
                
                self.window.displayTextOnTheView(f"{self.configs[0]} a gagné", 15, (self.window.screen_width / 4, self.window.screen_height / 2))
            
            elif winner == "cpu" :
                
                self.window.displayTextOnTheView("CPU a gagné", 15, (self.window.screen_width / 1.35, self.window.screen_height / 2))
        
        # CPU_1 vs CPU_2 mode.
        elif self.configs[3] == "2" :
            
            pass
        
        pygame.display.flip()
    
    def options(self, buttons, text_input) :
        
        self.window.optionsView(buttons, text_input)
        pygame.display.flip()
        pygame.display.update()
    
    def credits(self, buttons) : 
        
        self.window.creditsView(buttons)
        pygame.display.flip()
        pygame.display.update()
    
    # Close the window and quit the program
    def quit(self):
        
        self.running == False
        pygame.quit()
        exit()
