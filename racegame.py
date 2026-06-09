import pygame
import random
import os

pygame.init()

#WINDOW SETTINGS
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("RACE IN 2")

#FPS SETTINGS
FPS = 60

clock = pygame.time.Clock()

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (220, 50, 50)
BLUE = (50, 120, 255)
GREEN = (50, 200, 50)

GRAY = (40, 40, 40)
DARK_GRAY = (25, 25, 25)

GOLD = (255, 215, 0)

#FONTS
title_font = pygame.font.SysFont(
    "Arial",
    90,
    bold=True
)

menu_font = pygame.font.SysFont(
    "Arial",
    45,
    bold=True
)

small_font = pygame.font.SysFont(
    "Arial",
    30,
    bold=True
)

winner_font = pygame.font.SysFont(
    "Arial",
    110,
    bold=True
)
#LOAD CAR IMAGES
red_car = pygame.image.load(
    "assets/redcar.png"
)

blue_car = pygame.image.load(
    "assets/bluecar.png"
)

green_car = pygame.image.load(
    "assets/greencar.png"
)

pink_car = pygame.image.load(
    "assets/pinkcar.png"
)
#SCALE CAR IMAGES
CAR_WIDTH = 60
CAR_HEIGHT = 100

red_car = pygame.transform.scale(
    red_car,
    (CAR_WIDTH, CAR_HEIGHT)
)

blue_car = pygame.transform.scale(
    blue_car,
    (CAR_WIDTH, CAR_HEIGHT)
)

green_car = pygame.transform.scale(
    green_car,
    (CAR_WIDTH, CAR_HEIGHT)
)

pink_car = pygame.transform.scale(
    pink_car,
    (CAR_WIDTH, CAR_HEIGHT)
)
#LOAD OBSTACLES IMAGE
road_con = pygame.image.load(
    "assets/roadcon.png"
)

road_con = pygame.transform.scale(
    road_con,
    (50, 50)
)
#CAR DICTIONARY
car_images = {
    "RED": red_car,
    "BLUE": blue_car,
    "GREEN": green_car,
    "PINK": pink_car
}
#GAME STATES
MENU = "menu"
CAR_SELECT = "car_select"
GAME = "game"
LEADERBOARD = "leaderboard"
WINNER = "winner"

#CURRENT STATE
game_state = MENU

#GAME MODES
SINGLEPLAYER = "singleplayer"
MULTIPLAYER = "multiplayer"
AI_MODE = "ai"

#SELECTED MODE
selected_mode = None

#SELECTED CARS
player1_car = None
player2_car = None
ai_car = None

#CAR SELECTION VARIABLES
selection_step = 1

available_cars = [
    "RED",
    "BLUE",
    "GREEN",
    "PINK"
]
#TRACK SETTINGS
TRACK_LEFT = 200
TRACK_RIGHT = 1080

FINISH_Y = 80

#PLAYER SETTINGS
CAR_SPEED = 5

p1_x = 0
p1_y = 0

p2_x = 0
p2_y = 0

ai_x = 0
ai_y = 0

#OBSTACLES LIST
obstacles = []

#PLAYER RECTS
winner = None
start_time = 0
current_time = 0

#HANDLE GAME INPUT
def handle_game_input():

    global p1_x
    global p1_y

    global p2_x
    global p2_y

    keys = pygame.key.get_pressed()

    # PLAYER 1 (WASD)

    if keys[pygame.K_w]:
        p1_y -= CAR_SPEED

    if keys[pygame.K_s]:
        p1_y += CAR_SPEED

    if keys[pygame.K_a]:
        p1_x -= CAR_SPEED

    if keys[pygame.K_d]:
        p1_x += CAR_SPEED

    # PLAYER 2 (ARROWS)

    if selected_mode == MULTIPLAYER:

        if keys[pygame.K_UP]:
            p2_y -= CAR_SPEED

        if keys[pygame.K_DOWN]:
            p2_y += CAR_SPEED

        if keys[pygame.K_LEFT]:
            p2_x -= CAR_SPEED

        if keys[pygame.K_RIGHT]:
            p2_x += CAR_SPEED
