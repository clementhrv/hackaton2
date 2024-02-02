import pygame
import timeit
from character import Character


dim = (512, 512)
screen = pygame.display.set_mode(dim)


t = timeit.default_timer()
a = Character((100, 100))

running = True
while running :
    delta = timeit.default_timer() - t
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, dim[0], dim[1]))
    key = pygame.key.get_pressed()
    a.update(key, delta)
    a.render(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    t = timeit.default_timer()
