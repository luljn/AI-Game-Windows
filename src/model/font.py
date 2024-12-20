# Font management class.
import pygame



class Font :
    
    @staticmethod
    def getFont(size:int) :
        
        return pygame.font.Font("resources/fonts/font.ttf", size)
