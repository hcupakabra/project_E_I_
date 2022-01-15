import pygame
from pygame import *
import pygame_menu
COLOR = "#888888"

MOVE_SPEED = 7
JUMP_POWER = 10
ANIMATION_RIGHT = [
    pygame.image.load('pictures/paint/r1.png'),
    pygame.image.load('pictures/paint/r2.png'),
    pygame.image.load('pictures/paint/r3.png'), ]
ANIMATION_LEFT = [
    pygame.image.load('pictures/paint/l1.png'),
    pygame.image.load('pictures/paint/l2.png'),
    pygame.image.load('pictures/paint/l3.png'), ]
ANIMATION_JUMP_LEFT = [('pictures/paint/l4.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('pictures/paint/r4.png', 0.1)]
ANIMATION_JUMP = [('pictures/paint/j.png', 0.1)]
ANIMATION_STAY = [('pictures/paint/stay.png', 0.1)]
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
SIZE = (WIDTH, HEIGHT) = (500, 500)
FONT = pygame_menu.font.FONT_8BIT
screen = pygame.display.set_mode(SIZE)


class Character(pygame.sprite.Sprite):
    def __init__(self, hp, dmg, x, y, images, *groups):
        # добавление в группы
        super(Character, self).__init__(*groups)
        self.hp = hp
        self.dmg = dmg
        self.index = 0
        self.images = images
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)


class Player(Character):
    pass


class Enemy(Character):
    pass



