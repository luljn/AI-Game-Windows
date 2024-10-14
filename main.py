import pygame


def main() :
    
    pygame.init()
    window = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    
    while running :
        
        for event in pygame.event.get() :
            
            if event.type == pygame.QUIT :
                
                running = False
                
        window.fill("lightblue")
        pygame.display.flip()
        
        clock.tick(60)
        
    pygame.quit()
    
main()