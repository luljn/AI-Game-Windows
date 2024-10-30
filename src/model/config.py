#Configurations management class.



class Config : 
    
    @staticmethod
    def loadConfig() :
        
        with open("configurations/configs.txt") as config_file :
            
            configs = []
            lines = config_file.readlines()
            for line in lines :
                
                print(line.strip())
                config = line.split('=')
                configs.append(config[1].replace("\n", ""))
            
            print(configs)
            print("\n")
    
    @staticmethod
    def saveConfigs() :
        
        pass