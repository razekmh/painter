import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the HyperPixel display
width, height = 800, 480
screen = pygame.display.set_mode((width, height))

# Load the image from the file
image = pygame.image.load("output_image.png")

# Initial position of the square
square_x, square_y = 100, 100

# Speed and direction of the square movement
speed = 5
direction = (1, 1)  # (1, 1) means moving diagonally down and to the right

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the position of the square
    square_x += speed * direction[0]
    square_y += speed * direction[1]

    # Bounce off the screen edges (optional)
    if square_x <= 0 or square_x + image.get_width() >= width:
        direction = (-direction[0], direction[1])
    if square_y <= 0 or square_y + image.get_height() >= height:
        direction = (direction[0], -direction[1])

    # Draw the image on the screen
    screen.fill((255, 255, 255))  # Clear the screen with a white background
    screen.blit(image, (square_x, square_y))

    # Update the display
    pygame.display.flip()

    # Add a small delay to control the frame rate
    pygame.time.delay(10)
