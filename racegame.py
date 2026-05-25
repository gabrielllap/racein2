import pygame
import random

pygame.init()
redcar = pygame.image.load("assets/redcar.png")
bluecar = pygame.image.load("assets/bluecar.png")
redcar = pygame.transform.scale(redcar, (60, 100))
bluecar = pygame.transform.scale(bluecar, (60, 100))

# dimensiuni
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Race in 2")

clock = pygame.time.Clock()
winner_font = pygame.font.SysFont("Arial", 120, bold=True)
menu_font = pygame.font.SysFont("Arial", 70, bold=True)
small_font = pygame.font.SysFont("Arial", 40)

# culori
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)

# player 1
p1_x = 200
p1_y = 600

# player 2
p2_x = 400
p2_y = 600

# butoane meniu

single_rect = pygame.Rect(390, 220, 500, 80)
multi_rect = pygame.Rect(390, 340, 500, 80)
ai_rect = pygame.Rect(390, 460, 500, 80)

car_width = 60
car_height = 100

speed = 5
winner = None
game_mode = None
in_menu = True

def draw_menu():

    screen.fill((20, 20, 20))

    title = winner_font.render(
        "CURSA IN 2",
        True,
        WHITE
    )

    screen.blit(title, (320, 70))

    # SINGLE PLAYER
    pygame.draw.rect(screen, RED, single_rect)

    single_text = menu_font.render(
        "Single Player",
        True,
        WHITE
    )

    screen.blit(single_text, (470, 235))

    # MULTIPLAYER
    pygame.draw.rect(screen, BLUE, multi_rect)

    multi_text = menu_font.render(
        "Multiplayer Local",
        True,
        WHITE
    )

    screen.blit(multi_text, (410, 355))

    # AI MODE
    pygame.draw.rect(screen, GREEN, ai_rect)

    ai_text = menu_font.render(
        "Vs AI",
        True,
        WHITE
    )

    screen.blit(ai_text, (560, 475))

    pygame.display.update()

running = True

while running:

    clock.tick(60)
    if in_menu:

        draw_menu()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                if single_rect.collidepoint(mouse_pos):
                    game_mode = "single"
                    in_menu = False

                if multi_rect.collidepoint(mouse_pos):
                    game_mode = "multi"
                    in_menu = False

                if ai_rect.collidepoint(mouse_pos):
                    game_mode = "ai"
                    in_menu = False

        continue

    # evenimente
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # PLAYER 1 - WASD

    if keys[pygame.K_w]:
        p1_y -= speed

    if keys[pygame.K_s]:
        p1_y += speed

    if keys[pygame.K_a]:
        p1_x -= speed

    if keys[pygame.K_d]:
        p1_x += speed

    # PLAYER 2 - SAGETI

    if game_mode == "multi":

        # controale player 2

        if keys[pygame.K_UP]:
            p2_y -= speed

        if keys[pygame.K_DOWN]:
            p2_y += speed

        if keys[pygame.K_LEFT]:
            p2_x -= speed

        if keys[pygame.K_RIGHT]:
            p2_x += speed

    # AI MODE

    if game_mode == "ai":

        ai_speed = 4

        # merge înainte constant
        p2_y -= ai_speed

        # urmărește playerul pe X

        if p2_x + car_width // 2 < p1_x + car_width // 2:
            p2_x += 3

        if p2_x + car_width // 2 > p1_x + car_width // 2:
            p2_x -= 3

    # limite ecran player 1

    if p1_x < 0:
        p1_x = 0

    if p1_x > WIDTH - car_width:
        p1_x = WIDTH - car_width

    if p1_y < 0:
        p1_y = 0

    if p1_y > HEIGHT - car_height:
        p1_y = HEIGHT - car_height

    # limite ecran player 2

    if p2_x < 0:
        p2_x = 0

    if p2_x > WIDTH - car_width:
        p2_x = WIDTH - car_width

    if p2_y < 0:
        p2_y = 0

    if p2_y > HEIGHT - car_height:
        p2_y = HEIGHT - car_height

    # coliziune între mașini
        # coliziune între mașini

        if game_mode != "single":

            if (
                    p1_x < p2_x + car_width and
                    p1_x + car_width > p2_x and
                    p1_y < p2_y + car_height and
                    p1_y + car_height > p2_y
            ):

                if p1_x < p2_x:
                    p1_x -= speed
                    p2_x += speed

                if p1_x > p2_x:
                    p1_x += speed
                    p2_x -= speed

                if p1_y < p2_y:
                    p1_y -= speed
                    p2_y += speed

                if p1_y > p2_y:
                    p1_y += speed
                    p2_y -= speed


        # împinge mașinile înapoi

        if p1_x < p2_x:
            p1_x -= speed
            p2_x += speed

        if p1_x > p2_x:
            p1_x += speed
            p2_x -= speed

        if p1_y < p2_y:
            p1_y -= speed
            p2_y += speed

        if p1_y > p2_y:
            p1_y += speed
            p2_y -= speed

    # verificare câștigător

    if p1_y <= 50:
        winner = "PLAYER 1 WIN"

    if p2_y <= 50:
        winner = "PLAYER 2 WIN"

    # fundal
    screen.fill(GRAY)

    # pista
    pygame.draw.rect(screen, (60, 60, 60), (150, 0, 980, 720))

    # finish line
    pygame.draw.rect(screen, WHITE, (150, 120, 980, 10))

    # mașini
    # car player 1
    screen.blit(redcar, (p1_x, p1_y))

    # car player 2
    if game_mode != "single":
        screen.blit(bluecar, (p2_x, p2_y))

    # afișare winner

    if winner is not None:
        winner_text = winner_font.render(
            winner,
            True,
            WHITE
        )

        text_rect = winner_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(winner_text, text_rect)

        pygame.display.update()

        pygame.time.delay(3000)

        running = False

    pygame.display.update()

pygame.quit()