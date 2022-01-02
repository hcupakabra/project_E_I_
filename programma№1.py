import pygame
from pygame import *

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Player(sprite.Sprite):
    def __init__(self, x, y):
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right, up):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): # если есть пересечение платформы с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку

    hero = Player(55, 55)  # создаем героя по (x,y) координатам
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
        # screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        hero.update(self, left, right, up, platforms)   # передвижение
        entities.draw(screen) # отображение всего
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()