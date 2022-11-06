import pygame
from buffs import *
from items import *
from random import randint
from math import floor
from screen import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, hp_pos_x, hp_pos_y, flip=False, anim_offset=False, turn=True):
        super().__init__()

        # Loads the sprites for the player into a list.
        self.sprites = []

        self.sprites.append(pygame.image.load("sprites/test/cb_1.png").convert_alpha())
        self.sprites.append(pygame.image.load("sprites/test/cb_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("sprites/test/cb_3.png").convert_alpha())
        self.sprites.append(pygame.image.load("sprites/test/cb_4.png").convert_alpha())
        self.sprites.append(pygame.image.load("sprites/test/cb_5.png").convert_alpha())
        if flip:
            flipped_sprites = [pygame.transform.flip(sprite, True, False) for sprite in self.sprites]
            self.sprites = flipped_sprites
        self.anim_off = anim_offset
        self.sprite_index = 0  # Index that keeps track of the index of the list. Which in turn controls what sprite is shown
        if anim_offset:
            self.sprite_index = 2
        self.image = self.sprites[self.sprite_index]
        self.is_animating = True
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]  # Creates the position rectangle for the player with and x and y value

        # Player states

        self.is_dead = False
        self.turn = turn
        self.turn_counter = 0
        self.attack_time = 0
        self.attack_cd = 3000

        # Attributes for the player. Attack, Defense, Strength and Health points
        self.att = 70
        self.defe = 40
        self.stre = 70
        self.hp = 66

        # Items equipped
        self.weapon = dragon_long
        self.head = rune_helmet
        self.chest = rune_body
        self.legs = rune_legs
        self.amulet = ruby_amulet
        self.items_equipped = [self.weapon, self.head, self.chest, self.legs, self.amulet]

        # Boosts (Pots, Prayer, Combat Style)
        self.att_pot = super_attack_potion
        self.def_pot = super_defense_potion
        self.str_pot = super_strength_potion
        self.att_prayer = incredible_reflexes
        self.def_prayer = steel_skin
        self.str_prayer = ultimate_strength
        self.att_style = accurate
        self.def_style = defensive
        self.str_style = aggressive

        # Modifiers
        self.att_modifiers = self.att_pot.multiP + self.att_prayer.value - 1
        self.def_modifiers = self.def_pot.multiP + self.def_prayer.value - 1
        self.str_modifiers = self.str_pot.multiP + self.str_prayer.value - 1

        #  Values for the healthbar
        self.hp_x = hp_pos_x
        self.hp_y = hp_pos_y
        self.current_health = 66
        self.maximum_health = self.hp
        self.health_bar_length = 180
        self.health_ratio = self.maximum_health / self.health_bar_length

        # Function to draw the health bar. First define the color-value. Then set the position with and x and y value.
        # Then set the length and height values.
        # The red bar is drawn first. And then the green one on top. The green bars length is based on the current health
        # and the health ratio which is the maximum health divided by the health bar length.
        # The function will then later be called within the .update function of the class.

    def update_health(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
            self.is_dead = True
            self.is_animating = False

    def basic_health(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.hp_x, self.hp_y, self.health_bar_length, 20))
        pygame.draw.rect(screen, (0, 255, 0), (self.hp_x, self.hp_y, self.current_health / self.health_ratio, 20))

    # Calculates the boosted base stats of att, def and str depending on what modifiers are used (Pots, prayers)
    def boosted_stats(self):
        attack = self.att * self.att_modifiers
        defense = self.defe * self.def_modifiers
        strength = self.stre * self.str_modifiers
        return attack, defense, strength

    # Calculates the defense value based on armor and the defense level of the player
    def defense_value(self):
        att, defe, stre = self.boosted_stats()

        armor = self.head.dp + self.chest.dp + self.legs.dp
        armor_score = 0.0008 * armor ** 3 + 4 * armor + 40

        level = 0.0008 * defe ** 3 + 4 * defe + 40
        def_score = level + 2.5 * armor_score
        roll_defense = randint(0, floor(def_score))
        return roll_defense

    # Calculates the attack value based on weapon and the attack level of the player
    def attack_value(self):
        att, defe, stre = self.boosted_stats()

        weapon = 0.0008 * self.weapon.aim ** 3 + 4 * self.weapon.aim + 40

        level = 0.0008 * att ** 3 + 4 * att + 40
        att_score = level + 2.5 * weapon
        roll_attack = randint(0, floor(att_score))
        return roll_attack

    # Returns the damage output. Ranged from 0-Max hit.
    def attack(self):
        att, defe, stre = self.boosted_stats()
        m_hit = (stre + self.str_style.value + self.amulet.power) * (
                (self.weapon.pow * 0.00175) + 0.1) + 1.05
        damage = randint(0, floor(m_hit))
        return damage

    def cooldown_timer(self):
        if self.turn_counter >= 4 and self.sprite_index >= 3 and not self.anim_off:
            self.turn = True
            self.turn_counter = -2
        elif self.turn_counter >= 2 and self.sprite_index >= 3 and self.anim_off:
            self.turn = True
            self.turn_counter = -4
        else:
            self.turn = False

    # Update method that runs every frame. Based on tick-rating of the clock.
    def update(self):
        self.basic_health()
        self.cooldown_timer()
        if self.is_animating:
            self.sprite_index += 0.18
            if self.sprite_index >= len(self.sprites):
                self.sprite_index = 0
                self.turn_counter += 1
                self.sprites.reverse()

            self.image = self.sprites[int(self.sprite_index)]
