import pygame
import random
pygame.init()

screen_width, screen_height = 480, 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

def write_text_sideways(text):
    font = pygame.font.Font(None, 50)
    text = font.render(text, 0, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.centerx = screen_height / 2.0
    text_rect.centery = screen_width / 2.0
    screen.blit(text, text_rect)
    screen.blit(pygame.transform.rotate(screen, 90), (0, 0))
    pygame.display.flip()

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    screen.fill((0,0,0))
    #draw_two_rects() 
    write_text_sideways("HyperText")
    pygame.display.update()    

pygame.quit()
    # create text for later display

