# Base class of shapes used in the game.



class Form :
    
    def __init__(self, window, position):
        
        self.window = window
        self.position = position
        
        #Keyboard keys
        self.keys = 0
    
    def move(self) :
        
        pass
    
    def drawSprite(self) :
        
        pass
