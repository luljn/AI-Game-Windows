# MinMax management class.

class MinMax : 
    
    @staticmethod
    def minmax(cpu_pawns) :
        
        circles_cpu_id = [] # Id of cpu pawns.
        
        for circle_cpu in cpu_pawns :
            
            circles_cpu_id.append(circle_cpu.square.id)
        
        
