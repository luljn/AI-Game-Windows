# check winner controller.

class CheckWinner :
    
    @staticmethod
    def checkPlayerVsAiWinner(player_pawns, cpu_pawns) :
        
        if len(player_pawns) == 3 and len(cpu_pawns) == 3 :
            
            # Player
            # Horizontally
            if player_pawns[0].square.id == 0 and player_pawns[1].square.id == 1 and player_pawns[2].square.id == 2 :
                
                return "player"
            
            elif player_pawns[0].square.id == 3 and player_pawns[1].square.id == 4 and player_pawns[2].square.id == 5 :
                
                return "player"
            
            elif player_pawns[0].square.id == 6 and player_pawns[1].square.id == 7 and player_pawns[2].square.id == 8 :
                
                return "player"
            
            # Vertically
            elif player_pawns[0].square.id == 0 and player_pawns[1].square.id == 3 and player_pawns[2].square.id == 6 :
                
                return "player"
            
            elif player_pawns[0].square.id == 1 and player_pawns[1].square.id == 4 and player_pawns[2].square.id == 7 :
                
                return "player"
            
            elif player_pawns[0].square.id == 2 and player_pawns[1].square.id == 5 and player_pawns[2].square.id == 8 :
                
                return "player"
            
            # Diagonally
            elif player_pawns[0].square.id == 0 and player_pawns[1].square.id == 4 and player_pawns[2].square.id == 8 :
                
                return "player"
            
            elif player_pawns[0].square.id == 2 and player_pawns[1].square.id == 4 and player_pawns[2].square.id == 6 :
                
                return "player"
            
            # CPU
            # Horizontally
            if cpu_pawns[0].square.id == 0 and cpu_pawns[1].square.id == 1 and cpu_pawns[2].square.id == 2 :
                
                return "cpu"
            
            elif cpu_pawns[0].square.id == 3 and cpu_pawns[1].square.id == 4 and cpu_pawns[2].square.id == 5 :
                
                return "cpu"
            
            elif cpu_pawns[0].square.id == 6 and cpu_pawns[1].square.id == 7 and cpu_pawns[2].square.id == 8 :
                
                return "cpu"
            
            # Vertically
            elif cpu_pawns[0].square.id == 0 and cpu_pawns[1].square.id == 3 and cpu_pawns[2].square.id == 6 :
                
                return "cpu"
            
            elif cpu_pawns[0].square.id == 1 and cpu_pawns[1].square.id == 4 and cpu_pawns[2].square.id == 7 :
                
                return "cpu"
            
            elif cpu_pawns[0].square.id == 2 and cpu_pawns[1].square.id == 5 and cpu_pawns[2].square.id == 8 :
                
                return "cpu"
            
            # Diagonally
            elif cpu_pawns[0].square.id == 0 and cpu_pawns[1].square.id == 4 and cpu_pawns[2].square.id == 8 :
                
                return "cpu"
            
            elif cpu_pawns[0].square.id == 2 and cpu_pawns[1].square.id == 4 and cpu_pawns[2].square.id == 6 :
                
                return "cpu"
    
    @staticmethod
    def checkAiVsAiWinner(cpu_1_pawns, cpu_2_pawns) :
        
        if len(cpu_1_pawns) == 3 and len(cpu_2_pawns) == 3 :
            
            # cpu_1
            # Horizontally
            if cpu_1_pawns[0].square.id == 0 and cpu_1_pawns[1].square.id == 1 and cpu_1_pawns[2].square.id == 2 :
                
                return "cpu_1"
            
            elif cpu_1_pawns[0].square.id == 3 and cpu_1_pawns[1].square.id == 4 and cpu_1_pawns[2].square.id == 5 :
                
                return "cpu_1"
            
            elif cpu_1_pawns[0].square.id == 6 and cpu_1_pawns[1].square.id == 7 and cpu_1_pawns[2].square.id == 8 :
                
                return "cpu_1"
            
            # Vertically
            elif cpu_1_pawns[0].square.id == 0 and cpu_1_pawns[1].square.id == 3 and cpu_1_pawns[2].square.id == 6 :
                
                return "cpu_1"
            
            elif cpu_1_pawns[0].square.id == 1 and cpu_1_pawns[1].square.id == 4 and cpu_1_pawns[2].square.id == 7 :
                
                return "cpu_1"
            
            elif cpu_1_pawns[0].square.id == 2 and cpu_1_pawns[1].square.id == 5 and cpu_1_pawns[2].square.id == 8 :
                
                return "cpu_1"
            
            # Diagonally
            elif cpu_1_pawns[0].square.id == 0 and cpu_1_pawns[1].square.id == 4 and cpu_1_pawns[2].square.id == 8 :
                
                return "cpu_1"
            
            elif cpu_1_pawns[0].square.id == 2 and cpu_1_pawns[1].square.id == 4 and cpu_1_pawns[2].square.id == 6 :
                
                return "cpu_1"
            
            # cpu_2
            # Horizontally
            if cpu_2_pawns[0].square.id == 0 and cpu_2_pawns[1].square.id == 1 and cpu_2_pawns[2].square.id == 2 :
                
                return "cpu_2"
            
            elif cpu_2_pawns[0].square.id == 3 and cpu_2_pawns[1].square.id == 4 and cpu_2_pawns[2].square.id == 5 :
                
                return "cpu_2"
            
            elif cpu_2_pawns[0].square.id == 6 and cpu_2_pawns[1].square.id == 7 and cpu_2_pawns[2].square.id == 8 :
                
                return "cpu_2"
            
            # Vertically
            elif cpu_2_pawns[0].square.id == 0 and cpu_2_pawns[1].square.id == 3 and cpu_2_pawns[2].square.id == 6 :
                
                return "cpu_2"
            
            elif cpu_2_pawns[0].square.id == 1 and cpu_2_pawns[1].square.id == 4 and cpu_2_pawns[2].square.id == 7 :
                
                return "cpu_2"
            
            elif cpu_2_pawns[0].square.id == 2 and cpu_2_pawns[1].square.id == 5 and cpu_2_pawns[2].square.id == 8 :
                
                return "cpu_2"
            
            # Diagonally
            elif cpu_2_pawns[0].square.id == 0 and cpu_2_pawns[1].square.id == 4 and cpu_2_pawns[2].square.id == 8 :
                
                return "cpu_2"
            
            elif cpu_2_pawns[0].square.id == 2 and cpu_2_pawns[1].square.id == 4 and cpu_2_pawns[2].square.id == 6 :
                
                return "cpu_2"
