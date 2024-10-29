#Sound management
import pygame



class Sound :
    
    @staticmethod
    def getAndPlaySound(sound_path) :
        
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(-1)