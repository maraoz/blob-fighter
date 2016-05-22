import pygame, sys
from pygame.locals import *

from config import *

clock = pygame.time.Clock()

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode(RESOLUTION, 0, 32)
pygame.display.set_caption('Fighting game!')

running = True

pygame.mouse.set_pos(WIDTH/2, HEIGHT/2)

class Player(object):
  def __init__(self, x0, y0, color, left, right, speed):
    self.x = x0
    self.y = y0
    self.color = color
    self.keys = {}
    self.keys['left'] = left
    self.keys['right'] = right
    self.speed = speed

  def move(self, dx, dy):
    self.x = self.x + dx * self.speed
    self.y = self.y + dy

  def draw(self, surface):
    pygame.draw.circle(surface, self.color, (self.x, self.y), 20, 0)

  def control(self, keys):
    dx, dy = 0,0
    if keys[self.keys['left']]:
      dx, dy = -1, 0
    if keys[self.keys['right']]:
      dx, dy = 1, 0
    self.move(dx, dy)

p1 = Player(50, HEIGHT - 30, RED, K_a, K_d, 3)
p2 = Player(WIDTH-50, HEIGHT - 30, BLUE, K_LEFT, K_RIGHT, 5)

# run the game loop
while running:
  clock.tick(FRAMERATE)
  # handle events
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  keys=pygame.key.get_pressed()

  # update game state
  p1.control(keys)
  p2.control(keys)

  # redraw screen
  windowSurface.fill(WHITE)
  p1.draw(windowSurface)
  p2.draw(windowSurface)
  pygame.display.update()















