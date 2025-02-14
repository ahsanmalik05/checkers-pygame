import pygame
from Board import *
from load_assets import *

FPS = 60

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Checkers")
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = Board(self.screen)
        self.turn = 'white'

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.board.select(x, y, self.turn)


    def update(self):
        pass

    def draw(self):
        self.board.draw()
        pygame.display.flip()
