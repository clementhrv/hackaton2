import pygame
import timeit
from character import Protagonist
from antagonist import Antagonist


dim = (512, 512)
screen = pygame.display.set_mode(dim)


t = timeit.default_timer()
a = Protagonist((100, 100))
b = Antagonist((100, 50))

running = True
while running :
    delta = timeit.default_timer() - t
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, dim[0], dim[1]))
    key = pygame.key.get_pressed()
    a.update(key, delta)
    a.render(screen)
    b.update(a.pos, delta)
    b.render(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    t = timeit.default_timer()
