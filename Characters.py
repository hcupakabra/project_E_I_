import os
import sys
import pygame
# инициализация pygame
pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

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
    ANIMATION_RIGHT = [
        pygame.transform.scale(pygame.image.load('pictures/Player/r1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/Player/r2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/Player/r3.png'), (100, 100))]
    ANIMATION_LEFT = [
        pygame.transform.scale(pygame.image.load('pictures/Player/l1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/Player/l2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/Player/l3.png'), (100, 100))]
    ANIMATION_STAY = [pygame.transform.scale(pygame.image.load('pictures/Player/stay.png'), (100, 100))]

    def __init__(self, hp, dmg, x, y, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.MOVE_SPEED = 7
        self.JUMP_POWER = 10
        self.image = self.ANIMATION_STAY[self.index]

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.MOVE_SPEED
            self.startAnimation(self.ANIMATION_LEFT)
        elif key[pygame.K_RIGHT]:
            self.rect.x += self.MOVE_SPEED
            self.startAnimation(self.ANIMATION_RIGHT)
        else:
            self.startAnimation(self.ANIMATION_STAY)


class Enemy(Character):
    animation_LEFT = [
        load_image("pavuk/walk0.gif", colorkey=-1),
        load_image("pavuk/walk1.gif", colorkey=-1),
        load_image("pavuk/walk2.gif", colorkey=-1),
        load_image("pavuk/walk3.gif", colorkey=-1),
        load_image("pavuk/walk4.gif", colorkey=-1)]
    animation_IDLE = [
        load_image("pavuk/idle0.gif", colorkey=-1),
        load_image("pavuk/idle1.gif", colorkey=-1),
        load_image("pavuk/idle2.gif", colorkey=-1),
        load_image("pavuk/idle3.gif", colorkey=-1)]

    def __init__(self, hp, dmg, x, y, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.movement_speed = 7
        self.distance_to_player = 50
        self.image = self.animation_IDLE[self.index]

    def update(self):
        if self.rect.x > self.distance_to_player:
            self.startAnimation(self.animation_IDLE)
        else:
            self.startAnimation(self.animation_LEFT)
            self.rect.x -= self.movement_speed