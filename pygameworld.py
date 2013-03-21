import sys
import pygame

from settings import DRAW_FACTOR

class PyGameWorld(object):

    def __init__(self, world):
        pygame.init()

        (self.width, self.height) = (DRAW_FACTOR * world.xsize, DRAW_FACTOR * world.ysize)
        self.size = (self.width, self.height)
        self.bg = (100, 100, 100)

        self.screen = pygame.display.set_mode(self.size)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def draw(self, world):
        self.screen.fill(self.bg)
        red_block = pygame.Surface((DRAW_FACTOR, DRAW_FACTOR))
        red_block.fill((200, 0, 0))
        for p in world.pets:
            self.screen.blit(red_block, [DRAW_FACTOR * el for el in p.get_pos()])
        pygame.display.flip()


