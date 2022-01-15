import pygame
import pygame_menu

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
    def __init__(self, x, y, images, *groups):
        # добавление в группы
        super(Character, self).__init__(*groups)
        self.index = 0
        self.images = images
        # вешаем картинку на персонажа и границы
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # устанавливаем позицию персонажа по x и y
        self.rect.x, self.rect.y = (x, y)

    # запуск анимации, принимает в себя базу изображений
    def startAnimation(self, base_images):
        self.index += 1
        if self.index >= len(base_images):
            self.index = 0
        self.image = base_images[self.index]

    def update(self):
        # update будет выполняться каждый шаг цикла игры, поэтому здесь все, что должно обновляться
        self.startAnimation(self.images)
        if self.rect.x >= 10:
            self.rect.x = self.rect.x - 10
        else:
            self.rect.x = 315


def startGame():
    # база картинок для дракоши
    images_my_player = [
        pygame.image.load('pictures/paint/r1.png'),
        pygame.image.load('pictures/paint/r2.png'),
        pygame.image.load('pictures/paint/r3.png')
    ]
    # создаем нашего героя, что будет ходить (экземпляр класса Character)
    my_player = Character(315, 150, images_my_player, player_group, all_sprites)
    # часики
    clock = pygame.time.Clock()
    # игра - это цикл
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
        # мы добавили my_player в группу, поэтому он обновится
        all_sprites.update()

        # визуализация
        all_sprites.draw(screen)
        # замедляем время
        clock.tick(10)
        # обновление
        pygame.display.flip()


menu = pygame_menu.Menu("Minotaur's Labyrinth", 500, 500,
                            theme=pygame_menu.themes.THEME_BLUE)


