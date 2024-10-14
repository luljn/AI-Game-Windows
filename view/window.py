import pygame



class Window :
    
    def __init__(self):
        
        pass
    
    def show(self) :
        
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        
        while running :
            
            for event in pygame.event.get() :
                
                if event.type == pygame.QUIT :
                    
                    running = False
                    
            screen.fill("lightblue")
            pygame.display.flip()
            
            clock.tick(60)
            
        pygame.quit()