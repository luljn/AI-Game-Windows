#The factory of the programm
import pygame

from model.button import *
from model.buttonAction import ButtonAction
from model.config import Config
from model.circle import Circle
from model.font import *
from model.square import Square

from view.view import View



class Factory :
    
    def __init__(self):
        
        super().__init__()
    
    def buttonFactory(self, window, view = "") : 
        
        rect_img_path = "resources\img\\rect.png"
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
        back_button = Button(pygame.image.load(rect_img_path), (window.getScreenWidth() / 1.25, credits_button.position_y + 230), ButtonAction.BACK.value, font, "White", "Blue")
        
        #Return a specific list of buttons, depending on the view we want to display. 
        if view == View.WELCOME.value :
            
            buttons = [start_game_button, options_button, credits_button, quit_button]
        
        elif view == View.OPTIONS.value :
            
            buttons = [green_options_button, red_options_button, player_vs_cpu_options_button,
                        cpu_vs_cpu_options_button, music_on_options_button, music_off_options_button, save_button, back_button]
        
        elif view == View.GAME.value or View.CREDITS.value :
            
            buttons = [back_button]
        
        return buttons
    
    def formFactory(self, window) :
        
        configs = Config.loadConfig()
        forms = []
        #squares dimensions
        square_width = window.getScreenWidth() / 16
        square_height = window.getScreenHeight() / 10
        
        #Position of the 1st square(the central square) => square id 4.
        square_id = 4
        square_position_x = (window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2
        square_position_y = (window.getScreenHeight() / 2) - (window.getScreenHeight() / 10) /2
        
        #Construction of the middle(2nd) line square.
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
        
        #Position of the 4th square(the central square of the 1st line) => square id 1.
        square_id = 1
        square_position_x = (window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2
        square_position_y = ((window.getScreenHeight() / 2) - (window.getScreenHeight() / 10) /2) - ((window.getScreenHeight() / 10) + 10)
        
        #Construction of the 1st line square.
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
        
        #Position of the 7th square(the central square of the 1st line) => square id 1.
        square_id = 7
        square_position_x = (window.getScreenWidth() / 2) -  (window.getScreenWidth() / 16) / 2
        square_position_y = ((window.getScreenHeight() / 2) - (window.getScreenHeight() / 10) /2) + ((window.getScreenHeight() / 10) + 10)
        
        #Construction of the 3rd line square.
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
        
        #Set the right color to the central square(the empty one at the beginning of the game).
        for element in forms :
            
            if element.__class__ == Square and element.getId() == 4:
                
                element.setColor("White")
        
        #Central square position.
        square_ = Square(square_id, window, square_width, square_height,
                        pygame.Vector2(square_position_x , square_position_y))
        
        #Player paws
        # for i in range(3) :
            
        #     circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) + (square_.getWidth() + 10), (window.getScreenHeight() / 2) + (square_.getHeigth() + 10)), configs[1])
            
        #     if i == 1 :
                
        #         circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2), (window.getScreenHeight() / 2) + (square_.getHeigth() + 10)), configs[1])
            
        #     if i == 2 :
                
        #         circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) - (square_.getWidth() + 10), (window.getScreenHeight() / 2) + (square_.getHeigth() + 10)), configs[1])
            
        #     forms.append(circle)
        circle = Circle(window, pygame.Vector2((window.getScreenWidth() / 2), (window.getScreenHeight() / 2) + (square_.getHeigth() + 10)), configs[1], 7)
        forms.append(circle)
        
        #CPU pawns.
        # for i in range(3) :
            
        #     circle1 = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) - (square_.getWidth() + 10), (window.getScreenHeight() / 2) - (square_.getHeigth() + 10)), configs[2])
            
        #     if i == 1 :
                
        #         circle1 = Circle(window, pygame.Vector2((window.getScreenWidth() / 2), (window.getScreenHeight() / 2) - (square_.getHeigth() + 10)), configs[2])
            
        #     if i == 2 :
                
        #         circle1 = Circle(window, pygame.Vector2((window.getScreenWidth() / 2) + (square_.getWidth() + 10), (window.getScreenHeight() / 2) - (square_.getHeigth() + 10)), configs[2])
            
        #     forms.append(circle1)
        
        return forms