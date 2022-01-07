
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


def startGame():
    # база картинок для дракоши
    images_my_player = [
        pygame.image.load("data/pavuk/frame_0_delay-0.1s.gif"),
        pygame.image.load("data/pavuk/frame_1_delay-0.1s.gif"),
        pygame.image.load("data/pavuk/frame_2_delay-0.1s.gif"),
        pygame.image.load("data/pavuk/frame_3_delay-0.1s.gif")
    ]
    # создаем нашего героя, что будет ходить (экземпляр класса Character)
    my_player = Character(0, 0, images_my_player, player_group, all_sprites)
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

# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', startGame)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)


