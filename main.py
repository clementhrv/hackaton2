import pygame
import numpy as np
import math

dim = (512, 512)
screen = pygame.display.set_mode(dim)

p_pos = (3, 3)
p_angle = 0

map = [[1, 1, 1, 1, 1, 1,
       0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0,
       1, 1, 1, 1, 1, 1],

       [1, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 1]]
map_dim = (6, 6)


def get_angles(i, fov, dim, angle):
    return (angle + (i*fov)/dim)


def convert_map(map, map_dim):
    new_map = []
    for i in range(map_dim[1]):
        line = []
        for j in range(map_dim[0]):
            line.append((map[0][i*map_dim[0] +j],
                         map[1][i*map_dim[0] +j]))
        new_map.append(line)
    return np.array(new_map)





def cast_ray(pos, angle, map, map_dim):
    direction = (math.cos(angle), math.sin(angle))
    abs_direction = (math.copysign(1, direction[0]), math.copysign(1, direction[1]))
    D = {-1 : math.floor, 1:math.ceil}
    next_x = D[abs_direction[0]](pos(0))
    coords_nextx = (next_x, pos[1] + direction[1] * ((pos[0] - next_x) / direction[0]))

    next_y = D[abs_direction[1]](pos(1))
    coords_nexty = (pos[0] + direction[0] * ((pos[1] - next_x) / direction[1]), next_y)

    i = 0
    while 0 <= pos[0] <= map_dim[0] and 0 <= pos[1] <= map_dim[1] and map[int(pos[0]), int(pos[1])]:




        a = 1
    pass


running = True
while running :




    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False