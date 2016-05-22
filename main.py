import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
RESOLUTION = (WIDTH, HEIGHT)

# set up the window
windowSurface = pygame.display.set_mode(RESOLUTION, 0, 32)
pygame.display.set_caption('Fighting game!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw a blue circle onto the surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)
    
# draw the window onto the screen
pygame.display.update()


running = True

# run the game loop
while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
