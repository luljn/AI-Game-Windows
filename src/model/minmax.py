# MinMax management class.
from random import choice

from model.square import Square
from model.turn import Turn



class MinMax : 
    
    @staticmethod
    def minmax(cpu_pawns, player_pawns, squares_without_pawn, position_x, position_y, factory, forms, window) :
        
        circles_id = [] # Id of player pawns.
        circles_cpu_id = [] # Id of cpu pawns.
        squares_without_pawn_id = [] # Id of empty squares.
        
        for circle in player_pawns :
            
            circles_id.append(circle.square.id)
        
        for circle_cpu in cpu_pawns :
            
            circles_cpu_id.append(circle_cpu.square.id)
        
        for circle in squares_without_pawn :
            
            squares_without_pawn_id.append(circle.square.id)
        
        choosen_pawn = choice(circles_cpu_id)
        
        if(len(cpu_pawns) == 3 and len(player_pawns) == 3) :
            
            for pawn in cpu_pawns :
                
                if Turn.getTurn() == 1 and pawn.square.id == choosen_pawn :
                    
                    if (pawn.square.id == Square.empty_square_id - 3) :
                        
                        pawn.canMove = True
                        pawn.moveDown(position_y, pawn.square.getWidth())
                        pawn.canMove = False
                        break
                    
                    elif (pawn.square.id == Square.empty_square_id + 3) :
                        
                        pawn.canMove = True
                        pawn.moveUp(position_y, pawn.square.getWidth())
                        pawn.canMove = False
                        break
                    
                    elif (pawn.square.id == Square.empty_square_id + 1) :
                        
                        pawn.canMove = True
                        pawn.moveLeft(position_x, pawn.square.getWidth() + 10)
                        pawn.canMove = False
                        break
                    
                    elif (pawn.square.id == Square.empty_square_id - 1) :
                        
                        pawn.canMove = True
                        pawn.moveRight(position_x, pawn.square.getWidth() + 10)
                        pawn.canMove = False
                        break
                    
                    else :
                        
                        new_square_id = choice(squares_without_pawn_id)
                        pawn.changeSquare(squares_without_pawn, new_square_id)
                        factory.transparentCircles(player_pawns, cpu_pawns, forms, window)
                        break
    
    @staticmethod
    def minmax1(cpu_pawns, player_pawns, squares_without_pawn, position_x, position_y, getAwinner, factory, forms, window) :
        
        circles_id = [] # Id of player pawns.
        circles_cpu_id = [] # Id of cpu pawns.
        squares_without_pawn_id = [] # Id of empty squares.
        
        for circle in player_pawns :
            
            circles_id.append(circle.square.id)
        
        for circle_cpu in cpu_pawns :
            
            circles_cpu_id.append(circle_cpu.square.id)
        
        for circle in squares_without_pawn :
            
            squares_without_pawn_id.append(circle.square.id)
        
        choosen_pawn = choice(circles_cpu_id)
        
        if(len(cpu_pawns) == 3 and len(player_pawns) == 3) :
            
            for pawn in cpu_pawns :
                
                if Turn.getTurn() == 0 and pawn.square.id == choosen_pawn and not getAwinner :
                    
                    if (pawn.square.id == Square.empty_square_id - 3):
                        
                        pawn.canMove = True
                        pawn.moveDown(position_y, pawn.square.getWidth())
                        pawn.canMove = False
                        return None
                    
                    elif (pawn.square.id == Square.empty_square_id + 3):
                        
                        pawn.canMove = True
                        pawn.moveUp(position_y, pawn.square.getWidth())
                        pawn.canMove = False
                        return None
                    
                    elif (pawn.square.id == Square.empty_square_id + 1):
                        
                        pawn.canMove = True
                        pawn.moveLeft(position_x, pawn.square.getWidth() + 10)
                        pawn.canMove = False
                        return None
                    
                    elif (pawn.square.id == Square.empty_square_id - 1):
                        
                        pawn.canMove = True
                        pawn.moveRight(position_x, pawn.square.getWidth() + 10)
                        pawn.canMove = False
                        return None
                    
                    else : 
                        
                        new_square_id = choice(squares_without_pawn_id)
                        pawn.changeSquare(squares_without_pawn, new_square_id)
                        factory.transparentCircles(player_pawns, cpu_pawns, forms, window)
                        return None
    
    @staticmethod
    def minmax2(cpu_pawns, player_pawns, squares_without_pawn, position_x, position_y, getAwinner, factory, forms, window) :
        
        circles_id = [] # Id of player pawns.
        circles_cpu_id = [] # Id of cpu pawns.
        squares_without_pawn_id = [] # Id of empty squares.
        
        for circle in player_pawns :
            
            circles_id.append(circle.square.id)
        
        for circle_cpu in cpu_pawns :
            
            circles_cpu_id.append(circle_cpu.square.id)
        
        for circle in squares_without_pawn :
            
            squares_without_pawn_id.append(circle.square.id)
        
        choosen_pawn = choice(circles_cpu_id)
        
        if(len(cpu_pawns) == 3 and len(player_pawns) == 3) :
            
            for pawn in cpu_pawns :
                
                if Turn.getTurn() == 1 and pawn.square.id == choosen_pawn and not getAwinner :
                    
                    if (pawn.square.id == Square.empty_square_id - 3):
                        
                        pawn.canMove = True
                        pawn.moveDown(position_y, pawn.square.getWidth())
                        pawn.canMove = False
                        return None
                    
                    elif (pawn.square.id == Square.empty_square_id + 3):
                        
                        pawn.canMove = True
                        pawn.moveUp(position_y, pawn.square.getWidth())
                        pawn.canMove = False
                        return None
                    
                    elif (pawn.square.id == Square.empty_square_id + 1):
                        
                        pawn.canMove = True
                        pawn.moveLeft(position_x, pawn.square.getWidth() + 10)
                        pawn.canMove = False
                        return None
                    
                    elif (pawn.square.id == Square.empty_square_id - 1):
                        
                        pawn.canMove = True
                        pawn.moveRight(position_x, pawn.square.getWidth() + 10)
                        pawn.canMove = False
                        return None
                    
                    else : 
                        
                        new_square_id = choice(squares_without_pawn_id)
                        pawn.changeSquare(squares_without_pawn, new_square_id)
                        factory.transparentCircles(player_pawns, cpu_pawns, forms, window)
                        return None
