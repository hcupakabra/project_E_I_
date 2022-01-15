import pygame
from pygame import *
import pygame_menu
COLOR = "#888888"


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
    MOVE_SPEED = 7
    JUMP_POWER = 10
    ANIMATION_LEFT = [
        pygame.transform.scale(pygame.image.load('pictures/paint/r1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/paint/r2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/paint/r3.png'), (100, 100))]
    ANIMATION_LEFT = [
        pygame.transform.scale(pygame.image.load('pictures/paint/l1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/paint/l2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/paint/l3.png'), (100, 100))]
    ANIMATION_JUMP_LEFT = [pygame.transform.scale(pygame.image.load('pictures/paint/l3.png'), (100, 100))]
    ANIMATION_JUMP_RIGHT = [pygame.transform.scale(pygame.image.load('pictures/paint/r4.png'), (100, 100))]
    ANIMATION_JUMP = [pygame.transform.scale(pygame.image.load('pictures/paint/j.png'), (100, 100))]
    ANIMATION_STAY = [pygame.transform.scale(pygame.image.load('pictures/paint/stay.png'), (100, 100))]


class Enemy(Character):
    pass



