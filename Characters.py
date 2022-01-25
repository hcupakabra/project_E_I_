import pygame
import pygame_menu

import load_file
from load_file import *
# инициализация pygame
pygame.init()

# задаем базовые константы (переменные, которые не хотим менятьб по PEP8 пишутся большими буквами)
vec = pygame.math.Vector2
SIZE = (WIDTH, HEIGHT) = (500, 500)
FONT = pygame_menu.font.FONT_8BIT
ACC = 0.1
FRIC = -0.12

# задаем сам экран, соответствующего размера
screen = pygame.display.set_mode(SIZE)

# место для групп (будем группировать объекты в игре, чтобы можно было запускать действия сразу для всех в группе)
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()


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
    def __init__(self, hp, dmg, x, y, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.MOVE_SPEED = 7
        self.JUMP_POWER = 10
        self.image = load_file.animation_STAY_Player[self.index]
        self.w = 100
        self.rect = x, y = 600, 500
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0.5)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.MOVE_SPEED
            self.startAnimation(load_file.animation_LGUN_Player)
            if key[pygame.K_1]:
                self.startAnimation(load_file.animation_ATLGUN_Player)
            if key[pygame.K_UP]:
                self.rect.y -= self.MOVE_SPEED
                self.startAnimation(load_file.animation_LUP_Player)
            if key[pygame.K_DOWN]:
                self.rect.y += self.MOVE_SPEED
                self.startAnimation(load_file.animation_LDOWN_Player)
        elif key[pygame.K_RIGHT]:
            self.rect.x += self.MOVE_SPEED
            self.startAnimation(load_file.animation_RGUN_Player)
            if key[pygame.K_1]:
                self.startAnimation(load_file.animation_ATRGUN_Player)
            if key[pygame.K_UP]:
                self.rect.y -= self.MOVE_SPEED
                self.startAnimation(load_file.animation_RUP_Player)
            if key[pygame.K_DOWN]:
                self.rect.y += self.MOVE_SPEED
                self.startAnimation(load_file.animation_RDOWN_Player)
        elif key[pygame.K_UP]:
            self.rect.y -= self.MOVE_SPEED
            self.startAnimation(load_file.animation_UP_Player)
        elif key[pygame.K_DOWN]:
            self.rect.y += self.MOVE_SPEED
            self.startAnimation(load_file.animation_DOWN_Player)
        else:
            self.startAnimation(load_file.animation_STAY_Player)
            if key[pygame.K_1]:
                self.startAnimation(load_file.animation_SGUN_Player)

        self.acc.x = self.vel.x
        self.vel = self.acc
        self.rect += self.vel


class Enemy(Character):
    def __init__(self, hp, dmg, x, y, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.movement_speed = 7
        self.distance_to_player = 50
        self.image = load_file.animation_IDLE_ENEMY[self.index]
        self.w = 192

    def update(self, player):
        # print("P", player.rect.x - player.w)
        # print("S", self.rect.x - self.w)
        if self.rect.x - player.rect.x > self.distance_to_player:
            self.startAnimation(load_file.animation_IDLE_ENEMY)
        elif player.rect.x - self.rect.x <= self.distance_to_player:
            self.startAnimation(load_file.animation_LEFT_ENEMY)
            self.rect.x -= self.movement_speed
        elif (player.rect.x - player.w) + (self.rect.x - self.w) >= 68:
            self.startAnimation(load_file.animation_ATTACK_ENEMY)
