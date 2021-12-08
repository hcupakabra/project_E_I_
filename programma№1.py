import pygame
# try:
#     # width = int(input())
#     # height = int(input())
# except ValueError as v:
#     print("Неправильный формат ввода")
#     exit()

SIZE = (800, 800)
BACKGROUND = (0, 0, 0)


def draw(screen):
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, "orange", (0, 500, 800, 300))
    pygame.draw.rect(screen, "blue", (0, 0, 800, 500))
    pygame.draw.rect(screen, "brown", (150, 340, 20, 160))
    pygame.draw.circle(screen, "green", (160, 350), 60)
    pygame.draw.rect(screen, "black", (300, 520, 100, 75))
    # pygame.draw.line(screen, (255, 255, 255), start_pos=(0, height), end_pos=(width, 0), width=5)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("ну это наш проект, ок?")
    screen = pygame.display.set_mode(size=SIZE)
    # цикл работы игры
    while True:
        if pygame.event.wait().type == pygame.QUIT:
            break
        draw(screen)
        pygame.display.flip()
    pygame.quit()