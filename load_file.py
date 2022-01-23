import os
import sys
import pygame
pygame.init()
# from pygame import *
SIZE = (WIDTH, HEIGHT) = (500, 500)
screen = pygame.display.set_mode(SIZE)


def load_image(name, colorkey=None):
    fullname = os.path.join("data", name)
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


animation_LEFT_ENEMY = [
    pygame.transform.scale(load_image("pavuk/walk0.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/walk1.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/walk2.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/walk3.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/walk4.gif", colorkey=-1), (100, 100))]
animation_IDLE_ENEMY = [
    pygame.transform.scale(load_image("pavuk/idle0.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/idle1.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/idle2.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/idle3.gif", colorkey=-1), (100, 100)),]
animation_ATTACK_ENEMY = [
    pygame.transform.scale(load_image("pavuk/attack0.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack1.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack2.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack3.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack4.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack5.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack6.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack7.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack8.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack9.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack10.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack11.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack12.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack13.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack14.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/attack15.gif", colorkey=-1), (100, 100))]
animation_DEATH_ENEMY = [
    pygame.transform.scale(load_image("pavuk/death0.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death1.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death2.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death3.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death4.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death5.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death6.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death7.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death8.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death9.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death10.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death11.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death12.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death13.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death14.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death15.gif", colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image("pavuk/death16.gif", colorkey=-1), (100, 100))]
animation_RIGHT_Player = [
    pygame.transform.scale(load_image('player/r1.png', colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image('player/r2.png', colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image('player/r3.png', colorkey=-1), (50, 50))]
animation_LEFT_Player = [
    pygame.transform.scale(load_image('player/l1.png', colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image('player/l2.png', colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image('player/l3.png', colorkey=-1), (50, 50))]
animation_STAY_Player = [pygame.transform.scale(load_image('player/stay.png', colorkey=-1), (50, 50))]


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': pygame.transform.scale(load_image('level_blocks/main_block.png'), (48, 48)),
    'empty': load_image('level_blocks/background_block.png')}
