import os
import pygame
import pygame_menu
import sys
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


def startGame():
    # база картинок для дракоши
    pavuk_walk = [
        load_image("pavuk/walk0.gif", colorkey=-1),
        load_image("pavuk/walk1.gif", colorkey=-1),
        load_image("pavuk/walk2.gif", colorkey=-1),
        load_image("pavuk/walk3.gif", colorkey=-1),
        load_image("pavuk/walk4.gif", colorkey=-1)
    ]
    pavuk_idle = [
        load_image("pavuk/idle0.gif", colorkey=-1),
        load_image("pavuk/idle1.gif", colorkey=-1),
        load_image("pavuk/idle2.gif", colorkey=-1),
        load_image("pavuk/idle3.gif", colorkey=-1)
    ]
    # создаем нашего героя, что будет ходить (экземпляр класса Character)
    my_player = Character(315, 150, pavuk_walk, player_group, all_sprites)
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
        clock.tick(4)
        # обновление
        pygame.display.flip()


menu = pygame_menu.Menu("Minotaur's Labyrinth", 500, 500,
                            theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', startGame)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)

# import pygame
# from pygame import *
# import pygame_menu
# COLOR = "#888888"



