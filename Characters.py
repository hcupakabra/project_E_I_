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


class Player(Character):
    def __init__(self, hp, dmg, x, y, images, *groups):
        super().__init__(hp, dmg, x, y, images, *groups)
        self.MOVE_SPEED = 7
        self.JUMP_POWER = 10

    def update(self, *args):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if args and args[0].type == pygame.K_LEFT and self.rect.collidepoint(args[0].pos):
                    self.rect.x += 10
                if args and args[0].type == pygame.K_RIGHT and self.rect.collidepoint(args[0].pos):
                    self.rect.x -= 10


class Enemy(Character):
    pass


def startGame():
    clock = pygame.time.Clock()
    # игра - это цикл
    ANIMATION_RIGHT = [
        pygame.transform.scale(pygame.image.load('pictures/paint/r1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/paint/r2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/paint/r3.png'), (100, 100))]
    ANIMATION_LEFT = [
        pygame.transform.scale(pygame.image.load('pictures/paint/l1.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/paint/l2.png'), (100, 100)),
        pygame.transform.scale(pygame.image.load('pictures/paint/l3.png'), (100, 100))]
    ANIMATION_JUMP_LEFT = [pygame.transform.scale(pygame.image.load('pictures/paint/l3.png'), (100, 100))]
    ANIMATION_JUMP_RIGHT = [pygame.transform.scale(pygame.image.load('pictures/paint/r4.png'), (100, 100))]
    ANIMATION_JUMP = [pygame.transform.scale(pygame.image.load('pictures/paint/j.png'), (100, 100))]
    ANIMATION_STAY = [pygame.transform.scale(pygame.image.load('pictures/paint/stay.png'), (100, 100))]
    my_player = Character(100, 10, 55, 55, ANIMATION_RIGHT, player_group, all_sprites)
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