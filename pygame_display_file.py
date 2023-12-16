import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the HyperPixel display
width, height = 800, 480
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

# Load the image from the file
image = pygame.image.load("output_image.png")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the image on the screen
    screen.blit(image, (0, 0))

    # Update the display
    pygame.display.flip()
