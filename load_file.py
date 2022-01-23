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
    pygame.transform.scale(load_image("pavuk/walk0.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/walk1.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/walk2.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/walk3.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/walk4.png", colorkey=-1), (50, 50))]
animation_IDLE_ENEMY = [
    pygame.transform.scale(load_image("pavuk/idle0.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/idle1.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/idle2.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/idle3.png", colorkey=-1), (50, 50)),]
animation_ATTACK_ENEMY = [
    pygame.transform.scale(load_image("pavuk/attack0.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack1.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack2.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack3.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack4.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack5.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack6.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack7.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack8.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack9.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack10.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack11.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack12.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack13.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack14.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/attack15.png", colorkey=-1), (50, 50))]
animation_DEATH_ENEMY = [
    pygame.transform.scale(load_image("pavuk/death0.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death1.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death2.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death3.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death4.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death5.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death6.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death7.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death8.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death9.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death10.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death11.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death12.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death13.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death14.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death15.png", colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image("pavuk/death16.png", colorkey=-1), (50, 50))]
animation_RIGHT_Player = [
    pygame.transform.scale(load_image('player/r1.png', colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image('player/r2.png', colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image('player/r3.png', colorkey=-1), (50, 50))]
animation_LEFT_Player = [
    pygame.transform.scale(load_image('player/l1.png', colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image('player/l2.png', colorkey=-1), (50, 50)),
    pygame.transform.scale(load_image('player/l3.png', colorkey=-1), (50, 50))]
animation_STAY_Player = [pygame.transform.scale(load_image('player/stay.png', colorkey=-1), (50, 50))]
animation_UP_Player = [pygame.transform.scale(load_image('player/j.png', colorkey=-1), (50, 50))]
animation_RUP_Player = [pygame.transform.scale(load_image('player/rj1.png', colorkey=-1), (50, 50)),
                        pygame.transform.scale(load_image('player/rj2.png', colorkey=-1), (50, 50))]
animation_LUP_Player = [pygame.transform.scale(load_image('player/lj1.png', colorkey=-1), (50, 50)),
                        pygame.transform.scale(load_image('player/lj2.png', colorkey=-1), (50, 50))]

animation_DOWN_Player = [pygame.transform.scale(load_image('player/down.png', colorkey=-1), (50, 50))]
animation_RDOWN_Player = [pygame.transform.scale(load_image('player/rdown.png', colorkey=-1), (50, 50))]
animation_LDOWN_Player = [pygame.transform.scale(load_image('player/ldown.png', colorkey=-1), (50, 50))]
animation_RGUN_Player = [pygame.transform.scale(load_image('player/rgun1.png', colorkey=-1), (50, 50)),
                         pygame.transform.scale(load_image('player/rgun2.png', colorkey=-1), (50, 50)),
                         pygame.transform.scale(load_image('player/rgun3.png', colorkey=-1), (50, 50))]
animation_LGUN_Player = [pygame.transform.scale(load_image('player/lgun1.png', colorkey=-1), (50, 50)),
                         pygame.transform.scale(load_image('player/lgun2.png', colorkey=-1), (50, 50)),
                         pygame.transform.scale(load_image('player/lgun3.png', colorkey=-1), (50, 50))]
animation_SGUN_Player = [pygame.transform.scale(load_image('player/staygun.png', colorkey=-1), (50, 50))]


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
    'wall': pygame.transform.scale(load_image('level_blocks/main_block.png'), (50, 50)),
    'empty': load_image('level_blocks/background_block.png')}
