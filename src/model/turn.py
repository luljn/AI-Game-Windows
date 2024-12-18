# Turn management class.



class Turn :
    
    turn = 0
    
    @staticmethod
    def getTurn() :
        
        return Turn.turn
    
    @staticmethod
    def setTurn(new_turn:int) :
        
        Turn.turn = new_turn
