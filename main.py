import sys
import pygame 
from constants import *
from asteroid import Asteroid
from player import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids_group, drawable_group, updatable_group)
    AsteroidField.containers = (updatable_group)
    Player.containers = (updatable_group, drawable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)

    asteroidfield = AsteroidField()
    player = Player(x, y)    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for updatable in updatable_group:
            updatable.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit(0)

        for asteroid in asteroids_group:
            for shot in shot_group:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for drawable in drawable_group:
            drawable.draw(screen)
        
        dt = clock.tick(60) / 1000

        pygame.display.flip()
if __name__ == "__main__":
    main()