import pygame



class Window :
    
    def __init__(self):
        
        #pygame initialization
        pygame.init()
        
        #screen dimensions
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        
        #
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        
        #
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.keys = 0
    
    def show(self) :
        
        while self.running :
            
            for event in pygame.event.get() :
                
                if event.type == pygame.QUIT :
                    
                    self.running = False
                    
            self.screen.fill("black")
            self.move()
            pygame.display.flip()
            
            self.dt = self.clock.tick(60) / 1000
            
        self.quit()
        
    def move(self) :
        
        pygame.draw.circle(self.screen, "green", self.player_pos, 40)
        
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP] : 
            
            self.player_pos.y -= 300 * self.dt
        
        if self.keys[pygame.K_DOWN] : 
            
            self.player_pos.y += 300 * self.dt
            
        if self.keys[pygame.K_LEFT] : 
            
            self.player_pos.x -= 300 * self.dt
            
        if self.keys[pygame.K_RIGHT] : 
            
            self.player_pos.x += 300 * self.dt
            
        pygame.display.flip()
            
        self.dt = self.clock.tick(60) / 1000
        
        
    def quit(self):
            
        pygame.quit()