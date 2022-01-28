import pygame
import pygame_menu
import load_file
from load_file import *

# инициализация pygame
pygame.init()

# задаем базовые константы (переменные, которые не хотим менятьб по PEP8 пишутся большими буквами)
SIZE = (WIDTH, HEIGHT) = (500, 500)

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
        self.MOVE_SPEED = 10
        self.image = load_file.animation_STAY_Player[self.index]
        self.w = 100

    def update(self):
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

    def xren(self, enemy):
        if pygame.sprite.collide_rect(self, enemy):
            return True
        else:
            return False


class Enemy(Character):

    def __init__(self, hp, dmg, x, y, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.MOVEMENT_SPEED = 7
        self.distance_to_player_x = 150
        self.ATTACK_DISTANCE = 8
        self.ATTACK_DISTANCE_RIGHT = 20
        self.distance_to_player_y = 50
        self.image = animation_IDLE_LEFT[self.index]
        self.w = 100
        self.h = 100

    def check_collide(self, player):
        self.a = False
        # print(self.hp)
        # print("P:", player.rect.x)
        # print("E:", self.rect.x)
        if player.rect.x < self.rect.x - self.distance_to_player_x and self.hp > 0:
            self.startAnimation(animation_IDLE_LEFT)
        elif (self.rect.x - player.rect.x <= self.distance_to_player_x) and (
                self.rect.x - player.rect.x > self.ATTACK_DISTANCE) and self.hp > 0:
            self.startAnimation(animation_LEFT)
            self.rect.x -= self.MOVEMENT_SPEED
        elif (
                self.rect.x - player.rect.x <= self.ATTACK_DISTANCE) and self.rect.x - player.rect.x >= 0 and self.hp > 0:
            self.startAnimation(animation_ATTACK_LEFT)
        elif (player.rect.x - self.rect.x - player.w <= self.distance_to_player_x) and (
                player.rect.x - self.rect.x - player.w > self.ATTACK_DISTANCE) and self.hp > 0:
            self.startAnimation(animation_RIGHT)
            self.rect.x += self.MOVEMENT_SPEED
        elif player.rect.x - self.rect.x - player.w <= self.ATTACK_DISTANCE + self.w and self.hp > 0:
            self.startAnimation(animation_ATTACK_RIGHT)
        elif self.rect.x < player.rect.x - self.distance_to_player_x and self.hp > 0:
            self.startAnimation(animation_IDLE_RIGHT)
        elif self.hp < 0:
            self.startAnimation(animation_DEATH)
            self.a = True

    def update(self, player, player_group):
        self.check_collide(player)
        self.is_alive()
        # self.cause_damage(player, player_group)

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False