# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt_var = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player_ship = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                    
        screen.fill("black") 

        for obj in updatable:
            obj.update(dt_var)
           
        for obj in asteroids:
            if obj.check_for_collision(player_ship):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if obj.check_for_collision(bullet):
                    bullet.kill()
                    obj.split()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        delta_time = game_clock.tick(60.0)
        dt_var = delta_time/1000
        

if __name__ == "__main__":
    main()