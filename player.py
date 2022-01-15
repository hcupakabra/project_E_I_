import pygame
import pyganim as pyganim
from pygame import *
import Characters

WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
ANIMATION_RIGHT = [
    pygame.image.load('pictures/paint/r1.png'),
    pygame.image.load('pictures/paint/r2.png'),
    pygame.image.load('pictures/paint/r3.png'), ]
ANIMATION_LEFT = [
    pygame.image.load('pictures/paint/l1.png'),
    pygame.image.load('pictures/paint/l2.png'),
    pygame.image.load('pictures/paint/l3.png'), ]
ANIMATION_JUMP_LEFT = [('pictures/paint/l4.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('pictures/paint/r4.png', 0.1)]
ANIMATION_JUMP = [('pictures/paint/j.png', 0.1)]
ANIMATION_STAY = [('pictures/paint/stay.png', 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnimR = []
        for anim in ANIMATION_RIGHT:
            boltAnimR.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnimR)
        self.boltAnimRight.play()
        for anim in ANIMATION_JUMP_RIGHT:
            boltAnimR.append((anim, ANIMATION_DELAY))
        self.boltAnimJumpRight = pyganim.PygAnimation(boltAnimR)
        self.boltAnimJumpRight.play()
        #        Анимация движения влево
        boltAnimL = []
        for anim in ANIMATION_JUMP_LEFT:
            boltAnimL.append((anim, ANIMATION_DELAY))
        self.boltAnimJumpLeft = pyganim.PygAnimation(boltAnimL)
        self.boltAnimJumpLeft.play()
        for anim in ANIMATION_LEFT:
            boltAnimL.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnimL)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

