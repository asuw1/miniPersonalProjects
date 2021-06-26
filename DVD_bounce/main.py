import pygame as pg
import os
import math
import random

# Constants for displaying the window
BACKGROUND_COLOR = (20,0,50)
WIDTH = 1000
HEIGHT = 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))
FPS = 144

# Setting caption
pg.display.set_caption('Bouncing DVD Logo')

# DVD constants
DVD_WIDTH = 200
DVD_HEIGHT = 110
DVD_SPRITE = pg.image.load(os.path.join('Assets', 'dvd_logo.png'))
DVD = pg.transform.scale(DVD_SPRITE, (DVD_WIDTH, DVD_HEIGHT))

# Drawing the window
def draw_window(dvd):
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(DVD, (dvd.x, dvd.y))
    pg.display.update()

def main():

    # Setting a Rect object for the DVD logo
    dvd = pg.Rect(math.floor(random.random()*(WIDTH - DVD_WIDTH)), math.floor(random.random()*(HEIGHT - DVD_HEIGHT)), DVD_WIDTH, DVD_HEIGHT)
    clock = pg.time.Clock()
    run = True

    # Setting random intial speed for the logo ranging from -2 to 2
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)

    while run:

        # Moving the DVD logo
        dvd.x += dx
        dvd.y += dy

        # Collision detection
        if dvd.x + dvd.width > WIDTH:
            dx = random.random()+1 * -1
        elif dvd.x <= 0:
            dx = random.random()+1
        if dvd.y + dvd.height > HEIGHT:
            dy = random.random()+1 * -1
        elif dvd.y <= 0:
            dy = random.random()+1

        # Setting FPS cap
        clock.tick(FPS)

        # Quitting check, if so the while loop will stop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        # Calling the draw_window function
        draw_window(dvd)

    # Quitting if while loop breaks
    pg.quit()

if __name__ == "__main__":
    main()
