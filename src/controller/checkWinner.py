# check winner controller.
import numpy as np

class CheckWinner :
    
    @staticmethod
    def checkPlayerVsAiWinner(player_pawns, cpu_pawns) :
        
        if len(player_pawns) == 3 and len(cpu_pawns) == 3 :
            
            circles_id = [] # Id of players pawns.
            circles_cpu_id = [] # Id of cpu pawns.
            
            for circle in player_pawns :
                
                circles_id.append(circle.square.id)
            
            for circle_cpu in cpu_pawns :
                
                circles_cpu_id.append(circle_cpu.square.id)
            
            # Player
            # Horizontally
            if (np.array_equal(circles_id, [0, 1, 2]) or np.array_equal(circles_id, [0, 2, 1]) or np.array_equal(circles_id, [1, 0, 2]) 
                or np.array_equal(circles_id, [1, 2, 0]) or np.array_equal(circles_id, [2, 0, 1]) or np.array_equal(circles_id, [2, 1, 0])):
                
                return "player"
            
            elif (np.array_equal(circles_id, [3, 4, 5]) or np.array_equal(circles_id, [3, 5, 4]) or np.array_equal(circles_id, [4, 3, 5]) 
                or np.array_equal(circles_id, [4, 5, 3]) or np.array_equal(circles_id, [5, 3, 4]) or np.array_equal(circles_id, [5, 4, 3])):
                
                return "player"
            
            elif (np.array_equal(circles_id, [6, 7, 8]) or np.array_equal(circles_id, [6, 8, 7]) or np.array_equal(circles_id, [7, 6, 8]) 
                or np.array_equal(circles_id, [7, 8, 6]) or np.array_equal(circles_id, [8, 6, 7]) or np.array_equal(circles_id, [8, 7, 6])):
                
                return "player"
            
            # Vertically
            elif (np.array_equal(circles_id, [0, 3, 6]) or np.array_equal(circles_id, [0, 6, 3]) or np.array_equal(circles_id, [3, 0, 6]) 
                or np.array_equal(circles_id, [3, 6, 0]) or np.array_equal(circles_id, [6, 0, 3]) or np.array_equal(circles_id, [6, 3, 0])):
                
                return "player"
            
            elif (np.array_equal(circles_id, [1, 4, 7]) or np.array_equal(circles_id, [1, 7, 4]) or np.array_equal(circles_id, [4, 1, 7]) 
                or np.array_equal(circles_id, [4, 7, 1]) or np.array_equal(circles_id, [7, 1, 4]) or np.array_equal(circles_id, [7, 4, 1])):
                
                return "player"
            
            elif (np.array_equal(circles_id, [2, 5, 8]) or np.array_equal(circles_id, [2, 8, 5]) or np.array_equal(circles_id, [5, 2, 8]) 
                or np.array_equal(circles_id, [5, 8, 2]) or np.array_equal(circles_id, [8, 2, 5]) or np.array_equal(circles_id, [8, 5, 2])):
                
                return "player"
            
            # Diagonally
            elif (np.array_equal(circles_id, [0, 4, 8]) or np.array_equal(circles_id, [0, 8, 4]) or np.array_equal(circles_id, [4, 0, 8]) 
                or np.array_equal(circles_id, [4, 8, 0]) or np.array_equal(circles_id, [8, 0, 4]) or np.array_equal(circles_id, [8, 4, 0])):
                
                return "player"
            
            elif (np.array_equal(circles_id, [2, 4, 6]) or np.array_equal(circles_id, [2, 6, 4]) or np.array_equal(circles_id, [4, 2, 6]) 
                or np.array_equal(circles_id, [4, 6, 2]) or np.array_equal(circles_id, [6, 2, 4]) or np.array_equal(circles_id, [6, 4, 2])):
                
                return "player"
            
            # CPU
            # Horizontally
            if (np.array_equal(circles_cpu_id, [0, 1, 2]) or np.array_equal(circles_cpu_id, [0, 2, 1]) or np.array_equal(circles_cpu_id, [1, 0, 2]) 
                or np.array_equal(circles_cpu_id, [1, 2, 0]) or np.array_equal(circles_cpu_id, [2, 0, 1]) or np.array_equal(circles_cpu_id, [2, 1, 0])):
                
                return "cpu"
            
            elif (np.array_equal(circles_cpu_id, [3, 4, 5]) or np.array_equal(circles_cpu_id, [3, 5, 4]) or np.array_equal(circles_cpu_id, [4, 3, 5]) 
                or np.array_equal(circles_cpu_id, [4, 5, 3]) or np.array_equal(circles_cpu_id, [5, 3, 4]) or np.array_equal(circles_cpu_id, [5, 4, 3])):
                
                return "cpu"
            
            elif (np.array_equal(circles_cpu_id, [6, 7, 8]) or np.array_equal(circles_cpu_id, [6, 8, 7]) or np.array_equal(circles_cpu_id, [7, 6, 8]) 
                or np.array_equal(circles_cpu_id, [7, 8, 6]) or np.array_equal(circles_cpu_id, [8, 6, 7]) or np.array_equal(circles_cpu_id, [8, 7, 6])):
                
                return "cpu"
            
            # Vertically
            elif (np.array_equal(circles_cpu_id, [0, 3, 6]) or np.array_equal(circles_cpu_id, [0, 6, 3]) or np.array_equal(circles_cpu_id, [3, 0, 6]) 
                or np.array_equal(circles_cpu_id, [3, 6, 0]) or np.array_equal(circles_cpu_id, [6, 0, 3]) or np.array_equal(circles_cpu_id, [6, 3, 0])):
                
                return "cpu"
            
            elif (np.array_equal(circles_cpu_id, [1, 4, 7]) or np.array_equal(circles_cpu_id, [1, 7, 4]) or np.array_equal(circles_cpu_id, [4, 1, 7]) 
                or np.array_equal(circles_cpu_id, [4, 7, 1]) or np.array_equal(circles_cpu_id, [7, 1, 4]) or np.array_equal(circles_cpu_id, [7, 4, 1])):
                
                return "cpu"
            
            elif (np.array_equal(circles_cpu_id, [2, 5, 8]) or np.array_equal(circles_cpu_id, [2, 8, 5]) or np.array_equal(circles_cpu_id, [5, 2, 8]) 
                or np.array_equal(circles_cpu_id, [5, 8, 2]) or np.array_equal(circles_cpu_id, [8, 2, 5]) or np.array_equal(circles_cpu_id, [8, 5, 2])):
                
                return "cpu"
            
            # Diagonally
            elif (np.array_equal(circles_cpu_id, [0, 4, 8]) or np.array_equal(circles_cpu_id, [0, 8, 4]) or np.array_equal(circles_cpu_id, [4, 0, 8]) 
                or np.array_equal(circles_cpu_id, [4, 8, 0]) or np.array_equal(circles_cpu_id, [8, 0, 4]) or np.array_equal(circles_cpu_id, [8, 4, 0])):
                
                return "cpu"
            
            elif (np.array_equal(circles_cpu_id, [2, 4, 6]) or np.array_equal(circles_cpu_id, [2, 6, 4]) or np.array_equal(circles_cpu_id, [4, 2, 6]) 
                or np.array_equal(circles_cpu_id, [4, 6, 2]) or np.array_equal(circles_cpu_id, [6, 2, 4]) or np.array_equal(circles_cpu_id, [6, 4, 2])):
                
                return "cpu"
    
    @staticmethod
    def checkAiVsAiWinner(cpu_1_pawns, cpu_2_pawns) :
        
        if len(cpu_1_pawns) == 3 and len(cpu_2_pawns) == 3 :
            
            circles_cpu_1_id = [] # Id of players pawns.
            circles_cpu_2_id = [] # Id of cpu pawns.
            
            for circle in cpu_1_pawns :
                
                circles_cpu_1_id.append(circle.square.id)
            
            for circle in cpu_2_pawns :
                
                circles_cpu_2_id.append(circle.square.id)
            
            # cpu_1
            # Horizontally
            if (np.array_equal(circles_cpu_1_id, [0, 1, 2]) or np.array_equal(circles_cpu_1_id, [0, 2, 1]) or np.array_equal(circles_cpu_1_id, [1, 0, 2]) 
                or np.array_equal(circles_cpu_1_id, [1, 2, 0]) or np.array_equal(circles_cpu_1_id, [2, 0, 1]) or np.array_equal(circles_cpu_1_id, [2, 1, 0])):
                
                return "cpu_1"
            
            elif (np.array_equal(circles_cpu_1_id, [3, 4, 5]) or np.array_equal(circles_cpu_1_id, [3, 5, 4]) or np.array_equal(circles_cpu_1_id, [4, 3, 5]) 
                or np.array_equal(circles_cpu_1_id, [4, 5, 3]) or np.array_equal(circles_cpu_1_id, [5, 3, 4]) or np.array_equal(circles_cpu_1_id, [5, 4, 3])):
                
                return "cpu_1"
            
            elif (np.array_equal(circles_cpu_1_id, [6, 7, 8]) or np.array_equal(circles_cpu_1_id, [6, 8, 7]) or np.array_equal(circles_cpu_1_id, [7, 6, 8]) 
                or np.array_equal(circles_cpu_1_id, [7, 8, 6]) or np.array_equal(circles_cpu_1_id, [8, 6, 7]) or np.array_equal(circles_cpu_1_id, [8, 7, 6])):
                
                return "cpu_1"
            
            # Vertically
            elif (np.array_equal(circles_cpu_1_id, [0, 3, 6]) or np.array_equal(circles_cpu_1_id, [0, 6, 3]) or np.array_equal(circles_cpu_1_id, [3, 0, 6]) 
                or np.array_equal(circles_cpu_1_id, [3, 6, 0]) or np.array_equal(circles_cpu_1_id, [6, 0, 3]) or np.array_equal(circles_cpu_1_id, [6, 3, 0])):
                
                return "cpu_1"
            
            elif (np.array_equal(circles_cpu_1_id, [1, 4, 7]) or np.array_equal(circles_cpu_1_id, [1, 7, 4]) or np.array_equal(circles_cpu_1_id, [4, 1, 7]) 
                or np.array_equal(circles_cpu_1_id, [4, 7, 1]) or np.array_equal(circles_cpu_1_id, [7, 1, 4]) or np.array_equal(circles_cpu_1_id, [7, 4, 1])):
                
                return "cpu_1"
            
            elif (np.array_equal(circles_cpu_1_id, [2, 5, 8]) or np.array_equal(circles_cpu_1_id, [2, 8, 5]) or np.array_equal(circles_cpu_1_id, [5, 2, 8]) 
                or np.array_equal(circles_cpu_1_id, [5, 8, 2]) or np.array_equal(circles_cpu_1_id, [8, 2, 5]) or np.array_equal(circles_cpu_1_id, [8, 5, 2])):
                
                return "cpu_1"
            
            # Diagonally
            elif (np.array_equal(circles_cpu_1_id, [0, 4, 8]) or np.array_equal(circles_cpu_1_id, [0, 8, 4]) or np.array_equal(circles_cpu_1_id, [4, 0, 8]) 
                or np.array_equal(circles_cpu_1_id, [4, 8, 0]) or np.array_equal(circles_cpu_1_id, [8, 0, 4]) or np.array_equal(circles_cpu_1_id, [8, 4, 0])):
                
                return "cpu_1"
            
            elif (np.array_equal(circles_cpu_1_id, [2, 4, 6]) or np.array_equal(circles_cpu_1_id, [2, 6, 4]) or np.array_equal(circles_cpu_1_id, [4, 2, 6]) 
                or np.array_equal(circles_cpu_1_id, [4, 6, 2]) or np.array_equal(circles_cpu_1_id, [6, 2, 4]) or np.array_equal(circles_cpu_1_id, [6, 4, 2])):
                
                return "cpu_1"
            
            # cpu_2
            # Horizontally
            if (np.array_equal(circles_cpu_2_id, [0, 1, 2]) or np.array_equal(circles_cpu_2_id, [0, 2, 1]) or np.array_equal(circles_cpu_2_id, [1, 0, 2]) 
                or np.array_equal(circles_cpu_2_id, [1, 2, 0]) or np.array_equal(circles_cpu_2_id, [2, 0, 1]) or np.array_equal(circles_cpu_2_id, [2, 1, 0])):
                
                return "cpu_2"
            
            elif (np.array_equal(circles_cpu_2_id, [3, 4, 5]) or np.array_equal(circles_cpu_2_id, [3, 5, 4]) or np.array_equal(circles_cpu_2_id, [4, 3, 5]) 
                or np.array_equal(circles_cpu_2_id, [4, 5, 3]) or np.array_equal(circles_cpu_2_id, [5, 3, 4]) or np.array_equal(circles_cpu_2_id, [5, 4, 3])):
                
                return "cpu_2"
            
            elif (np.array_equal(circles_cpu_2_id, [6, 7, 8]) or np.array_equal(circles_cpu_2_id, [6, 8, 7]) or np.array_equal(circles_cpu_2_id, [7, 6, 8]) 
                or np.array_equal(circles_cpu_2_id, [7, 8, 6]) or np.array_equal(circles_cpu_2_id, [8, 6, 7]) or np.array_equal(circles_cpu_2_id, [8, 7, 6])):
                
                return "cpu_2"
            
            # Vertically
            elif (np.array_equal(circles_cpu_2_id, [0, 3, 6]) or np.array_equal(circles_cpu_2_id, [0, 6, 3]) or np.array_equal(circles_cpu_2_id, [3, 0, 6]) 
                or np.array_equal(circles_cpu_2_id, [3, 6, 0]) or np.array_equal(circles_cpu_2_id, [6, 0, 3]) or np.array_equal(circles_cpu_2_id, [6, 3, 0])):
                
                return "cpu_2"
            
            elif (np.array_equal(circles_cpu_2_id, [1, 4, 7]) or np.array_equal(circles_cpu_2_id, [1, 7, 4]) or np.array_equal(circles_cpu_2_id, [4, 1, 7]) 
                or np.array_equal(circles_cpu_2_id, [4, 7, 1]) or np.array_equal(circles_cpu_2_id, [7, 1, 4]) or np.array_equal(circles_cpu_2_id, [7, 4, 1])):
                
                return "cpu_2"
            
            elif (np.array_equal(circles_cpu_2_id, [2, 5, 8]) or np.array_equal(circles_cpu_2_id, [2, 8, 5]) or np.array_equal(circles_cpu_2_id, [5, 2, 8]) 
                or np.array_equal(circles_cpu_2_id, [5, 8, 2]) or np.array_equal(circles_cpu_2_id, [8, 2, 5]) or np.array_equal(circles_cpu_2_id, [8, 5, 2])):
                
                return "cpu_2"
            
            # Diagonally
            elif (np.array_equal(circles_cpu_2_id, [0, 4, 8]) or np.array_equal(circles_cpu_2_id, [0, 8, 4]) or np.array_equal(circles_cpu_2_id, [4, 0, 8]) 
                or np.array_equal(circles_cpu_2_id, [4, 8, 0]) or np.array_equal(circles_cpu_2_id, [8, 0, 4]) or np.array_equal(circles_cpu_2_id, [8, 4, 0])):
                
                return "cpu_2"
            
            elif (np.array_equal(circles_cpu_2_id, [2, 4, 6]) or np.array_equal(circles_cpu_2_id, [2, 6, 4]) or np.array_equal(circles_cpu_2_id, [4, 2, 6]) 
                or np.array_equal(circles_cpu_2_id, [4, 6, 2]) or np.array_equal(circles_cpu_2_id, [6, 2, 4]) or np.array_equal(circles_cpu_2_id, [6, 4, 2])):
                
                return "cpu_2"
