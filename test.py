import pygame as py
import random
import os

# настройка папки ассетов
game_folder = os.path.dirname(__file__)
pictures_folder = os.path.join(game_folder, 'pictures')
player_up = py.image.load(os.path.join(pictures_folder, 'tank1_up.png'))
player_down = py.image.load(os.path.join(pictures_folder, 'tank1_down.png'))
player_left = py.image.load(os.path.join(pictures_folder, 'tank1_left.png'))
player_right = py.image.load(os.path.join(pictures_folder, 'tank1_right.png'))
bg = py.image.load(os.path.join(pictures_folder, 'i.jpg'))

WIDTH = 480
HEIGHT = 600
FPS = 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (33, 33, 33)
YELLOW = (255, 255, 0)


class Mob(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Player(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = player_up
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = py.key.get_pressed()
        if __name__ == "__main__":
            if keystate[py.K_a]:
                self.speedx = -3
                self.image = player_left
                img = player_left
            elif keystate[py.K_d]:
                self.speedx = 3
                self.image = player_right
                img = player_right
            elif keystate[py.K_w]:
                self.speedy = -3
                self.image = player_up
                img = player_up
            elif keystate[py.K_s]:
                self.speedy = 3
                self.image = player_down
                img = player_down
        if self.rect.y > HEIGHT - 50:
            self.rect.y = HEIGHT - 50
        if self.rect.y < 0:
            self.rect.y = 0
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.image)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(py.sprite.Sprite):
    def __init__(self, x, y, dir):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        if dir == player_up:
            self.speedx = 0
            self.speedy = -10
        elif dir == player_down:
            self.speedx = 0
            self.speedy = 10
        elif dir == player_left:
            self.speedx = -10
            self.speedy = 0
        elif dir == player_right:
            self.speedx = 10
            self.speedy = 0

    def update(self):

        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


py.init()
py.mixer.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("My First Game")
clock = py.time.Clock()

all_sprites = py.sprite.Group()
player = Player()
all_sprites.add(player)
bullets = py.sprite.Group()
mobs = py.sprite.Group()
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

running = True
while running:
    screen.fill(BLACK)
    screen.blit(bg, (0, 0))
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                player.shoot()

    # Обновление спрайтов
    all_sprites.update()
    hits = py.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits = py.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    # Рендеринг
    # Отрисовываем спрайт

    all_sprites.draw(screen)
    # ПОВОРОТ ЭКРАНА
    py.display.flip()
py.quit()