#Configurations management class.



class Config : 
    
    configuration_file_path = "configurations/configs.txt"
    
    @staticmethod
    def loadConfig() :
        
        with open(Config.configuration_file_path, "r") as config_file :
            
            configs = []
            lines = config_file.readlines()
            for line in lines :
                
                # print(line.strip())
                config = line.split('=')
                configs.append(config[1].replace("\n", ""))
            
            print(configs)
            print("\n")
        
        return configs
    
    @staticmethod
    def saveConfigs(lines) :
        
        # pass
        with open(Config.configuration_file_path, "w") as config_file :
            
            config_file.writelines(lines)
    
    @staticmethod
    def changePlayerName(player_name) :
        
        Config.changeConfiguration("PLAYER_NAME", 0, player_name)
    
    @staticmethod
    def changeColor(color) :
        
        Config.changeConfiguration("COLOR", 1, color)
    
    @staticmethod
    def changeCpuColor(color) :
        
        Config.changeConfiguration("CPU_COLOR", 2, color)
    
    @staticmethod
    def changeMode(mode) :
        
        Config.changeConfiguration("MODE", 3, mode)
    
    @staticmethod
    def stopOrEnableMusic(action) : 
        
        Config.changeConfiguration("MUSIC", 4, action)
    
    @staticmethod
    def changeConfiguration(config, line_number, new_config) : 
        
        with open(Config.configuration_file_path, "r") as config_file :
            
            lines = config_file.readlines()
            lines[line_number] = f"{config}={new_config}\n"

        Config.saveConfigs(lines)