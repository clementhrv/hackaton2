import pygame
import time
import numpy as np
import math
from skimage.draw import line


class Protagonist:

    def __init__(self, position):
        self.pos = position
        self.sheet = pygame.image.load("images/protagonist.gif")
        print(self.sheet.get_width())
        self.Sprites = {}
        self.dir = "up"
        self.health = 100


        dir = ["up", "down", "left", "right"]
        for d in dir:
            self.Sprites[d] = []
        crops = [[(-70, -8), (-99, -8)], [(-73, -280), (-43, -280)],[(-38, -109), (-68, -109)], [(-262, -110), (-292, -110)]]
        for i in range(4):
            for j in range(2):
                surf = pygame.Surface((30, 30))
                surf.blit(self.sheet, crops[i][j])
                self.Sprites[dir[i]].append(surf)

        self.ticks = 0
        self.state = False
        self.sprite = surf

    def get_map_pos(self):
        x, y = self.pos
        return int(x / 8), int(y / 8)

    def check_collision(self, map, dir):
        x, y = self.get_map_pos()
        dx, dy = dir
        if map[x+dx, y+dy] == 1:
            return False







    def animate(self):

        if self.ticks > 800:
            self.state = not self.state
            self.ticks = 0
        self.sprite = self.Sprites[self.dir][int(self.state)]

    def render(self, screen):
        self.animate()
        pygame.draw.rect(screen, (0, 100, 255), (self.pos[0], self.pos[1], 10, 10))
        screen.blit(self.sprite, self.pos)

    def update(self, key, t, map):
        px,py = self.get_map_pos()
        x, y = self.pos
        if key[pygame.K_LEFT] and map[px-1, py] != 0:
            x -= 100000*t
            self.dir = "left"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_RIGHT] and map[px+1, py] != 0:
            x += 100000*t
            self.dir = "right"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_UP] and map[px, py-1] != 0:
            y -= 100000*t
            self.dir = "up"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_DOWN] and map[px, py+1] != 0:
            y += 100000*t
            self.dir = "down"
            self.ticks += 1
        if key[pygame.K_a]:
            print(px, py)
        self.pos = (x, y)




    def visible(self, coords, map):
        x,y = self.get_map_pos()
        rr, cc = line(coords[0], coords[1], x, y)
        l = len(rr)
        for i in range(1, l-1) :
            if map[rr[i], cc[i]] == 0:
                return False, 0, 0
        return True, rr, cc
    def get_distance(self, coords):
        return math.sqrt((self.pos[0]-coords[0])**2+(self.pos[1]-coords[1])**2)


    def render_light(self, screen, map, Wx, Wy):
        Walls = []

        for i in range(len((Wx))):
            x = Wx[i]
            y = Wy[i]
            if self.get_distance((x*8,y*8)) < 100:
                bool, rx, ry = self.visible((x,y), map)
                if bool:
                    Walls.append([x*8,y*8])


        lowest = min(Walls, key=lambda x: (x[1], x[0]))
        vertices = sorted(Walls, key=lambda x: math.atan2(x[1] - lowest[1], x[0] - lowest[0]) + 2 * math.pi)
        pygame.draw.polygon(screen, (100, 255, 0), vertices)
        for x,y in Walls:
            pygame.draw.rect(screen, (0, 0, 255), ((x), (y), 8, 8))
        """l = len(rx)
                for i in range(1, l - 1):
                    pygame.draw.rect(screen, (100, 255, 0), ((rx[i])*8,(ry[i])*8, 8, 8))
                





        return Wx"""




