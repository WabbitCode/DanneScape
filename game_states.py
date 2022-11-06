import pygame
import sys


class GameState:
    def __init__(self):
        self.state = "main_game"

    def main_game(self, surface):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                sys.exit()
        surface.fill((80, 80, 80))
        pygame.display.update()

    def title(self, surface):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                sys.exit()
        surface.fill((80, 80, 80))
        pygame.display.update()
