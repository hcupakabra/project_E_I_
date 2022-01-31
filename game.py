import pygame
import pygame_menu
import sys
import os

import Characters
from Characters import *
from level import *
from load_file import *
# инициализация pygame
pygame.init()
SIZE = (WIDTH, HEIGHT) = (800, 800)
FONT = pygame_menu.font.FONT_8BIT
screen = pygame.display.set_mode(SIZE)
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
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
    my_player = Player(100, 20, 100, 700, player_group, all_sprites)
    enemy = Enemy(60, 15, 700, 680, enemy_group, all_sprites)
    running = True
    while running:
        key = pygame.key.get_pressed()
        # обработка событий
        for event in pygame.event.get():
            if Characters.Player.xren(my_player, enemy) and key[pygame.K_1]:
                enemy.hp -= my_player.dmg
                if enemy.hp <= 0:
                    final_menu = pygame_menu.Menu("You're a lazy winner XD", 800, 800, theme=pygame_menu.themes.THEME_GREEN)
                    final_menu.add.button('Quit', pygame_menu.events.EXIT)
                    final_menu.mainloop(screen)
            if Characters.Player.xren(my_player, enemy):
                my_player.hp -= enemy.dmg
                print(my_player.hp)
                if my_player.hp <= 0:
                    final_menu_2 = pygame_menu.Menu("You lose", 800, 800, theme=pygame_menu.themes.THEME_GREEN)
                    final_menu_2.add.button('Quit', pygame_menu.events.EXIT)
                    final_menu_2.mainloop(screen)
            # обрабатываем событие нажатия на крестик
            if event.type == pygame.QUIT:
                # завершаем цикл игры
                running = False
        # задаем фон экрана
        screen.fill((0, 0, 0))
        player_group.update()
        enemy_group.update(my_player, player_group)
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
