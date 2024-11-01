#Sound management
import pygame



class Sound :
    
    #Static variable.
    default_music = "resources/sounds/Treachery.mp3"
    
    @staticmethod
    def getAndPlaySound(sound_path) :
        
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(-1)
    
    @staticmethod
    def stopSound() :
        
        pygame.mixer.music.stop()