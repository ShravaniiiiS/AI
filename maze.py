# =====================================================
# DARK MAZE ESCAPE GAME
# Smooth + Horror UI + Torch Vision
# =====================================================

# INSTALL:
# pip install pygame

import pygame
import sys

pygame.init()

# =====================================================
# WINDOW
# =====================================================

WIDTH = 700
HEIGHT = 760

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ESCAPE THE LAB")

clock = pygame.time.Clock()

# =====================================================
# COLORS
# =====================================================

BLACK = (8,8,8)
DARK_RED = (60,0,0)
RED = (200,0,0)
WHITE = (230,230,230)
GREEN = (0,200,100)
GRAY = (45,45,45)
GOLD = (255,215,0)

# =====================================================
# FONTS
# =====================================================

title_font = pygame.font.SysFont("Arial", 42, bold=True)
font = pygame.font.SysFont("Arial", 26)
small = pygame.font.SysFont("Arial", 20)

# =====================================================
# GRID
# =====================================================

ROWS = 10
CELL = 70

# =====================================================
# MAZES
# =====================================================

levels = [

[
[0,1,0,0,0,1,0,0,0,0],
[0,1,0,1,0,1,0,1,1,0],
[0,0,0,1,0,0,0,1,0,0],
[1,1,0,1,1,1,0,1,0,1],
[0,0,0,0,0,1,0,0,0,0],
[0,1,1,1,0,1,1,1,1,0],
[0,0,0,1,0,0,0,0,0,0],
[1,1,0,1,1,1,1,1,0,1],
[0,0,0,0,0,0,0,1,0,0],
[0,1,1,1,1,1,0,0,0,0]
],

[
[0,0,1,0,0,1,0,0,0,0],
[1,0,1,0,1,1,0,1,1,0],
[0,0,0,0,0,0,0,1,0,0],
[0,1,1,1,1,1,0,1,0,1],
[0,0,0,0,0,1,0,0,0,0],
[1,1,1,1,0,1,1,1,1,0],
[0,0,0,1,0,0,0,0,0,0],
[0,1,0,1,1,1,1,1,0,1],
[0,1,0,0,0,0,0,1,0,0],
[0,0,0,1,1,1,0,0,0,0]
]

]

# =====================================================
# VARIABLES
# =====================================================

level = 0
maze = levels[level]

px = 0
py = 0

gx = 9
gy = 9

coins = [
(2,0),
(4,2),
(0,4),
(6,8)
]

score = 0

won = False

start_time = pygame.time.get_ticks()

# =====================================================
# NEXT LEVEL
# =====================================================

def next_level():

    global level
    global maze
    global px
    global py
    global won
    global start_time

    if level < len(levels) - 1:

        level += 1

        maze = levels[level]

        px = 0
        py = 0

        won = False

        start_time = pygame.time.get_ticks()

# =====================================================
# DRAW MAZE
# =====================================================

def draw_maze():

    for row in range(ROWS):

        for col in range(ROWS):

            rect = pygame.Rect(
                col * CELL,
                row * CELL,
                CELL,
                CELL
            )

            if maze[row][col] == 1:

                pygame.draw.rect(
                    screen,
                    DARK_RED,
                    rect
                )

            else:

                pygame.draw.rect(
                    screen,
                    BLACK,
                    rect
                )

            pygame.draw.rect(
                screen,
                GRAY,
                rect,
                1
            )

# =====================================================
# PLAYER
# =====================================================

def draw_player():

    x = px * CELL + CELL//2
    y = py * CELL + CELL//2

    pygame.draw.circle(
        screen,
        WHITE,
        (x, y-10),
        8
    )

    pygame.draw.line(
        screen,
        WHITE,
        (x,y),
        (x,y+18),
        3
    )

    pygame.draw.line(
        screen,
        WHITE,
        (x-8,y+5),
        (x+8,y+5),
        3
    )

    pygame.draw.line(
        screen,
        WHITE,
        (x,y+18),
        (x-8,y+28),
        3
    )

    pygame.draw.line(
        screen,
        WHITE,
        (x,y+18),
        (x+8,y+28),
        3
    )

# =====================================================
# EXIT DOOR
# =====================================================

def draw_exit():

    x = gx * CELL + 18
    y = gy * CELL + 12

    pygame.draw.rect(
        screen,
        GREEN,
        (x,y,35,45)
    )

    pygame.draw.circle(
        screen,
        GOLD,
        (x+25,y+22),
        3
    )

# =====================================================
# COINS
# =====================================================

def draw_coins():

    for coin in coins:

        pygame.draw.circle(
            screen,
            GOLD,
            (
                coin[0] * CELL + 35,
                coin[1] * CELL + 35
            ),
            8
        )

# =====================================================
# TORCH EFFECT
# =====================================================

def draw_torch():

    fog = pygame.Surface((WIDTH, HEIGHT))

    fog.fill((0,0,0))

    fog.set_alpha(215)

    x = px * CELL + CELL//2
    y = py * CELL + CELL//2

    pygame.draw.circle(
        fog,
        (120,120,120),
        (x,y),
        120
    )

    screen.blit(fog, (0,0))

# =====================================================
# UI
# =====================================================

def draw_ui():

    title = title_font.render(
        "ESCAPE THE LAB",
        True,
        RED
    )

    screen.blit(title, (180, 705))

    level_text = small.render(
        f"Level: {level+1}",
        True,
        WHITE
    )

    screen.blit(level_text, (20,20))

    score_text = small.render(
        f"Coins: {score}",
        True,
        GOLD
    )

    screen.blit(score_text, (20,50))

    timer = (
        pygame.time.get_ticks() - start_time
    ) // 1000

    timer_text = small.render(
        f"Time: {timer}s",
        True,
        WHITE
    )

    screen.blit(timer_text, (20,80))

# =====================================================
# WIN
# =====================================================

def show_win():

    total = (
        pygame.time.get_ticks() - start_time
    ) // 1000

    text = title_font.render(
        "YOU ESCAPED!",
        True,
        GREEN
    )

    screen.blit(text, (210, 280))

    text2 = font.render(
        f"Completed in {total} sec",
        True,
        WHITE
    )

    screen.blit(text2, (240, 340))

    if level < len(levels)-1:

        text3 = font.render(
            "Press N For Next Level",
            True,
            GOLD
        )

        screen.blit(text3, (180, 390))

    else:

        text4 = font.render(
            "ALL LEVELS COMPLETED",
            True,
            GOLD
        )

        screen.blit(text4, (180, 390))

# =====================================================
# LOOP
# =====================================================

running = True

while running:

    clock.tick(15)

    screen.fill(BLACK)

    draw_maze()
    draw_exit()
    draw_coins()
    draw_player()
    draw_torch()
    draw_ui()

    # COINS

    for coin in coins[:]:

        if (px,py) == coin:

            coins.remove(coin)

            score += 1

    # WIN

    if px == gx and py == gy:

        won = True

        show_win()

    # EVENTS

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

            sys.exit()

        if event.type == pygame.KEYDOWN:

            if won and event.key == pygame.K_n:

                next_level()

            if not won:

                nx = px
                ny = py

                if event.key == pygame.K_LEFT:

                    nx -= 1

                if event.key == pygame.K_RIGHT:

                    nx += 1

                if event.key == pygame.K_UP:

                    ny -= 1

                if event.key == pygame.K_DOWN:

                    ny += 1

                if (
                    0 <= nx < ROWS and
                    0 <= ny < ROWS and
                    maze[ny][nx] == 0
                ):

                    px = nx
                    py = ny

    pygame.display.flip()