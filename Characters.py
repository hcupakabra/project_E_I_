import pygame
import pygame_menu
import sys
import os
# инициализация pygame
pygame.init()

# задаем базовые константы (переменные, которые не хотим менятьб по PEP8 пишутся большими буквами)
SIZE = (WIDTH, HEIGHT) = (500, 500)
FONT = pygame_menu.font.FONT_8BIT

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


class Player(Character):
    ANIMATION_RIGHT = [
        pygame.transform.scale(load_image('player/r1.png', colorkey=-1), (100, 100)),
        pygame.transform.scale(load_image('player/r2.png', colorkey=-1), (100, 100)),
        pygame.transform.scale(load_image('player/r3.png', colorkey=-1), (100, 100))]
    ANIMATION_LEFT = [
        pygame.transform.scale(load_image('player/l1.png', colorkey=-1), (100, 100)),
        pygame.transform.scale(load_image('player/l2.png', colorkey=-1), (100, 100)),
        pygame.transform.scale(load_image('player/l3.png', colorkey=-1), (100, 100))]
    ANIMATION_STAY = [pygame.transform.scale(load_image('player/stay.png', colorkey=-1), (100, 100))]

    def __init__(self, hp, dmg, x, y, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.MOVE_SPEED = 7
        self.JUMP_POWER = 10
        self.image = self.ANIMATION_STAY[self.index]
        self.w = 100

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
    animation_ATTACK = [
        load_image("pavuk/attack0.gif", colorkey=-1),
        load_image("pavuk/attack1.gif", colorkey=-1),
        load_image("pavuk/attack2.gif", colorkey=-1),
        load_image("pavuk/attack3.gif", colorkey=-1),
        load_image("pavuk/attack4.gif", colorkey=-1),
        load_image("pavuk/attack5.gif", colorkey=-1),
        load_image("pavuk/attack6.gif", colorkey=-1),
        load_image("pavuk/attack7.gif", colorkey=-1),
        load_image("pavuk/attack8.gif", colorkey=-1),
        load_image("pavuk/attack9.gif", colorkey=-1),
        load_image("pavuk/attack10.gif", colorkey=-1),
        load_image("pavuk/attack11.gif", colorkey=-1),
        load_image("pavuk/attack12.gif", colorkey=-1),
        load_image("pavuk/attack13.gif", colorkey=-1),
        load_image("pavuk/attack14.gif", colorkey=-1),
        load_image("pavuk/attack15.gif", colorkey=-1)
    ]
    animation_DEATH = [
        load_image("pavuk/death0.gif", colorkey=-1),
        load_image("pavuk/death1.gif", colorkey=-1),
        load_image("pavuk/death2.gif", colorkey=-1),
        load_image("pavuk/death3.gif", colorkey=-1),
        load_image("pavuk/death4.gif", colorkey=-1),
        load_image("pavuk/death5.gif", colorkey=-1),
        load_image("pavuk/death6.gif", colorkey=-1),
        load_image("pavuk/death7.gif", colorkey=-1),
        load_image("pavuk/death8.gif", colorkey=-1),
        load_image("pavuk/death9.gif", colorkey=-1),
        load_image("pavuk/death10.gif", colorkey=-1),
        load_image("pavuk/death11.gif", colorkey=-1),
        load_image("pavuk/death12.gif", colorkey=-1),
        load_image("pavuk/death13.gif", colorkey=-1),
        load_image("pavuk/death14.gif", colorkey=-1),
        load_image("pavuk/death15.gif", colorkey=-1),
        load_image("pavuk/death16.gif", colorkey=-1)
    ]

    def __init__(self, hp, dmg, x, y, *groups):
        super().__init__(hp, dmg, x, y, *groups)
        self.movement_speed = 7
        self.distance_to_player = 50
        self.image = self.animation_IDLE[self.index]
        self.w = 192

    def update(self, player):
        # print("P", player.rect.x - player.w)
        # print("S", self.rect.x - self.w)
        if self.rect.x - player.rect.x > self.distance_to_player:
            self.startAnimation(self.animation_IDLE)
        elif player.rect.x - self.rect.x <= self.distance_to_player:
            self.startAnimation(self.animation_LEFT)
            self.rect.x -= self.movement_speed
        elif (player.rect.x - player.w) + (self.rect.x - self.w) >= 68:
            self.startAnimation(self.animation_ATTACK)
