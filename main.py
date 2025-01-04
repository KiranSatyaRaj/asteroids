import pygame 
from constants import *
from player import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    player = Player(x, y)
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    updatable_group.add(player)
    drawable_group.add(player)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for updatable in updatable_group:
            updatable.update(dt)

        for drawable in drawable_group:
            drawable.draw(screen)
        
        dt = clock.tick(60) / 1000

        pygame.display.flip()
if __name__ == "__main__":
    main()