import os
import sys
import pygame


# инициализация pygame
# pygame.init()


class Character(pygame.sprite.Sprite):
    def __init__(self, hp, dmg, x, y, *groups):
        # добавление в группы
        super(Character, self).__init__(*groups)
        self.hp = hp
        self.dmg = dmg
        self.index = 0
        self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def startAnimation(self, base_images):
        self.index += 1
        if self.index >= len(base_images):
            self.index = 0
        self.image = base_images[self.index]


class Player(Character):
    def __init__(self, hp, dmg, x, y, images, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.MOVE_SPEED = 7
        self.JUMP_POWER = 10
        print(images[0])
        self.animation_LEFT = images[0]
        self.animation_IDLE = images[1]
        self.animation_RIGHT = images[2]
        self.image = self.animation_IDLE[self.index]

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.MOVE_SPEED
            self.startAnimation(self.animation_LEFT)
        elif key[pygame.K_RIGHT]:
            self.rect.x += self.MOVE_SPEED
            self.startAnimation(self.animation_RIGHT)
        else:
            self.startAnimation(self.animation_IDLE)


class Enemy(Character):
    def __init__(self, hp, dmg, x, y, images, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.MOVE_SPEED = 7
        self.distance_to_player = 50
        self.animation_IDLE = images[0]
        self.animation_LEFT = images[1]
        self.image = self.animation_IDLE[self.index]

    def update(self):
        if self.rect.x > self.distance_to_player:
            self.startAnimation(self.animation_IDLE)
        else:
            self.startAnimation(self.animation_LEFT)
            self.rect.x -= self.MOVE_SPEED
