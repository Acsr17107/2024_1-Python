import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('마우스로 그림 그리기')

RED = (255, 0, 0)

mdown = False
mpos = []
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mdown = True
        elif event.type == pygame.MOUSEMOTION:
            if mdown:
                mpos.append(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            mdown = False
    
    screen.fill((255, 255, 255))

    for x, y in mpos:
        pygame.draw.circle(screen, RED, [x, y], 2)
    pygame.display.flip()

pygame.quit()