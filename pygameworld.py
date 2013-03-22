import sys
import pygame

from settings import DRAW_FACTOR

class PyGameWorld(object):

    def __init__(self, world):
        pygame.init()

        (self.width, self.height) = (DRAW_FACTOR * world.xsize, DRAW_FACTOR * world.ysize + 30)
        self.size = (self.width, self.height)
        self.bg = (100, 100, 100)

        self.screen = pygame.display.set_mode(self.size)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def draw(self, world):
        self.screen.fill(self.bg)
        for p in world.pets:
            self.screen.blit(p.graphic(DRAW_FACTOR), [DRAW_FACTOR * el for el in p.get_pos()])
        # Update stats at bottom of screen

        string = "t: " + str(world.time) +\
                    " pets: " + str(len(world.pets)) +\
                    " avg a: " + str(world.average_age()) +\
                    " avg e: " + str(world.average_energy()) +\
                    " avg h: " + str(world.average_health()) +\
                    " avg c: " + str(world.average_carried())
        font = pygame.font.Font(None, 25)
        text = font.render(string, 1, (255, 255, 255 ))
        
        self.screen.blit(text, (5, DRAW_FACTOR * world.ysize))

        pygame.display.flip()


