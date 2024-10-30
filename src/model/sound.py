#Sound management
import pygame



class Sound :
    
    @staticmethod
    def getAndPlaySound(sound_path) :
        
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(-1)
    
    @staticmethod
    def stopSound() :
        
        pygame.mixer.music.stop()