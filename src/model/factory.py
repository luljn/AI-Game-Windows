# The factory of the program.
import pygame
from random import randint

from model.button import *
from model.buttonAction import ButtonAction
from model.config import Config
from model.circle import Circle
from model.font import *
from model.square import Square

from view.view import View



class Factory :
    
    # List of circles on the gameBoard.
    circles = []
    circles_cpu = []
    squares_without_circle = []
    
    def __init__(self):
        
        super().__init__()
        self.configs = []
    
    def buttonFactory(self, window, view = "") : 
        
        rect_img_path = "resources/img/rect.png"
        position_x = window.getScreenWidth() / 3.05
        font = Font.getFont(25)
        
        start_game_button = Button(pygame.image.load(rect_img_path), (position_x, window.getScreenHeight() / 2.7), ButtonAction.PLAY.value, font, "White", "Blue")
        options_button = Button(pygame.image.load(rect_img_path), (position_x, start_game_button.position_y + 120), ButtonAction.OPTIONS.value, font, "White", "Blue")
        green_options_button = Button(image = None, position = ((window.getScreenWidth() / 3) + 300, window.getScreenHeight() / 2.7), text_input = ButtonAction.GREEN.value, background = font, color_background = "White", color_text = "Green")
        red_options_button = Button(image = None, position = ((window.getScreenWidth() / 3) + 600, window.getScreenHeight() / 2.7), text_input = ButtonAction.RED.value, background = font, color_background = "White", color_text = "Red")
        player_vs_cpu_options_button = Button(image = None, position = ((window.getScreenWidth() / 3) + 250, window.getScreenHeight() / 2), text_input = ButtonAction.PLAYER_VS_CPU.value, background = font, color_background = "White", color_text = "Blue")
        cpu_vs_cpu_options_button = Button(image = None, position = ((window.getScreenWidth() / 3) + 700, window.getScreenHeight() / 2), text_input = ButtonAction.CPU_VS_CPU.value, background = font, color_background = "White", color_text = "Blue")
        music_on_options_button = Button(image = None, position = ((window.getScreenWidth() / 3) + 150, window.getScreenHeight() / 1.5), text_input = ButtonAction.MUSIC_ON.value, background = font, color_background = "White", color_text = "Blue")
        music_off_options_button = Button(image = None, position = ((window.getScreenWidth() / 3) + 400, window.getScreenHeight() / 1.5), text_input = ButtonAction.MUSIC_OFF.value, background = font, color_background = "White", color_text = "Red")
        credits_button = Button(pygame.image.load(rect_img_path), (position_x, options_button.position_y + 120), ButtonAction.CREDITS.value, font, "White", "Blue")
        quit_button = Button(pygame.image.load(rect_img_path), (position_x, credits_button.position_y + 120), ButtonAction.QUIT.value, font, "White", "Blue")
        save_button = Button(pygame.image.load(rect_img_path), (window.getScreenWidth() / 4.75, credits_button.position_y + 230), ButtonAction.SAVE.value, font, "White", "Blue")
        restart_game_button = Button(pygame.image.load(rect_img_path), (window.getScreenWidth() / 4.75, credits_button.position_y + 230), ButtonAction.RESTART.value, font, "White", "Blue")
        back_button = Button(pygame.image.load(rect_img_path), (window.getScreenWidth() / 1.25, credits_button.position_y + 230), ButtonAction.BACK.value, font, "White", "Blue")
        
        # Return a specific list of buttons, depending on the view we want to display. 
        if view == View.WELCOME.value :
            
            buttons = [start_game_button, options_button, credits_button, quit_button]
        
        elif view == View.OPTIONS.value :
            
            buttons = [green_options_button, red_options_button, player_vs_cpu_options_button,
                        cpu_vs_cpu_options_button, music_on_options_button, music_off_options_button, save_button, back_button]
        
        elif view == View.GAME.value :
            
            buttons = [restart_game_button, back_button]
        
        elif view == View.CREDITS.value :
            
            buttons = [back_button]
        
        return buttons
    
    def formFactory(self, window) :
        
        forms = []
        #squares dimensions
        square_width = window.getScreenWidth() / 16
        square_height = window.getScreenHeight() / 10
        
        # Position of the 1st square(the central square) => square id 4.
        square_id = Square.empty_square_id
        square_position_x = (window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2
        square_position_y = (window.getScreenHeight() / 2) - (window.getScreenHeight() / 10) /2
        
        # Construction of the middle(2nd) line square.
        for i in range(3) : 
            
            square = Square(square_id, window, square_width, square_height,
                        pygame.Vector2(square_position_x , square_position_y))
            
            forms.append(square)
            
            if i == 0 :
                
                #square id 3
                square_id = 3
                square_position_x = ((window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2) - ((window.getScreenWidth() / 16) + 10)
            
            if i == 1 :
                
                #square id 5
                square_id = 5
                square_position_x = ((window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2) + ((window.getScreenWidth() / 16) + 10)
        
        # Position of the 4th square(the central square of the 1st line) => square id 1.
        square_id = 1
        square_position_x = (window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2
        square_position_y = ((window.getScreenHeight() / 2) - (window.getScreenHeight() / 10) /2) - ((window.getScreenHeight() / 10) + 10)
        
        # Construction of the 1st line square.
        for i in range(3) : 
            
            square = Square(square_id, window, square_width, square_height,
                        pygame.Vector2(square_position_x , square_position_y))
            
            forms.append(square)
            
            if i == 0 :
                
                #square id 0
                square_id = 0
                square_position_x = ((window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2) - ((window.getScreenWidth() / 16) + 10)
            
            if i == 1 :
                
                #square id 2
                square_id = 2
                square_position_x = ((window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2) + ((window.getScreenWidth() / 16) + 10)
        
        # Position of the 7th square(the central square of the 1st line) => square id 7.
        square_id = 7
        square_position_x = (window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2
        square_position_y = ((window.getScreenHeight() / 2) - (window.getScreenHeight() / 10) /2) + ((window.getScreenHeight() / 10) + 10)
        
        # Construction of the 3rd line square.
        for i in range(3) : 
            
            square = Square(square_id, window, square_width, square_height,
                        pygame.Vector2(square_position_x , square_position_y))
            
            forms.append(square)
            
            if i == 0 :
                
                #square id 6
                square_id = 6
                square_position_x = ((window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2) - ((window.getScreenWidth() / 16) + 10)
            
            if i == 1 :
                
                #square id 8
                square_id = 8
                square_position_x = ((window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2) + ((window.getScreenWidth() / 16) + 10)
        
        # Set the right color to the central square(the empty one at the beginning of the game).
        for element in forms :
            
            if element.__class__ == Square and element.getId() == Square.empty_square_id :
                
                element.setColor("Black")
        
        return forms
    
    def circleFactory(self, window, event, squares) :
        
        self.configs = Config.loadConfig()
        circles_id = [] # Id of players pawns.
        circles_cpu_id = [] # Id of cpu pawns.
        
        for circle in Factory.circles :
            
            circles_id.append(circle.square.id)
        
        for circle_cpu in Factory.circles_cpu :
            
            circles_cpu_id.append(circle_cpu.square.id)
        
        # If the player has less than 3 pawns and it is turn.
        if len(Factory.circles) < 3 and self.configs[5] == "0" : 
            
            for square in squares :
                
                if event.key == pygame.K_0 and square.getId() == 0 and 0 not in circles_id and 0 not in circles_cpu_id :
                    
                    circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) - (square.getWidth() + 10), (window.getScreenHeight() / 2) - (square.getHeigth() + 10)), self.configs[1], square)
                    print(f"0 - PAWN {self.configs[1]}")
                    Factory.circles.append(circle)
                    Config.changeTurn(1)
                    break
                
                elif event.key == pygame.K_1 and square.getId() == 1 and 1 not in circles_id and 1 not in circles_cpu_id :
                    
                    circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2), (window.getScreenHeight() / 2) - (square.getHeigth() + 10)), self.configs[1], square)
                    print(f"1 - PAWN {self.configs[1]}")
                    Factory.circles.append(circle)
                    Config.changeTurn(1)
                    break
                
                elif event.key == pygame.K_2 and square.getId() == 2 and 2 not in circles_id and 2 not in circles_cpu_id :
                    
                    circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) + (square.getWidth() + 10), (window.getScreenHeight() / 2) - (square.getHeigth() + 10)), self.configs[1], square)
                    print(f"2 - PAWN {self.configs[1]}")
                    Factory.circles.append(circle)
                    Config.changeTurn(1)
                    break
                
                elif event.key == pygame.K_3 and square.getId() == 3 and 3 not in circles_id and 3 not in circles_cpu_id :
                    
                    circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) - (square.getWidth() + 10), (window.getScreenHeight() / 2)), self.configs[1], square)
                    print(f"3 - PAWN {self.configs[1]}")
                    Factory.circles.append(circle)
                    Config.changeTurn(1)
                    break
                
                elif event.key == pygame.K_5 and square.getId() == 5 and 5 not in circles_id and 5 not in circles_cpu_id :
                    
                    circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) + (square.getWidth() + 10), (window.getScreenHeight() / 2)), self.configs[1], square)
                    print(f"5 - PAWN {self.configs[1]}")
                    Factory.circles.append(circle)
                    Config.changeTurn(1)
                    break
                
                elif event.key == pygame.K_6 and square.getId() == 6 and 6 not in circles_id and 6 not in circles_cpu_id :
                    
                    circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) - (square.getWidth() + 10), (window.getScreenHeight() / 2) + (square.getHeigth() + 10)), self.configs[1], square)
                    print(f"6 - PAWN {self.configs[1]}")
                    Factory.circles.append(circle)
                    Config.changeTurn(1)
                    break
                
                elif event.key == pygame.K_7 and square.getId() == 7 and 7 not in circles_id and 7 not in circles_cpu_id :
                    
                    circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2), (window.getScreenHeight() / 2) + (square.getHeigth() + 10)), self.configs[1], square)
                    print(f"7 - PAWN {self.configs[1]}")
                    Factory.circles.append(circle)
                    Config.changeTurn(1)
                    break
                
                elif event.key == pygame.K_8 and square.getId() == 8 and 8 not in circles_id and 8 not in circles_cpu_id :
                    
                    circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) + (square.getWidth() + 10), (window.getScreenHeight() / 2) + (square.getHeigth() + 10)), self.configs[1], square)
                    print(f"8 - PAWN {self.configs[1]}")
                    Factory.circles.append(circle)
                    Config.changeTurn(1)
                    break
                
                # To prevent the player to put two pawns on the same squares.
                elif (event.key - 48) in circles_id and (event.key - 48) in circles_cpu_id :
                    
                    pass
                    break
                
                # After the player has put his pawn, the turn goes to cpu
                # Config.changeTurn(1)
    
    def cpuCircleFactory(self, window, squares) :
        
        self.configs = Config.loadConfig()
        position_to_put_pawn = randint(0, 8)
        circles_id = [] # Id of players pawns.
        circles_cpu_id = [] # Id of cpu pawns.
        
        for circle in Factory.circles :
            
            circles_id.append(circle.square.id)
        
        for circle_cpu in Factory.circles_cpu :
            
            circles_cpu_id.append(circle_cpu.square.id)
        
        # If the cpu has less than 3 pawns and it is turn.
        if len(Factory.circles_cpu) < 3 and self.configs[5] == "1" : 
            
            if position_to_put_pawn not in circles_id and position_to_put_pawn not in circles_cpu_id :
                    
                    for square in squares :
                        
                        if (position_to_put_pawn == 0 and square.getId() == 0) :
                            
                            circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) - (square.getWidth() + 10), (window.getScreenHeight() / 2) - (square.getHeigth() + 10)), self.configs[2], square)
                            print(f"0 - CPU_PAWN {self.configs[2]}")
                            Factory.circles_cpu.append(circle)
                            break
                        
                        elif (position_to_put_pawn == 1 and square.getId() == 1) :
                            
                            circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2), (window.getScreenHeight() / 2) - (square.getHeigth() + 10)), self.configs[2], square)
                            print(f"1 - CPU_PAWN {self.configs[2]}")
                            Factory.circles_cpu.append(circle)
                            break
                        
                        elif (position_to_put_pawn == 2 and square.getId() == 2) :
                            
                            circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) + (square.getWidth() + 10), (window.getScreenHeight() / 2) - (square.getHeigth() + 10)), self.configs[2], square)
                            print(f"2 - CPU_PAWN {self.configs[2]}")
                            Factory.circles_cpu.append(circle)
                            break
                        
                        elif (position_to_put_pawn == 3 and square.getId() == 3) :
                            
                            circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) - (square.getWidth() + 10), (window.getScreenHeight() / 2)), self.configs[2], square)
                            print(f"3 - CPU_PAWN {self.configs[2]}")
                            Factory.circles_cpu.append(circle)
                            break
                        
                        elif (position_to_put_pawn == 4 and square.getId() == 4) :
                            
                            self.cpuCircleFactory(window, squares)
                        
                        elif (position_to_put_pawn == 5 and square.getId() == 5) :
                            
                            circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) + (square.getWidth() + 10), (window.getScreenHeight() / 2)), self.configs[2], square)
                            print(f"5 - CPU_PAWN {self.configs[2]}")
                            Factory.circles_cpu.append(circle)
                            break
                        
                        elif (position_to_put_pawn == 6 and square.getId() == 6) :
                            
                            circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) - (square.getWidth() + 10), (window.getScreenHeight() / 2) + (square.getHeigth() + 10)), self.configs[2], square)
                            print(f"6 - CPU_PAWN {self.configs[2]}")
                            Factory.circles_cpu.append(circle)
                            break
                        
                        elif (position_to_put_pawn == 7 and square.getId() == 7) :
                            
                            circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2), (window.getScreenHeight() / 2) + (square.getHeigth() + 10)), self.configs[2], square)
                            print(f"7 - CPU_PAWN {self.configs[2]}")
                            Factory.circles_cpu.append(circle)
                            break
                        
                        elif (position_to_put_pawn == 8 and square.getId() == 8) :
                            
                            circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) + (square.getWidth() + 10), (window.getScreenHeight() / 2) + (square.getHeigth() + 10)), self.configs[2], square)
                            print(f"8 - CPU_PAWN {self.configs[2]}")
                            Factory.circles_cpu.append(circle)
                            break
                    
                    # After the cpu has put his pawn, the turn goes to player
                    Config.changeTurn(0)
            
            else : 
                
                self.cpuCircleFactory(window, squares)
    
    def transparentCircles(self, player_pawns, cpu_pawns, squares, window) :
        
        circles_id = [] # Id of players pawns.
        circles_cpu_id = [] # Id of cpu pawns.
        squares_without_circles_id = [] # Id of squares without pawns.
        
        if (len(player_pawns) == 3 and len(cpu_pawns) == 3) :
            
            for circle in player_pawns :
                
                circles_id.append(circle.square.id)
            
            for circle_cpu in cpu_pawns :
                
                circles_cpu_id.append(circle_cpu.square.id)
            
            if len(Factory.squares_without_circle) != 0 :
                
                for circle in Factory.squares_without_circle :
                    
                    squares_without_circles_id.append(circle.square.id)
        
            for square in squares : 
                
                if (square.id not in circles_id and square.id not in circles_cpu_id 
                    and square.id not in squares_without_circles_id and square.id != Square.empty_square_id) :
                    
                    circle = Circle(window, pygame.Vector2((square.position.x + (square.getWidth() / 2)), (square.position.y + (square.getHeigth() / 2))), "Black", square)
                    Factory.squares_without_circle.append(circle)
                    print(f"{square.id} - Square without pawn !")
