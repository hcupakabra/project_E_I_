import pygame
import pygame_menu
import sys
import os
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
    def __init__(self, hp, dmg, x, y, images, *groups):
        # добавление в группы
        super(Character, self).__init__(*groups)
        self.hp = hp
        self.dmg = dmg
        self.index = 0
        self.images = images
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def startAnimation(self, base_images):
        self.index += 1
        if self.index >= len(base_images):
            self.index = 0
        self.image = base_images[self.index]

    # def stopAnimation(self, base_images):



class Player(Character):
    def __init__(self, hp, dmg, x, y, images, *groups):
        super().__init__(hp, dmg, x, y, images, *groups)
        self.MOVE_SPEED = 7
        self.JUMP_POWER = 10

    # def update(self):
    #     key = pygame.key.get_pressed()
    #     if key[pygame.K_LEFT] and self.rect.x > 0:
    #         self.rect.x -= self.stage_speed
    #     if key[pygame.K_RIGHT] and self.rect.x < WIDTH - self.w:
    #         self.rect.x += self.stage_speed


class Enemy(Character):
    pass


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
    clock = pygame.time.Clock()
    # игра - это цикл
    ANIMATION_LEFT = [
        load_image("pavuk/walk0.gif", colorkey=-1),
        load_image("pavuk/walk1.gif", colorkey=-1),
        load_image("pavuk/walk2.gif", colorkey=-1),
        load_image("pavuk/walk3.gif", colorkey=-1),
        load_image("pavuk/walk4.gif", colorkey=-1)
    ]
    ANIMATION_RIGHT = [
        pygame.transform.flip(ANIMATION_LEFT[0], True, False),
        pygame.transform.flip(ANIMATION_LEFT[1], True, False),
        pygame.transform.flip(ANIMATION_LEFT[2], True, False),
        pygame.transform.flip(ANIMATION_LEFT[3], True, False),
        pygame.transform.flip(ANIMATION_LEFT[4], True, False)
    ]
    my_player = Character(100, 15, 55, 55, ANIMATION_LEFT, all_sprites)
    running = True
    while running:
        # обработка событий
        for event in pygame.event.get():
            # обрабатываем событие нажатия на крестик
            if event.type == pygame.QUIT:
                # завершаем цикл игры
                running = False
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    my_player.rect.x += 25
                    my_player.startAnimation(ANIMATION_RIGHT)
                if event.key == pygame.K_s:
                    my_player.rect.x -= 25
                    my_player.startAnimation(ANIMATION_LEFT)
                # if event.key == pygame.K_a:
                #      -= 25
                # if event.key == pygame.K_d:
                #      += 25
        # задаем фон экрана
        screen.fill((0, 0, 0))
        all_sprites.update()

        # визуализация
        all_sprites.draw(screen)
        # замедляем время
        clock.tick(10)
        # обновление
        pygame.display.flip()


menu = pygame_menu.Menu("Minotaur's Labyrinth", 500, 500, theme=pygame_menu.themes.THEME_GREEN)


menu.add.button('Play', startGame)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)


