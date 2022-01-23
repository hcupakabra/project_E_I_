import pygame
import pygame_menu
import sys
import os
from Characters import *
from level import *
from load_file import load_image
# инициализация pygame
pygame.init()
SIZE = (WIDTH, HEIGHT) = (800, 800)
# задаем базовые константы (переменные, которые не хотим менятьб по PEP8 пишутся большими буквами)
FONT = pygame_menu.font.FONT_8BIT
# задаем сам экран, соответствующего размера
screen = pygame.display.set_mode(SIZE)
# место для групп (будем группировать объекты в игре, чтобы можно было запускать действия сразу для всех в группе)
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

tile_images = {
    'wall': pygame.transform.scale(load_image('level_blocks/main_block.png'), (48, 48)),
    'empty': load_image('level_blocks/background_block.png')
}

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


tiles_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                # new_player = Player(100, 15, 96, 300, player_group, all_sprites)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def startGame():
    clock = pygame.time.Clock()
    # игра - это цикл
    player, level_x, level_y = generate_level(load_level('level.txt'))
    my_player = Player(100, 15, 600, 500, player_group, all_sprites)
    enemy = Enemy(10, 5, 700, 690, enemy_group, all_sprites)
    running = True
    while running:
        # обработка событий
        for event in pygame.event.get():
            # обрабатываем событие нажатия на крестик
            if event.type == pygame.QUIT:
                # завершаем цикл игры
                running = False
        # задаем фон экрана
        screen.fill((0, 0, 0))
        player_group.update()
        enemy_group.update(my_player)
        # визуализация
        all_sprites.draw(screen)
        # замедляем время
        clock.tick(10)
        # обновление
        pygame.display.flip()


menu = pygame_menu.Menu("Minotaur's Labyrinth", 800, 800, theme=pygame_menu.themes.THEME_GREEN)



menu.add.button('Play', startGame)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)