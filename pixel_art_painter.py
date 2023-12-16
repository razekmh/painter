import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the HyperPixel display
width, height = 800, 480
screen = pygame.display.set_mode((width, height))

# Create a simple smiley face pixel art
pixel_art = [
    "    1111    ",
    "   111111   ",
    "  11111111  ",
    " 1111111111 ",
    "  11111111  ",
    "   111111   ",
    "    1111    "
]

# Define pixel colors
pixel_colors = {
    '0': (255, 255, 255),  # White
    '1': (255, 0, 0)        # Red
}

# Calculate pixel size based on screen dimensions and pixel art size
pixel_size = min(width // len(pixel_art[0]), height // len(pixel_art))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the pixel art on the screen
    screen.fill((0, 0, 0))  # Clear the screen with a black background

    for y, row in enumerate(pixel_art):
        for x, pixel in enumerate(row):
            color = pixel_colors.get(pixel, (0, 0, 0))
            pygame.draw.rect(screen, color, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))

    # Update the display
    pygame.display.flip()

    # Add a small delay to control the frame rate
    pygame.time.delay(100)

