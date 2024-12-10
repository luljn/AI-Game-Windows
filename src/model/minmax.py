# MinMax management class.
from model.config import Config
from model.square import Square

class MinMax : 
    
    @staticmethod
    def minmax(cpu_pawns, player_pawns, position_x, position_y) :
        
        configs = Config.loadConfig()
        
        circles_id = [] # Id of player pawns.
        circles_cpu_id = [] # Id of cpu pawns.
        
        for circle in player_pawns :
            
            circles_id.append(circle.square.id)
        
        for circle_cpu in cpu_pawns :
            
            circles_cpu_id.append(circle_cpu.square.id)
        
        if(len(cpu_pawns) == 3 and len(player_pawns) == 3) :
            
            for pawn in cpu_pawns :
                
                if configs[5] == "1" :
                    
                    if (pawn.square.id == Square.empty_square_id - 3):
                        
                        pawn.canMove = True
                        pawn.moveDown(position_y, pawn.square.getWidth())
                        pawn.canMove = False
                        break
                    
                    elif (pawn.square.id == Square.empty_square_id + 3):
                        
                        pawn.canMove = True
                        pawn.moveUp(position_y, pawn.square.getWidth())
                        pawn.canMove = False
                        break
                    
                    elif (pawn.square.id == Square.empty_square_id - 1):
                        
                        pawn.canMove = True
                        pawn.moveLeft(position_x, pawn.square.getWidth() + 10)
                        pawn.canMove = False
                        break
                    
                    elif (pawn.square.id == Square.empty_square_id + 1):
                        
                        pawn.canMove = True
                        pawn.moveRight(position_x, pawn.square.getWidth() + 10)
                        pawn.canMove = False
                        break
                    
                    Config.changeTurn(0)
