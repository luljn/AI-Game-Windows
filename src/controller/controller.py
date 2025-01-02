# Main Controller.
import pygame
from os import system
from pygame_textinput import TextInputVisualizer, TextInputManager
from sys import exit

from controller.checkWinner import *
from controller.gameStatus import GameStatus

from model.buttonAction import ButtonAction
from model.factory import *
from model.config import Config
from model.minmax import MinMax
from model.sound import Sound
from model.turn import Turn

from view.view import View
from view.window import *



class Controller :
    
    def __init__(self) :
        
        # Pygame initilization
        pygame.init()
        pygame.mixer.init()
        
        # Game loop variable
        self.running = True
        
        # To determine if someone (player or cpu) has won the game.
        self.getAwinner = False
        
        # Game configurations
        self.configs = Config.loadConfig()
        
        # View and model
        self.window = Window()
        self.factory = Factory()
        
        # Set on squares, to construct the game board.
        self.forms = self.factory.formFactory(self.window)
        
        # Buttons
        self.buttons = self.factory.buttonFactory(self.window, View.WELCOME.value)
        
        # Game status
        self.game_status = GameStatus.phase_1.value
    
    # main controller method
    def run(self) :
        
        system("cls")
        pygame.display.set_caption(self.window.getTitle())
        
        # Check if the music must be enabled at the starting or not.
        if(self.configs[4] == "ON") :
            
            Sound.getAndPlaySound(Sound.default_music)
        
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
            self.viewsManager(self.forms, text_input)
            self.window.clock.tick(60)
        
        self.quit()
    
    # To display the rigth view.
    def viewsManager(self, forms:list[Square], text_input:TextInputVisualizer) :
        
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
    def eventHandler(self, buttons:list[Button], text_manager:TextInputManager) : 
        
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                
                self.quit()
            
            # Mode 1 : Player vs CPU.
            if self.configs[3] == "1" and self.window.getView() == View.GAME.value :
                
                # key(s) pressed
                if(event.type == pygame.KEYDOWN) :
                    
                    if(self.game_status == GameStatus.phase_1.value) :
                        # Add player pawns on the board.
                        self.factory.circleFactory(self.window, event, self.forms)
                        # Add cpu pawns on the board.
                        self.factory.cpuCircleFactory(self.window, self.forms)
                        # Add transparent paws on squares without pawns to move them.
                        self.factory.transparentCircles(Factory.circles, Factory.circles_cpu, self.forms, self.window)
                        # Change the phase of the game.
                        if(len(Factory.circles) == 3 and len(Factory.circles_cpu) == 3) :
                            
                            self.game_status = GameStatus.phase_2.value
                    
                    # If the key associated to the id of the pawn's square is pressed, we can move it.
                    for circle in Factory.circles :
                        
                        if event.key == (circle.square.id + 48) :
                            
                            circle.canMove = True
                            print(circle.square.id + 48)
                    
                    # move squares without pawns.
                    for circle in Factory.squares_without_circle :
                        
                        if event.key == (circle.square.id + 48) :
                            
                            circle.canMove = True
                            print(circle.square.id + 48)
                    
                    # move cpu pawns.
                    for circle in Factory.circles_cpu :
                        
                        if event.key == (circle.square.id + 48) :
                            
                            circle.canMove = True
                            print(circle.square.id + 48)
                    
                    # To move two pawns at the same time.
                    for circle in Factory.circles :
                        
                        if event.key == pygame.K_d :
                            
                            circle.canMove = True
                            print(event.key)
                    #
                    for circle in Factory.squares_without_circle :
                        
                        if event.key == pygame.K_d :
                            
                            circle.canMove = True
                            print(event.key)
                    #
                    for circle in Factory.circles_cpu :
                        
                        if event.key == pygame.K_d :
                            
                            circle.canMove = True
                            print(event.key)
                    
                    # If the key 'm' is pressed we can move a pawn to an another square.
                    # User pawns
                    for circle in Factory.circles :
                        
                        if keys[pygame.K_m] and keys[circle.square.id + 48]  :
                            
                            circle.changeSquare(Factory.squares_without_circle, event.key - 48)
                            self.factory.transparentCircles(Factory.circles, Factory.circles_cpu, self.forms, self.window)
                    
                    # Cpu pawns
                    for circle in Factory.circles_cpu :
                        
                        if keys[pygame.K_m] and keys[circle.square.id + 48]  :
                            
                            circle.changeSquare(Factory.squares_without_circle, event.key - 48)
                            self.factory.transparentCircles(Factory.circles, Factory.circles_cpu, self.forms, self.window)
                    
                    # Give the turn to the cpu (MinMax AI play).
                    if(self.game_status == GameStatus.phase_2.value and event.key == pygame.K_RETURN) :
                        
                        Turn.setTurn(1)
                        MinMax.minmax(Factory.circles_cpu, Factory.circles, Factory.squares_without_circle, self.window.getScreenWidth() / 2, self.window.getScreenHeight() / 2, self.factory, self.forms, self.window)
                
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
                    for circle in Factory.squares_without_circle :
                        
                        if event.key == circle.square.id + 48 :
                            
                            circle.canMove = False
                            print(f"False - {circle.square.id + 48}")
                        
                        else :
                            
                            circle.canMove = False
                    
                    # can't move cpu pawns.
                    for circle in Factory.circles_cpu :
                        
                        if event.key == circle.square.id + 48 :
                            
                            circle.canMove = False
                            print(f"False - {circle.square.id + 48}")
                        
                        else :
                            
                            circle.canMove = False
                    
                    # Give the turn to the player.
                    if(self.game_status == GameStatus.phase_2.value and event.key == pygame.K_RETURN) :
                        
                        Turn.setTurn(0)
                        print("nouveau tour : ", Turn.getTurn())
            
            # Mode 2 : CPU_1 vs CPU_2.
            elif self.configs[3] == "2" and self.window.getView() == View.GAME.value :
                
                self.factory.cpu1CircleFactory(self.window, self.forms)
                self.factory.cpu2CircleFactory(self.window, self.forms)
                self.factory.transparentCircles(Factory.circles, Factory.circles_cpu, self.forms, self.window)
                
                if(len(Factory.circles) == 3 and len(Factory.circles_cpu) == 3) :
                    
                    self.game_status = GameStatus.phase_2.value
            
            # Buttons click management
            for button in buttons :
                
                if(event.type == pygame.MOUSEBUTTONDOWN) :
                    
                    # Launch the game view.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.PLAY.value) :
                        
                        Factory.circles = []
                        Factory.circles_cpu = []
                        self.window.setView(View.GAME.value)
                    
                    # Restart the game.
                    if (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.RESTART.value) :
                        
                        self.restartGame(View.GAME.value)
                    
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
                    
                    # Back to the welcome view.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.BACK.value) :
                        
                        self.restartGame(View.WELCOME.value)
                    
                    # Close the window and quit the game.
                    elif (button.checkPosition(pygame.mouse.get_pos()) and button.text_input == ButtonAction.QUIT.value) :
                        
                        # Reset the turn.
                        Config.changeTurn(0)
                        self.quit()
    
    def welcome(self, buttons:list[Button]) :
        
        self.window.welcomeView(buttons)
        self.window.displayTextOnTheView("Infos ", 17, (self.window.getScreenWidth() / 1.5, self.window.getScreenHeight() / 20))
        
        if self.configs[3] == "1" :
            
            color_player = "VERT" if self.configs[1] == "GREEN" else "ROUGE"
            color_cpu = "ROUGE" if self.configs[2] == "RED" else "VERT"
            self.window.displayTextOnTheView("Mode actuel : Joueur vs CPU", 17, (self.window.getScreenWidth() / 1.5, self.window.getScreenHeight() / 10))
            self.window.displayTextOnTheView(f"Couleur {self.configs[0]} : {color_player}", 17, (self.window.getScreenWidth() / 1.5, (self.window.getScreenHeight() / 10) + 50))
            self.window.displayTextOnTheView(f"Couleur CPU : {color_cpu}", 17, (self.window.getScreenWidth() / 1.5, (self.window.getScreenHeight() / 10) + 100))
        
        elif self.configs[3] == "2" :
            
            color_cpu_1 = "VERT" if self.configs[1] == "GREEN" else "ROUGE"
            color_cpu_2 = "ROUGE" if self.configs[2] == "RED" else "VERT"
            self.window.displayTextOnTheView("Mode actuel : CPU_1 vs CPU_2", 17, (self.window.getScreenWidth() / 1.5, self.window.getScreenHeight() / 10))
            self.window.displayTextOnTheView(f"Couleur CPU_1 : {color_cpu_1}", 17, (self.window.getScreenWidth() / 1.5, (self.window.getScreenHeight() / 10) + 50))
            self.window.displayTextOnTheView(f"Couleur CPU_2 : {color_cpu_2}", 17, (self.window.getScreenWidth() / 1.5, (self.window.getScreenHeight() / 10) + 100))
        
        if self.configs[4] == "ON" :
            
            self.window.displayTextOnTheView(f"Musique : activé", 17, (self.window.getScreenWidth() / 1.5, (self.window.getScreenHeight() / 10) + 150))
        
        elif self.configs[4] == "OFF" :
            
            self.window.displayTextOnTheView(f"Musique : désactivé", 17, (self.window.getScreenWidth() / 1.5, (self.window.getScreenHeight() / 10) + 150))
        
        pygame.display.flip()
        pygame.display.update()
    
    def game(self, forms:list[Square], buttons:list[Button]) :
        
        self.window.gameView(buttons)
        
        # Mode 1 : Player vs CPU.
        if self.configs[3] == "1" :
            
            # Draw the board.
            for form in forms :
                
                form.drawSprite()
                # form.move()
            
            # Put pawns on the board.
            for circle in Factory.circles :
                
                circle.drawSprite()
                if self.game_status == GameStatus.phase_2.value and circle.canMove and not self.getAwinner :
                    
                    circle.move()
            
            for circle in Factory.circles_cpu :
                
                circle.drawSprite()
                if self.game_status == GameStatus.phase_2.value and not self.getAwinner :
                    
                    circle.move()
            
            for circle in Factory.squares_without_circle :
                
                if self.game_status == GameStatus.phase_2.value and circle.canMove and not self.getAwinner :
                    
                    circle.move()
            
            # Check the winner of the game.
            winner = CheckWinner.checkPlayerVsAiWinner(Factory.circles, Factory.circles_cpu)
            
            if winner == "player" :
                
                self.window.displayTextOnTheView(f"{self.configs[0]} a gagné", 15, (self.window.screen_width / 4, self.window.screen_height / 2))
                self.stopGame()
            
            elif winner == "cpu" :
                
                self.window.displayTextOnTheView("CPU a gagné", 15, (self.window.screen_width / 1.35, self.window.screen_height / 2))
                self.stopGame()
        
        # Mode 2 : CPU_1 vs CPU_2.
        elif self.configs[3] == "2" :
            
            # Draw the board.
            for form in forms :
                
                form.drawSprite()
            
            # Put pawns on the board.
            for circle in Factory.circles :
                
                circle.drawSprite()
            
            for circle in Factory.circles_cpu :
                
                circle.drawSprite()
            
            for circle in Factory.squares_without_circle :
                
                circle.move()
            
            if(self.game_status == GameStatus.phase_2.value) :
                
                self.window.clock.tick(10)
                
                if Turn.getTurn() == 0 :
                    
                    MinMax.minmax1(Factory.circles, Factory.circles_cpu, Factory.squares_without_circle, self.window.getScreenWidth() / 2, self.window.getScreenHeight() / 2, self.getAwinner, self.factory, self.forms, self.window)
                    Turn.setTurn(1)
                
                if Turn.getTurn() == 1 :
                    
                    MinMax.minmax2(Factory.circles_cpu, Factory.circles, Factory.squares_without_circle, self.window.getScreenWidth() / 2, self.window.getScreenHeight() / 2, self.getAwinner, self.factory, self.forms, self.window)
                    Turn.setTurn(0)
            
            # Check the winner of the game.
            winner = CheckWinner.checkAiVsAiWinner(Factory.circles, Factory.circles_cpu)
            
            if winner == "cpu_1" :
                
                self.window.displayTextOnTheView("CPU_1 a gagné", 15, (self.window.screen_width / 4, self.window.screen_height / 2))
                self.stopGame()
            
            elif winner == "cpu_2" :
                
                self.window.displayTextOnTheView("CPU_2 a gagné", 15, (self.window.screen_width / 1.35, self.window.screen_height / 2))
                self.stopGame()
        
        pygame.display.flip()
    
    def options(self, buttons:list[Button], text_input:TextInputVisualizer) :
        
        self.window.optionsView(buttons, text_input)
        pygame.display.flip()
        pygame.display.update()
    
    def credits(self, buttons:list[Button]) : 
        
        self.window.creditsView(buttons)
        pygame.display.flip()
        pygame.display.update()
    
    def restartGame(self, view:View) :
        
        system("cls")
        Square.empty_square_id = 4
        Factory.circles = []
        Factory.circles_cpu = []
        Factory.squares_without_circle = []
        self.forms = []
        self.forms = self.factory.formFactory(self.window)
        self.window.setView(view)
        self.buttons = self.factory.buttonFactory(self.window, view)
        self.game_status = GameStatus.phase_1.value
        self.getAwinner = False
        Turn.setTurn(0)
        self.game(self.forms, self.buttons)
    
    def stopGame(self) :
        
        for circle in Factory.circles :
            
            circle.canMove = False
        
        for circle in Factory.circles_cpu :
            
            circle.canMove = False
        
        for circle in Factory.squares_without_circle :
            
            circle.canMove = False
        
        self.getAwinner = True
        self.window.clock.tick(60)
    
    # Close the window and quit the program
    def quit(self):
        
        Config.changeTurn(0)
        self.running == False
        pygame.quit()
        exit()