menu.add.button('Play', startGame)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
# import pygame
# import pyganim as pyganim
# from pygame import *
#
# # Объявляем переменные
# WIN_WIDTH = 800  # Ширина создаваемого окна
# WIN_HEIGHT = 640  # Высота
# MOVE_SPEED = 7
# WIDTH = 22
# HEIGHT = 32
# COLOR = "#888888"
# JUMP_POWER = 10
# GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз
# DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
# BACKGROUND_COLOR = "#004400"
# PLATFORM_WIDTH = 32
# PLATFORM_HEIGHT = 32
# PLATFORM_COLOR = "#FF6262"
# PLATFORM_WIDTH = 32
# PLATFORM_HEIGHT = 32
# PLATFORM_COLOR = "#FF6262"
# ANIMATION_DELAY = 0.1 # скорость смены кадров
# ANIMATION_RIGHT = [('игрок/r1.png'),
#                 ('игрок/r2.png'),
#                 ('игрок/r3.png'),]
# ANIMATION_LEFT = [('игрок/l1.png'),
#                 ('игрок/l2.png'),
#                 ('игрок/l3.png')]
# ANIMATION_JUMP_LEFT = [('игрок/l4.png', 0.1)]
# ANIMATION_JUMP_RIGHT = [('игрок/r4.png', 0.1)]
# ANIMATION_JUMP = [('mario/j.png', 0.1)]
# ANIMATION_STAY = [('mario/stay.png', 0.1)]
#
#
# class Platform(sprite.Sprite):
#     def __init__(self, x, y):
#         sprite.Sprite.__init__(self)
#         self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
#         self.image = image.load("pictures/tile4.png")
#         self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
#
#
# class Player(sprite.Sprite):
#     def __init__(self, x, y):
#         self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
#         #        Анимация движения вправо
#         boltAnim = []
#         for anim in ANIMATION_LEFT:
#             boltAnim.append((anim, ANIMATION_DELAY))
#         for anim in ANIMATION_RIGHT:
#             boltAnim.append((anim, ANIMATION_DELAY))
#         self.boltAnimRight = pyganim.PygAnimation(boltAnim)
#         self.boltAnimRight.play()
#         #        Анимация движения влево
#         boltAnim = []
#         for anim in ANIMATION_LEFT:
#             boltAnim.append((anim, ANIMATION_DELAY))
#         self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
#         self.boltAnimLeft.play()
#
#         self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
#         self.boltAnimStay.play()
#         self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим
#
#         self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
#         self.boltAnimJumpLeft.play()
#
#         self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
#         self.boltAnimJumpRight.play()
#
#         self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
#         self.boltAnimJump.play()
#
#         self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
#         self.boltAnimJump.play()
#         self.yvel = 0  # скорость вертикального перемещения
#         self.onGround = False  # На земле ли я?
#         sprite.Sprite.__init__(self)
#         self.xvel = 0  # скорость перемещения. 0 - стоять на месте
#         self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
#         self.startY = y
#         self.image = Surface((WIDTH, HEIGHT))
#         self.image.fill(Color(COLOR))
#         self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
#
#     def update(self, left, right, up, platforms):
#         if up:
#             if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
#                 self.yvel = -JUMP_POWER
#             self.image.fill(Color(COLOR))
#             self.boltAnimJump.blit(self.image, (0, 0))
#
#         if left:
#             self.xvel = -MOVE_SPEED  # Лево = x- n
#             self.image.fill(Color(COLOR))
#             if up:  # для прыжка влево есть отдельная анимация
#                 self.boltAnimJumpLeft.blit(self.image, (0, 0))
#             else:
#                 self.boltAnimLeft.blit(self.image, (0, 0))
#
#         if right:
#             self.xvel = MOVE_SPEED  # Право = x + n
#             self.image.fill(Color(COLOR))
#             if up:
#                 self.boltAnimJumpRight.blit(self.image, (0, 0))
#             else:
#                 self.boltAnimRight.blit(self.image, (0, 0))
#         if not (left or right):  # стоим, когда нет указаний идти
#             self.xvel = 0
#             if not up:
#                 self.image.fill(Color(COLOR))
#                 self.boltAnimStay.blit(self.image, (0, 0))
#
#         self.onGround = False;  # Мы не знаем, когда мы на земле((
#         self.rect.y += self.yvel
#         self.collide(0, self.yvel, platforms)
#
#         self.rect.x += self.xvel  # переносим свои положение на xvel
#         self.collide(self.xvel, 0, platforms)
#
#     def collide(self, xvel, yvel, platforms):
#         for p in platforms:
#             if sprite.collide_rect(self, p): # если есть пересечение платформы с игроком
#
#                 if xvel > 0:                      # если движется вправо
#                     self.rect.right = p.rect.left # то не движется вправо
#
#                 if xvel < 0:                      # если движется влево
#                     self.rect.left = p.rect.right # то не движется влево
#
#                 if yvel > 0:                      # если падает вниз
#                     self.rect.bottom = p.rect.top # то не падает вниз
#                     self.onGround = True          # и становится на что-то твердое
#                     self.yvel = 0                 # и энергия падения пропадает
#
#                 if yvel < 0:                      # если движется вверх
#                     self.rect.top = p.rect.bottom # то не движется вверх
#                     self.yvel = 0                 # и энергия прыжка пропадает
#
#
# def main():
#     pygame.init()  # Инициация PyGame, обязательная строчка
#     screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
#     pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
#
#     hero = Player(55, 55)  # создаем героя по (x,y) координатам
#     left = right = False  # по умолчанию — стоим
#     up = False
#     bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
#     # будем использовать как фон
#     bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
#     timer = pygame.time.Clock()
#     entities = pygame.sprite.Group()  # Все объекты
#     platforms = []  # то, во что мы будем врезаться или опираться
#     entities.add(hero)
#     level = ["-------------------------",
#              "-                       -",
#              "-                       -",
#              "-                       -",
#              "-            --         -",
#              "-                       -",
#              "--                      -",
#              "-                       -",
#              "-                   --- -",
#              "-                       -",
#              "-                       -",
#              "-      ---              -",
#              "-                       -",
#              "-   -----------         -",
#              "-                       -",
#              "-                -      -",
#              "-                   --  -",
#              "-                       -",
#              "-                       -",
#              "-------------------------"]
#
#     while 1:  # Основной цикл программы
#         timer.tick(60)
#         for e in pygame.event.get():  # Обрабатываем события
#             if e.type == KEYDOWN and e.key == K_UP:
#                 up = True
#
#             if e.type == KEYUP and e.key == K_UP:
#                 up = False
#             if e.type == KEYDOWN and e.key == K_LEFT:
#                 left = True
#             if e.type == KEYDOWN and e.key == K_RIGHT:
#                 right = True
#
#             if e.type == KEYUP and e.key == K_RIGHT:
#                 right = False
#             if e.type == KEYUP and e.key == K_LEFT:
#                 left = False
#             if e.type == QUIT:
#                 raise SystemExit("QUIT")
#         x = y = 0  # координаты
#         for row in level:  # вся строка
#             for col in row:  # каждый символ
#                 if col == "-":
#                     pf = Platform(x, y)
#                     entities.add(pf)
#                     platforms.append(pf)
#                 elif col == " ":
#                     pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
#                     pf.fill(Color(BACKGROUND_COLOR))
#                     screen.blit(pf, (x, y))
#
#                 x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
#             y += PLATFORM_HEIGHT  # то же самое и с высотой
#             x = 0  # на каждой новой строчке начинаем с нуля
#         # screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
#         hero.update(left, right, up, platforms)   # передвижение
#         entities.draw(screen) # отображение всего
#         pygame.display.update()  # обновление и вывод всех изменений на экран
#
#
# if __name__ == "__main__":
#     main()

