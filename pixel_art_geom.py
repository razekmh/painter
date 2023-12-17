import pygame
import random

pygame.init()

screen_width, screen_height = 480, 800
sqr_left = 10
sqr_top = 10
sqr_width = 10
sqr_height = 10

size_of_cell = 5
count_of_rows = int(screen_width / size_of_cell)
count_of_cols = int(screen_height / size_of_cell)
sqr_width = sqr_height = size_of_cell
badding = int(size_of_cell / 5)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


def draw_two_rects():
    base_rectangle = pygame.Rect(sqr_left, sqr_top, sqr_width, sqr_height)
    end_rectangle = pygame.Rect(
        screen_width - sqr_left, screen_height - sqr_top, sqr_width, sqr_height
    )
    pygame.draw.rect(screen, (0, 0, 255), base_rectangle)
    pygame.draw.rect(screen, (0, 255, 0), end_rectangle)


def create_dict_of_squares():
    dict_of_squares = {}
    square_index = 0
    for i in range(0, count_of_rows):
        for j in range(0, count_of_cols):
            white_colour = (255, 255, 255)
            dict_of_squares[square_index] = (
                pygame.Rect(
                    (i * size_of_cell) + badding,
                    (j * size_of_cell) + badding,
                    sqr_width - badding,
                    sqr_height - badding,
                ),
                white_colour,
            )

            square_index = +1

    return dict_of_squares


def draw_squares_from_dict(dict_of_squares):
    for square_index, square_info in dict_of_squares.items():
        pass


def draw_grid_of_squares():
    for i in range(0, count_of_rows):
        for j in range(0, count_of_cols):
            colour = (
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255),
            )
            target_rect = pygame.Rect(
                (i * size_of_cell) + badding,
                (j * size_of_cell) + badding,
                sqr_width - badding,
                sqr_height - badding,
            )
            pygame.draw.rect(screen, colour, target_rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    screen.fill((0, 0, 0))
    # draw_two_rects()
    draw_grid_of_squares()
    pygame.display.update()

pygame.quit()
