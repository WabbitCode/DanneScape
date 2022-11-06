import pygame

start_img = pygame.image.load("sprites/misc/login_screen.png")
start_button_img = pygame.image.load("sprites/misc/ok_button.png")


class Damage_Text(pygame.sprite.Sprite):
    def __init__(self, dmg_x, dmg_y):
        super().__init__()

        self.dmg_sprites = []
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/0.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/1.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/2.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/3.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/4.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/5.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/6.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/7.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/8.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/9.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/10.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/11.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/12.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/13.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/14.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/15.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/16.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/17.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/18.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/19.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/20.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/21.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/22.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/23.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/24.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/25.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/26.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/27.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/28.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/29.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/30.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/31.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/32.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/33.png").convert_alpha())
        self.dmg_sprites.append(pygame.image.load("sprites/numbers/34.png").convert_alpha())
        self.dmg_index = 0
        self.image = self.dmg_sprites[self.dmg_index]
        self.rect = self.image.get_rect()
        self.rect.center = [dmg_x, dmg_y]
        self.is_animating = True

        self.x_pos = dmg_x
        self.y_pos = dmg_y

    def update(self):
        self.image = self.dmg_sprites[int(self.dmg_index)]
