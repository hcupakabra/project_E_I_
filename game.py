import pygame
import pygame_menu
from Characters import *
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
enemy_group = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    print(image)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


animation_LEFT = [
        load_image("pavuk/walk0.gif", colorkey=-1),
        load_image("pavuk/walk1.gif", colorkey=-1),
        load_image("pavuk/walk2.gif", colorkey=-1),
        load_image("pavuk/walk3.gif", colorkey=-1),
        load_image("pavuk/walk4.gif", colorkey=-1)]
animation_IDLE = [
        load_image("pavuk/idle0.gif", colorkey=-1),
        load_image("pavuk/idle1.gif", colorkey=-1),
        load_image("pavuk/idle2.gif", colorkey=-1),
        load_image("pavuk/idle3.gif", colorkey=-1)]
animation_RIGHT = [
    pygame.transform.scale(load_image('Player/r1.png', colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image('Player/r2.png', colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image('Player/r3.png', colorkey=-1), (100, 100)),]
animation_LEFT = [
    pygame.transform.scale(load_image('Player/l1.png', colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image('Player/l2.png', colorkey=-1), (100, 100)),
    pygame.transform.scale(load_image('Player/l3.png', colorkey=-1), (100, 100))]
animation_STAY = [pygame.transform.scale(load_image('Player/stay.png', colorkey=-1), (100, 100))]


def startGame():
    clock = pygame.time.Clock()
    # игра - это цикл

    my_player = Player(100, 15, 205, 55, [animation_LEFT, animation_STAY, animation_RIGHT], player_group, all_sprites)
    enemy = Enemy(10, 5, 55, 55, [animation_IDLE, animation_LEFT], enemy_group, all_sprites)
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