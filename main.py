import pygame
import timeit
import numpy as np

from character import Protagonist
from antagonist import Antagonist
from coin import Mapfinale   #no


dim = (512, 512)
screen = pygame.display.set_mode(dim)

init_map = np.zeros((64, 64)) #no
init_map[30]=[1]*64 #no
init_map[40]=[1]*64 #no
init_map[50]=[1]*64 #no

t = timeit.default_timer()
a = Protagonist((100, 100))
b = Antagonist((100, 50))

map = Mapfinale(init_map) #no
mappiece = map.coin_generation(init_map) #no
finalmap = map.coeur_generation(mappiece) #no


running = True
while running :
    delta = timeit.default_timer() - t
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, dim[0], dim[1]))

    map.affichage(screen, finalmap) #no
    
    key = pygame.key.get_pressed()
    a.update(key, delta,finalmap)
    a.render(screen)
    b.update(a.pos, delta)
    b.render(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    t = timeit.default_timer()
