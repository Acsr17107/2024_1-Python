import pygame
import time

rgbs = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
colors = ['black', 'red', 'green', 'blue', 'yellow']
pygame.init()

screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont(None, 50)

index = 0
do = 1

while do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = 0
    
    screen.fill(rgbs[index])
    text_color = rgbs[(index + 1) % len(rgbs)]
    text = font.render(colors[index], True, text_color)
    text_rect = text.get_rect(center=(200, 150))
    screen.blit(text, text_rect)

    pygame.display.flip()
    time.sleep(1)
    index = (index + 1) % len(rgbs)

pygame.quit()