import pygame
import random
import time

pygame.init()

# LOAD CAR IMAGES

redcar = pygame.image.load("assets/redcar.png")
bluecar = pygame.image.load("assets/bluecar.png")
roadcon = pygame.image.load("assets/roadcon.png")

redcar = pygame.transform.scale(redcar, (60, 100))
bluecar = pygame.transform.scale(bluecar, (60, 100))
roadcon = pygame.transform.scale(roadcon, (70, 70))

# WINDOW SETTINGS

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Race in 2")

clock = pygame.time.Clock()

# FONTS

winner_font = pygame.font.SysFont("Arial", 120, bold=True)
menu_font = pygame.font.SysFont("Arial", 70, bold=True)
small_font = pygame.font.SysFont("Arial", 35)

# COLORS

WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)

# PLAYER 1 POSITION

p1_x = 250
p1_y = 600

# PLAYER 2 POSITION

p2_x = 900
p2_y = 600

# CAR SETTINGS

car_width = 60
car_height = 100

speed = 5

# GAME VARIABLES

winner = None

game_mode = None

in_menu = True

start_time = 0
finish_time = 0

# MENU BUTTONS

single_rect = pygame.Rect(390, 220, 500, 80)

multi_rect = pygame.Rect(390, 340, 500, 80)

ai_rect = pygame.Rect(390, 460, 500, 80)

# OBSTACLES

obstacles = [

    pygame.Rect(350, 250, 70, 70),

    pygame.Rect(800, 400, 70, 70),

    pygame.Rect(550, 520, 70, 70),

    pygame.Rect(950, 250, 70, 70)

]


# LOAD LEADERBOARD

def load_leaderboard():

    scores = []

    try:

        with open("leaderboard.txt", "r") as file:

            for line in file:
                scores.append(line.strip())

    except:
        pass

    return scores[-5:]

# DRAW MENU

def draw_menu():

    screen.fill((20, 20, 20))

    # game title
    title = winner_font.render(
        "RACE IN 2",
        True,
        WHITE
    )

    screen.blit(title, (280, 70))

    # single player button
    pygame.draw.rect(screen, RED, single_rect)

    single_text = menu_font.render(
        "Single Player",
        True,
        WHITE
    )

    screen.blit(single_text, (460, 235))

    # multiplayer button
    pygame.draw.rect(screen, BLUE, multi_rect)

    multi_text = menu_font.render(
        "Local Multiplayer",
        True,
        WHITE
    )

    screen.blit(multi_text, (360, 355))

    # ai button
    pygame.draw.rect(screen, GREEN, ai_rect)

    ai_text = menu_font.render(
        "VS AI",
        True,
        WHITE
    )

    screen.blit(ai_text, (550, 475))

    pygame.display.update()

# MAIN GAME LOOP

running = True