#TRACK LIMITS
def keep_cars_on_track():

    global p1_x
    global p1_y

    global p2_x
    global p2_y

    global ai_x
    global ai_y

    # PLAYER 1

    p1_x = max(
        TRACK_LEFT,
        min(
            p1_x,
            TRACK_RIGHT - CAR_WIDTH
        )
    )

    p1_y = max(
        0,
        min(
            p1_y,
            HEIGHT - CAR_HEIGHT
        )
    )

    # PLAYER 2

    p2_x = max(
        TRACK_LEFT,
        min(
            p2_x,
            TRACK_RIGHT - CAR_WIDTH
        )
    )

    p2_y = max(
        0,
        min(
            p2_y,
            HEIGHT - CAR_HEIGHT
        )
    )

    # AI

    ai_x = max(
        TRACK_LEFT,
        min(
            ai_x,
            TRACK_RIGHT - CAR_WIDTH
        )
    )

    ai_y = max(
        0,
        min(
            ai_y,
            HEIGHT - CAR_HEIGHT
        )
    )
#AI MOVEMENTS
def update_ai():

    global ai_y

    if selected_mode == AI_MODE:
        ai_y -= random.uniform(
            2.5,
            4.5
        )
#CAR COLLISION
def handle_car_collision():

    global p1_x
    global p2_x

    if selected_mode != MULTIPLAYER:
        return

    car1 = pygame.Rect(
        p1_x,
        p1_y,
        CAR_WIDTH,
        CAR_HEIGHT
    )

    car2 = pygame.Rect(
        p2_x,
        p2_y,
        CAR_WIDTH,
        CAR_HEIGHT
    )

    if car1.colliderect(car2):

        if p1_x < p2_x:

            p1_x -= 3
            p2_x += 3

        else:

            p1_x += 3
            p2_x -= 3
#OBSTACLE COLLISION
def handle_obstacle_collision():

    global p1_x
    global p1_y

    global p2_x
    global p2_y

    global ai_y

    player1_rect = pygame.Rect(
        p1_x,
        p1_y,
        CAR_WIDTH,
        CAR_HEIGHT
    )

    player2_rect = pygame.Rect(
        p2_x,
        p2_y,
        CAR_WIDTH,
        CAR_HEIGHT
    )

    ai_rect = pygame.Rect(
        ai_x,
        ai_y,
        CAR_WIDTH,
        CAR_HEIGHT
    )

    for obstacle in obstacles:

        if player1_rect.colliderect(obstacle):
            p1_y += 4

        if player2_rect.colliderect(obstacle):
            p2_y += 4

        if ai_rect.colliderect(obstacle):
            ai_y += 2
#WINNER DETECTION
def check_winner():

    global winner
    global game_state

    if p1_y <= FINISH_Y:

        winner = "PLAYER 1"

        if selected_mode == SINGLEPLAYER:
            save_score(current_time)

        game_state = WINNER

    if selected_mode == MULTIPLAYER:

        if p2_y <= FINISH_Y:

            winner = "PLAYER 2"

            game_state = WINNER

    if selected_mode == AI_MODE:

        if ai_y <= FINISH_Y:

            winner = "AI"

            game_state = WINNER
#LOAD LEADERBOARD
def load_leaderboard():

    try:

        with open(
            LEADERBOARD_FILE,
            "r"
        ) as file:

            scores = []

            for line in file:

                try:
                    scores.append(
                        float(line.strip())
                    )

                except:
                    pass

            scores.sort()

            return scores[:5]

    except:

        return []

