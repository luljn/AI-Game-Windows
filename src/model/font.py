#Font management class
import pygame



class Font :
    
    @staticmethod
    def getFont(size) :
        
        return pygame.font.Font("resources/fonts/font.ttf", size)
