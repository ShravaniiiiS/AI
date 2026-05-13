import pygame
import random
import sys

pygame.init()


WIDTH = 700
HEIGHT = 760

ROWS = 14
CELL = WIDTH // ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Maze Escape")

clock = pygame.time.Clock()



WHITE = (245,245,245)
BLACK = (25,25,35)
BLUE = (59,130,246)
GREEN = (34,197,94)
RED = (239,68,68)
YELLOW = (250,204,21)
GRAY = (180,180,180)
BG = (15,23,42)



title_font = pygame.font.SysFont("Arial", 42, bold=True)
font = pygame.font.SysFont("Arial", 28)


mazes = [

[
[0,1,0,0,0,0,0,1,0,0,0,0,0,0],
[0,1,0,1,1,1,0,1,0,1,1,1,1,0],
[0,0,0,1,0,0,0,0,0,1,0,0,1,0],
[1,1,0,1,0,1,1,1,0,1,0,0,1,0],
[0,0,0,0,0,1,0,0,0,0,0,1,0,0],
[0,1,1,1,0,1,0,1,1,1,0,1,1,0],
[0,0,0,1,0,0,0,1,0,0,0,0,0,0],
[1,1,0,1,1,1,0,1,0,1,1,1,0,1],
[0,0,0,0,0,1,0,0,0,1,0,0,0,0],
[0,1,1,1,0,1,1,1,0,1,0,1,1,0],
[0,0,0,1,0,0,0,1,0,0,0,0,0,0],
[1,1,0,1,1,1,0,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,1,1,1,1,0,0,0]
],

[
[0,0,0,1,0,0,0,0,1,0,0,0,0,0],
[1,1,0,1,0,1,1,0,1,0,1,1,1,0],
[0,0,0,0,0,1,0,0,0,0,0,0,1,0],
[0,1,1,1,0,1,0,1,1,1,1,0,1,0],
[0,0,0,1,0,0,0,0,0,0,1,0,0,0],
[1,1,0,1,1,1,1,1,1,0,1,1,1,0],
[0,0,0,0,0,0,0,0,1,0,0,0,1,0],
[0,1,1,1,1,1,1,0,1,1,1,0,1,0],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0],
[1,1,1,1,1,0,1,1,1,0,1,1,1,0],
[0,0,0,0,1,0,0,0,1,0,0,0,0,0],
[0,1,1,0,1,1,1,0,1,1,1,1,1,0],
[0,0,0,0,0,0,1,0,0,0,0,0,1,0],
[1,1,1,1,1,0,0,0,1,1,1,0,0,0]
]

]



current_maze = random.choice(mazes)

player_x = 0
player_y = 0

goal_x = ROWS - 1
goal_y = ROWS - 1

game_won = False



def reset_same_maze():

    global player_x, player_y, game_won

    player_x = 0
    player_y = 0
    game_won = False


def load_new_maze():

    global current_maze
    global player_x
    global player_y
    global game_won

    current_maze = random.choice(mazes)

    player_x = 0
    player_y = 0

    game_won = False


def draw_maze():

    for row in range(ROWS):

        for col in range(ROWS):

            rect = pygame.Rect(
                col * CELL,
                row * CELL,
                CELL,
                CELL
            )

            if current_maze[row][col] == 1:

                pygame.draw.rect(screen, BLACK, rect)

            else:

                pygame.draw.rect(screen, WHITE, rect)

            pygame.draw.rect(screen, GRAY, rect, 1)


def draw_player():

    pygame.draw.circle(
        screen,
        BLUE,
        (
            player_x * CELL + CELL // 2,
            player_y * CELL + CELL // 2
        ),
        CELL // 3
    )


def draw_goal():

    pygame.draw.rect(
        screen,
        GREEN,
        (
            goal_x * CELL + 10,
            goal_y * CELL + 10,
            CELL - 20,
            CELL - 20
        )
    )


def draw_ui():

    title = title_font.render("Maze Escape", True, WHITE)

    screen.blit(title, (220, 705))

    # Restart Button
    restart_btn = pygame.Rect(20, 705, 150, 40)

    pygame.draw.rect(
        screen,
        RED,
        restart_btn,
        border_radius=10
    )

    restart_text = font.render("Restart", True, WHITE)

    screen.blit(restart_text, (45, 712))

    # New Puzzle Button
    new_btn = pygame.Rect(520, 705, 160, 40)

    pygame.draw.rect(
        screen,
        BLUE,
        new_btn,
        border_radius=10
    )

    new_text = font.render("New Puzzle", True, WHITE)

    screen.blit(new_text, (532, 712))

    return restart_btn, new_btn


def show_win():

    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0,0,0))

    screen.blit(overlay, (0,0))

    text = title_font.render("YOU ESCAPED!", True, YELLOW)

    screen.blit(text, (180, 300))

    text2 = font.render(
        "Press New Puzzle for another maze",
        True,
        WHITE
    )

    screen.blit(text2, (150, 370))


# ------------------------------------------
# GAME LOOP
# ------------------------------------------

running = True

while running:

    clock.tick(60)

    screen.fill(BG)

    draw_maze()
    draw_goal()
    draw_player()

    restart_button, new_button = draw_ui()

    # WIN CHECK

    if player_x == goal_x and player_y == goal_y:

        game_won = True
        show_win()

    # EVENTS

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            sys.exit()

        # BUTTON CLICKS

        if event.type == pygame.MOUSEBUTTONDOWN:

            if restart_button.collidepoint(event.pos):

                reset_same_maze()

            if new_button.collidepoint(event.pos):

                load_new_maze()

        # KEYBOARD CONTROLS

        if event.type == pygame.KEYDOWN:

            if not game_won:

                new_x = player_x
                new_y = player_y

                if event.key == pygame.K_LEFT:

                    new_x -= 1

                if event.key == pygame.K_RIGHT:

                    new_x += 1

                if event.key == pygame.K_UP:

                    new_y -= 1

                if event.key == pygame.K_DOWN:

                    new_y += 1

                # COLLISION CHECK

                if (
                    0 <= new_x < ROWS and
                    0 <= new_y < ROWS and
                    current_maze[new_y][new_x] == 0
                ):

                    player_x = new_x
                    player_y = new_y

    pygame.display.update()