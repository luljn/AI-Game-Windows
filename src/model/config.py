#Configurations management class.



class Config : 
    
    @staticmethod
    def loadConfig() :
        
        with open("configurations/configs.txt", "r") as config_file :
            
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
    
    @staticmethod
    def changePlayerName(player_name) :
        
        Config.changeConfiguration("PLAYER_NAME", 0, player_name)
    
    @staticmethod
    def changeColor(color) :
        
        Config.changeConfiguration("COLOR", 1, color)
    
    @staticmethod
    def changeMode(mode) :
        
        Config.changeConfiguration("MODE", 2, mode)
    
    @staticmethod
    def stopOrEnableMusic(action) : 
        
        Config.changeConfiguration("MUSIC", 3, action)
    
    @staticmethod
    def changeConfiguration(config, line_number, new_config) : 
        
        with open("configurations/configs.txt", "r") as config_file :
            
            lines = config_file.readlines()
            lines[line_number] = f"{config}={new_config}\n"

        with open("configurations/configs.txt", "w") as config_file :
            
            config_file.writelines(lines)