#DRAW LEADERBOARD
def draw_leaderboard():

    screen.fill(BLACK)

    title = winner_font.render(
        "LEADERBOARD",
        True,
        GOLD
    )

    title_rect = title.get_rect(
        center=(WIDTH // 2, 100)
    )

    screen.blit(
        title,
        title_rect
    )

    scores = load_leaderboard()

    for i, score in enumerate(scores):

        score_text = menu_font.render(
            f"{i+1}. {score:.2f}s",
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (450, 200 + i * 50)
        )

    draw_button(
        back_to_menu_rect,
        "BACK TO MENU",
        pygame.mouse.get_pos()
    )
#LEADERBOARD EVENTS
def handle_leaderboard_events(event):

    global game_state

    if event.type == pygame.MOUSEBUTTONDOWN:

        if back_to_menu_rect.collidepoint(
            pygame.mouse.get_pos()
        ):

            game_state = MENU
#UPDATE GAME
def update_game():

    update_timer()

    handle_game_input()

    update_ai()

    keep_cars_on_track()

    handle_car_collision()

    handle_obstacle_collision()

    check_winner()

#GENERATE RANDOM OBSTACLES
def generate_obstacles():

    global obstacles

    obstacles = []

    for i in range(10):

        x = random.randint(
            TRACK_LEFT + 50,
            TRACK_RIGHT - 50
        )

        y = random.randint(
            150,
            HEIGHT - 150
        )

        obstacles.append(
            pygame.Rect(
                x,
                y,
                50,
                50
            )
        )
#RESET POSITIONS
def reset_positions():

    global p1_x
    global p1_y

    global p2_x
    global p2_y

    global ai_x
    global ai_y

    p1_x = WIDTH // 2 - 120
    p1_y = HEIGHT - 120

    p2_x = WIDTH // 2 + 60
    p2_y = HEIGHT - 120

    ai_x = WIDTH // 2
    ai_y = HEIGHT - 120

#LEADERBOARD FILE
LEADERBOARD_FILE = "leaderboard.txt"

#CREATE FILE IF MISSING
if not os.path.exists(
    LEADERBOARD_FILE
):
    open(
        LEADERBOARD_FILE,
        "w"
    ).close()

#MENU BUTTONS
single_rect = pygame.Rect(
    390,
    220,
    500,
    70
)

multi_rect = pygame.Rect(
    390,
    310,
    500,
    70
)

ai_rect = pygame.Rect(
    390,
    400,
    500,
    70
)

leaderboard_rect = pygame.Rect(
    390,
    490,
    500,
    70
)

exit_rect = pygame.Rect(
    390,
    580,
    500,
    70
)
#CAR BUTTONS
car_red_rect = pygame.Rect(
    100,
    250,
    220,
    220
)

car_blue_rect = pygame.Rect(
    380,
    250,
    220,
    220
)

car_green_rect = pygame.Rect(
    660,
    250,
    220,
    220
)

car_pink_rect = pygame.Rect(
    940,
    250,
    220,
    220
)

#DRAW MENU FUNCTION
def draw_menu():

    screen.fill(DARK_GRAY)

    mouse_pos = pygame.mouse.get_pos()

    # TITLU

    shadow = title_font.render(
        "RACE IN 2",
        True,
        (50, 50, 50)
    )

    title = title_font.render(
        "RACE IN 2",
        True,
        GOLD
    )

    shadow_rect = shadow.get_rect(
        center=(WIDTH // 2 + 4, 104)
    )

    title_rect = title.get_rect(
        center=(WIDTH // 2, 100)
    )

    screen.blit(shadow, shadow_rect)
    screen.blit(title, title_rect)

    draw_button(
        single_rect,
        "SINGLE PLAYER",
        mouse_pos
    )

    draw_button(
        multi_rect,
        "MULTIPLAYER 1 VS 1",
        mouse_pos
    )

    draw_button(
        ai_rect,
        "PLAYER VS AI",
        mouse_pos
    )

    draw_button(
        leaderboard_rect,
        "LEADERBOARD",
        mouse_pos
    )

    draw_button(
        exit_rect,
        "EXIT",
        mouse_pos
    )
#DRAW CAR SELECT
def draw_car_select():

    screen.fill(DARK_GRAY)

    if selected_mode == MULTIPLAYER:

        if selection_step == 1:

            title_text = (
                "PLAYER 1 CHOOSE"
            )

        else:

            title_text = (
                "PLAYER 2 CHOOSE"
            )

    else:

        title_text = "COOSE YOUR CAR"

    title = menu_font.render(
        title_text,
        True,
        WHITE
    )

    title_rect = title.get_rect(
        center=(WIDTH // 2, 100)
    )

    screen.blit(title, title_rect)
    draw_car_option(
        car_red_rect,
        red_car,
        "RED"
    )

    draw_car_option(
        car_blue_rect,
        blue_car,
        "BLUE"
    )

    draw_car_option(
        car_green_rect,
        green_car,
        "GREEN"
    )

    draw_car_option(
        car_pink_rect,
        pink_car,
        "PINK"
    )

    if (
            selected_mode == MULTIPLAYER
            and selection_step == 2
    ):

        if player1_car == "RED":
            draw_lock(car_red_rect)

        elif player1_car == "BLUE":
            draw_lock(car_blue_rect)

        elif player1_car == "GREEN":
            draw_lock(car_green_rect)

        elif player1_car == "PINK":
            draw_lock(car_pink_rect)
#LOCK FUNCTION
def draw_lock(rect):

    overlay = pygame.Surface(
        (
            rect.width,
            rect.height
        ),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 180)
    )

    screen.blit(
        overlay,
        rect.topleft
    )

    lock_text = menu_font.render(
        "USED",
        True,
        RED
    )

    lock_rect = lock_text.get_rect(
        center=rect.center
    )

    screen.blit(
        lock_text,
        lock_rect
    )
#DRAW CAR SELECT
def draw_car_select():

    screen.fill(DARK_GRAY)

    if selected_mode == MULTIPLAYER:

        if selection_step == 1:

            title_text = (
                "PLAYER 1 CHOOSE"
            )

        else:

            title_text = (
                "PLAYER 2 CHOOSE"
            )

    else:

        title_text = "CHOOSE YOUR CAR"

    title = menu_font.render(
        title_text,
        True,
        WHITE
    )

    title_rect = title.get_rect(
        center=(WIDTH // 2, 100)
    )

    screen.blit(title, title_rect)

    draw_car_option(
        car_red_rect,
        red_car,
        "RED"
    )

    draw_car_option(
        car_blue_rect,
        blue_car,
        "BLUE"
    )

    draw_car_option(
        car_green_rect,
        green_car,
        "GREEN"
    )

    draw_car_option(
        car_pink_rect,
        pink_car,
        "PINK"
    )
#DRAW CAR OPTION
def draw_car_option(
    rect,
    image,
    name
):

    mouse_pos = pygame.mouse.get_pos()

    border_color = WHITE

    if rect.collidepoint(mouse_pos):
        border_color = GOLD

    pygame.draw.rect(
        screen,
        border_color,
        rect,
        4,
        border_radius=20
    )

    image_rect = image.get_rect(
        center=(
            rect.centerx,
            rect.centery - 20
        )
    )

    screen.blit(
        image,
        image_rect
    )

    text = menu_font.render(
        name,
        True,
        WHITE
    )

    text_rect = text.get_rect(
        center=(
            rect.centerx,
            rect.bottom - 30
        )
    )

    screen.blit(
        text,
        text_rect
    )
#DRAW BUTTON FUNCTION
def draw_button(
    rect,
    text,
    mouse_pos
):

    color = (80, 80, 80)

    if rect.collidepoint(mouse_pos):
        color = (120, 120, 120)

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=20
    )

    pygame.draw.rect(
        screen,
        WHITE,
        rect,
        3,
        border_radius=20
    )

    button_text = menu_font.render(
        text,
        True,
        WHITE
    )

    text_rect = button_text.get_rect(
        center=rect.center
    )

    screen.blit(
        button_text,
        text_rect
    )
#MENU EVENT FUNCTION
def handle_menu_events(
    event
):

    global game_state
    global selected_mode

    if event.type == pygame.MOUSEBUTTONDOWN:

        mouse_pos = pygame.mouse.get_pos()

        if single_rect.collidepoint(mouse_pos):

            selected_mode = SINGLEPLAYER
            game_state = CAR_SELECT

        elif multi_rect.collidepoint(mouse_pos):

            selected_mode = MULTIPLAYER
            game_state = CAR_SELECT

        elif ai_rect.collidepoint(mouse_pos):

            selected_mode = AI_MODE
            game_state = CAR_SELECT

        elif leaderboard_rect.collidepoint(mouse_pos):

            game_state = LEADERBOARD

        elif exit_rect.collidepoint(mouse_pos):

            pygame.quit()
            exit()
#HANDLE CAR SELECT EVENTS
def handle_car_select(
    event
):

    global player1_car
    global player2_car
    global ai_car

    global game_state
    global selection_step

    if event.type != pygame.MOUSEBUTTONDOWN:
        return

    mouse_pos = pygame.mouse.get_pos()

    selected_car = None

    if car_red_rect.collidepoint(mouse_pos):
        selected_car = "RED"

    elif car_blue_rect.collidepoint(mouse_pos):
        selected_car = "BLUE"

    elif car_green_rect.collidepoint(mouse_pos):
        selected_car = "GREEN"

    elif car_pink_rect.collidepoint(mouse_pos):
        selected_car = "PINK"

    if selected_car is None:
        return
    #SINGLE PLAYER
    if selected_mode == SINGLEPLAYER:

        player1_car = selected_car

        start_game()
    #PLAYER VS AI
    elif selected_mode == AI_MODE:

        player1_car = selected_car

        remaining = [
            car for car in available_cars
            if car != player1_car
        ]

        ai_car = random.choice(
            remaining
        )

        start_game()
    #MULTIPLAYER
    elif selected_mode == MULTIPLAYER:

        if selection_step == 1:

            player1_car = selected_car

            selection_step = 2

        else:

            if selected_car == player1_car:
                return

            player2_car = selected_car

            start_game()
#START GAME FUNCTION
def start_game():

    global game_state
    global start_time

    reset_positions()

    generate_obstacles()

    start_time = pygame.time.get_ticks()

    game_state = GAME

#UPDATE TIMER
def update_timer():

    global current_time

    current_time = (
        pygame.time.get_ticks()
        - start_time
    ) / 1000

#DRAW TIMER
def draw_timer():

    timer_text = small_font.render(
        f"Time: {current_time:.2f}s",
        True,
        WHITE
    )

    screen.blit(
        timer_text,
        (20, 20)
    )

#DRAW TRACK
def draw_track():

    screen.fill((20, 120, 20))

    pygame.draw.rect(
        screen,
        (60, 60, 60),
        (
            TRACK_LEFT,
            0,
            TRACK_RIGHT - TRACK_LEFT,
            HEIGHT
        )
    )

    pygame.draw.line(
        screen,
        WHITE,
        (TRACK_LEFT, FINISH_Y),
        (TRACK_RIGHT, FINISH_Y),
        8
    )

#DRAW OBSTACLES
def draw_obstacles():

    for obstacle in obstacles:

        screen.blit(
            road_con,
            obstacle
        )

#DRAW CARS
def draw_cars():

    screen.blit(
        car_images[player1_car],
        (p1_x, p1_y)
    )

    if selected_mode == MULTIPLAYER:

        screen.blit(
            car_images[player2_car],
            (p2_x, p2_y)
        )

    elif selected_mode == AI_MODE:

        screen.blit(
            car_images[ai_car],
            (ai_x, ai_y)
        )

#DRAW GAME
def draw_game():

    update_game()

    draw_track()

    draw_obstacles()

    draw_cars()

    draw_timer()

#SAVE SCORE
def save_score(time_value):

    with open(
        LEADERBOARD_FILE,
        "a"
    ) as file:

        file.write(
            f"{time_value:.2f}\n"
        )
#WINNER SCREEN
back_to_menu_rect = pygame.Rect(
    440,
    500,
    400,
    80
)
def draw_winner_screen():

    screen.fill(BLACK)

    winner_text = winner_font.render(
        f"{winner} WINS!",
        True,
        GOLD
    )

    text_rect = winner_text.get_rect(
        center=(WIDTH // 2, 250)
    )

    screen.blit(
        winner_text,
        text_rect
    )

    draw_button(
        back_to_menu_rect,
        "BACK TO MENU",
        pygame.mouse.get_pos()
    )
#HANDLE WINNER EVENTS
def handle_winner_events(event):

    global game_state
    global winner
    global selection_step
    global player1_car
    global player2_car
    global ai_car

    if event.type == pygame.MOUSEBUTTONDOWN:

        if back_to_menu_rect.collidepoint(
            pygame.mouse.get_pos()
        ):
            winner = None

            selection_step = 1

            player1_car = None
            player2_car = None
            ai_car = None

            game_state = MENU

# MAIN LOOP

running = True

while running:

    clock.tick(FPS)

    # EVENTS

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # MENU

        if game_state == MENU:
            handle_menu_events(event)

        # CAR SELECT

        elif game_state == CAR_SELECT:
            handle_car_select(event)

        # WINNER SCREEN

        elif game_state == WINNER:
            handle_winner_events(event)

        #LEADERBOARD
        elif game_state == LEADERBOARD:
            handle_leaderboard_events(event)

    # DRAW STATES

    if game_state == MENU:

        draw_menu()

    elif game_state == CAR_SELECT:

        draw_car_select()

    elif game_state == GAME:

        draw_game()

    elif game_state == LEADERBOARD:

        draw_leaderboard()

    elif game_state == WINNER:

        draw_winner_screen()

    pygame.display.update()

pygame.quit()