while running:

    clock.tick(60)

    # MENU LOOP

    if in_menu:

        draw_menu()

        for event in pygame.event.get():

            # close game
            if event.type == pygame.QUIT:
                running = False

            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                # single player
                if single_rect.collidepoint(mouse_pos):

                    game_mode = "single"

                    in_menu = False

                    start_time = time.time()

                # multiplayer
                if multi_rect.collidepoint(mouse_pos):

                    game_mode = "multi"

                    in_menu = False

                    start_time = time.time()

                # ai mode
                if ai_rect.collidepoint(mouse_pos):

                    game_mode = "ai"

                    in_menu = False

                    start_time = time.time()

        continue

    # EVENTS

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # GAME MOVEMENT

    if winner is None:

        # PLAYER 1 CONTROLS

        if keys[pygame.K_w]:
            p1_y -= speed

        if keys[pygame.K_s]:
            p1_y += speed

        if keys[pygame.K_a]:
            p1_x -= speed

        if keys[pygame.K_d]:
            p1_x += speed

        # PLAYER 2 CONTROLS

        if game_mode == "multi":

            if keys[pygame.K_UP]:
                p2_y -= speed

            if keys[pygame.K_DOWN]:
                p2_y += speed

            if keys[pygame.K_LEFT]:
                p2_x -= speed

            if keys[pygame.K_RIGHT]:
                p2_x += speed

        # AI MOVEMENT

        if game_mode == "ai":

            ai_speed = 4

            # move forward
            p2_y -= ai_speed

            # follow player on X axis
            if p2_x + car_width // 2 < p1_x + car_width // 2:
                p2_x += 3

            if p2_x + car_width // 2 > p1_x + car_width // 2:
                p2_x -= 3

        # PLAYER 1 SCREEN LIMITS

        if p1_x < 0:
            p1_x = 0

        if p1_x > WIDTH - car_width:
            p1_x = WIDTH - car_width

        if p1_y < 0:
            p1_y = 0

        if p1_y > HEIGHT - car_height:
            p1_y = HEIGHT - car_height

        # PLAYER 2 SCREEN LIMITS

        if p2_x < 0:
            p2_x = 0

        if p2_x > WIDTH - car_width:
            p2_x = WIDTH - car_width

        if p2_y < 0:
            p2_y = 0

        if p2_y > HEIGHT - car_height:
            p2_y = HEIGHT - car_height

        # CAR COLLISION
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

        # PLAYER 1 OBSTACLE COLLISION

        player1_rect = pygame.Rect(
            p1_x,
            p1_y,
            car_width,
            car_height
        )

        for obstacle in obstacles:

            if player1_rect.colliderect(obstacle):
                # push player back
                p1_y += 10

        # PLAYER 2 OBSTACLE COLLISION

        if game_mode != "single":

            player2_rect = pygame.Rect(
                p2_x,
                p2_y,
                car_width,
                car_height
            )

            for obstacle in obstacles:

                if player2_rect.colliderect(obstacle):
                    p2_y += 10
        # WINNER CHECK

        if p1_y <= 50 and winner is None:

            winner = "PLAYER 1 WINS"

            finish_time = round(
                time.time() - start_time,
                2
            )

            with open("leaderboard.txt", "a") as file:

                file.write(
                    f"PLAYER 1 - {finish_time} seconds\n"
                )

        if game_mode != "single":

            if p2_y <= 50 and winner is None:

                winner = "PLAYER 2 WINS"

                finish_time = round(
                    time.time() - start_time,
                    2
                )

                with open("leaderboard.txt", "a") as file:

                    file.write(
                        f"PLAYER 2 - {finish_time} seconds\n"
                    )

    # DRAW BACKGROUND

    screen.fill(GRAY)

    # road
    pygame.draw.rect(
        screen,
        (60, 60, 60),
        (150, 0, 980, 720)
    )

    # finish line
    pygame.draw.rect(
        screen,
        WHITE,
        (150, 120, 980, 10)
    )

    # middle road lines
    for y in range(0, HEIGHT, 40):

        pygame.draw.rect(
            screen,
            WHITE,
            (WIDTH // 2 - 5, y, 10, 20)
        )

    # DRAW OBSTACLES

    for obstacle in obstacles:
        screen.blit(
            roadcon,
            (obstacle.x, obstacle.y)
        )

    # TIMER

    if winner is None:
        current_time = round(
            time.time() - start_time,
            2
        )

    else:
        current_time = finish_time

    timer_text = small_font.render(
        f"Time: {current_time}s",
        True,
        WHITE
    )

    screen.blit(timer_text, (20, 20))

    # LEADERBOARD

    leaderboard = load_leaderboard()

    leaderboard_title = small_font.render(
        "LEADERBOARD",
        True,
        WHITE
    )

    screen.blit(leaderboard_title, (20, 70))

    for i, score in enumerate(leaderboard):

        score_text = small_font.render(
            score,
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (20, 110 + i * 35)
        )

    # DRAW CARS

    # player 1 car
    screen.blit(redcar, (p1_x, p1_y))

    # player 2 car
    if game_mode != "single":
        screen.blit(bluecar, (p2_x, p2_y))

    # DRAW WINNER

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

    # update screen
    pygame.display.update()

# CLOSE GAME

pygame.quit()