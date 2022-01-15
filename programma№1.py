import pygame
from pygame import *
import player
import Characters

# у героя должна быть анимка
# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ANIMATION_DELAY = 0.1  # скорость смены кадров
ANIMATION_RIGHT = ['игрок/r1.png',
                   'игрок/r2.png',
                   'игрок/r3.png', ]
ANIMATION_LEFT = ['игрок/l1.png',
                  'игрок/l2.png',
                  'игрок/l3.png']
ANIMATION_JUMP_LEFT = [('игрок/l4.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('игрок/r4.png', 0.1)]
ANIMATION_JUMP = [('mario/j.png', 0.1)]
ANIMATION_STAY = [('mario/stay.png', 0.1)]


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load("pictures/tile4.png")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    hero = player.Player(55, 55)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию — стоим
    up = False
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)
    level = ["-------------------------",
             "-                       -",
             "-                       -",
             "-                       -",
             "-            --         -",
             "-                       -",
             "--                      -",
             "-                       -",
             "-                   --- -",
             "-                       -",
             "-                       -",
             "-      ---              -",
             "-                       -",
             "-   -----------         -",
             "-                       -",
             "-                -      -",
             "-                   --  -",
             "-                       -",
             "-                       -",
             "-------------------------"]

    while 1:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == QUIT:
                raise SystemExit("QUIT")
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == " ":
                    pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(Color(BACKGROUND_COLOR))
                    screen.blit(pf, (x, y))

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля
        pygame.display.update()  # обновление и вывод всех изменений на экран
        # screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        hero.update(left, right, up, platforms)  # передвижение
        entities.draw(screen)  # отображение всего


if __name__ == "__main__":
    main()
