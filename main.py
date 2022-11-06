import pygame
import sys
from player import Player
from settings import *
from game_states import *
from loaded_images import *

pygame.init()
clock = pygame.time.Clock()

# Define the screen surface and set the caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DanneScape")


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
    def draw(self):
        action = False
        # Mouse position
        pos = pygame.mouse.get_pos()

        # Check if mouse collides with button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# Title screen instances
start_button = Button(1455, 790, start_button_img)
title_background = start_img

# Player instances

player_1_sprites = pygame.sprite.GroupSingle()
player_1 = Player(1100, 600, 1100, 250)
player_1_sprites.add(player_1)

player_1_dmg_sprite = pygame.sprite.GroupSingle()
player_1_dmg = Damage_Text(770, 600)
player_1_dmg_sprite.add(player_1_dmg)

player_2_sprites = pygame.sprite.GroupSingle()
player_2 = Player(800, 600, 650, 250, flip=True, anim_offset=True, turn=False)
player_2_sprites.add(player_2)

player_2_dmg_sprite = pygame.sprite.GroupSingle()
player_2_dmg = Damage_Text(1150, 600)
player_2_dmg_sprite.add(player_2_dmg)


class GameState:
    def __init__(self):
        self.state = "title"

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                sys.exit()
        if not player_1.is_dead and not player_2.is_dead:

            if player_1.turn:

                if player_1.attack_value() > player_2.defense_value():
                    dmg = player_1.attack()
                    player_2.update_health(dmg)
                    player_1_dmg.dmg_index = dmg
                    print(f"Player 1 Hit")

                else:
                    dmg = 0
                    player_2.update_health(dmg)
                    player_1_dmg.dmg_index = dmg
                    print("Player 1 Miss")

            if player_2.turn:

                if player_2.attack_value() > player_1.defense_value():
                    dmg = player_2.attack()
                    player_1.update_health(dmg)
                    player_2_dmg.dmg_index = dmg
                    print("Player 2 hit")

                else:
                    dmg = 0
                    player_1.update_health(dmg)
                    player_2_dmg.dmg_index = dmg
                    print("Player 2 miss")

        elif player_1.is_dead:
            pass
        elif player_2.is_dead:
            pass
        screen.fill((80, 80, 80))

        player_1_sprites.draw(screen)
        player_1_sprites.update()

        player_2_sprites.draw(screen)
        player_2_sprites.update()
        if player_1.turn_counter < 2:
            player_1_dmg_sprite.update()
            player_1_dmg_sprite.draw(screen)

        if player_2.turn_counter < 0:
            player_2_dmg_sprite.update()
            player_2_dmg_sprite.draw(screen)

        pygame.display.update()

    def title(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                sys.exit()

        screen.blit(start_img, (0, 0))

        if start_button.draw():
            self.state = "main_game"
        pygame.display.update()

    def state_manager(self):
        if self.state == "title":
            self.title()
        if self.state == "main_game":
            self.main_game()


# Define the game states of the game (Title and game loop)
game_state = GameState()

# Game loop
while True:
    game_state.state_manager()
    clock.tick(FPS)
