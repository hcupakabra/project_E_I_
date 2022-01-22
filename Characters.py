import pygame
import pygame_menu
from load_file import load_image
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


class Player(Character):
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
