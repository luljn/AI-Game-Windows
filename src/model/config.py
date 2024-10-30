#Configurations management class.



class Config : 
    
    @staticmethod
    def loadConfig() :
        
        with open("configurations/configs.txt") as config_file :
            
            lines = config_file.readlines()
            for line in lines :
                
                print(line.strip())
    
    @staticmethod
    def saveConfigs() :
        
        pass