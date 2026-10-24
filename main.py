import pygame
import sys
import random
from logger import log_state
from logger import log_event
from constants import *
from player import *
from asteroidfield import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    timeclock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidfield1 = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawn in drawable:
            drawn.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    log_event("asteroid_shot")
        for asteroid in asteroids:
            if asteroid.collides_with(player1) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()

        dt = timeclock.tick(60) / 1000

if __name__ == "__main__":
    main()
