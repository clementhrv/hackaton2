import numpy as np
import pygame
import time

class Antagonist:

    def __init__(self, position):
        self.pos = position
        self.sheet = pygame.image.load("images/antagonist.gif")
        print(self.sheet.get_width())
        self.Sprites = {}
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
        self.dir = "up"

    def animate(self):
        if self.ticks == 1000:
            self.state = not self.state
            self.ticks = 0
        self.sprite = self.Sprites[self.dir][int(self.state)]

    def render(self, screen):
        self.animate()
        pygame.draw.rect(screen, (0, 100, 255), (self.pos[0], self.pos[1], 10, 10))
        screen.blit(self.sprite, self.pos)

    def update(self, protagonist_pos, t):
        x = self.pos[0]
        y = self.pos[1]
        xp = protagonist_pos[0]
        yp = protagonist_pos[1]
        angle_direction = np.arctan2(yp-y, xp-x)
        print(angle_direction)
        
        if (angle_direction >= -np.pi and angle_direction < -5*np.pi/4) or (angle_direction >= 5*np.pi/4 and angle_direction < np.pi):
            x += 10000*t
            self.dir = "left"
            self.ticks += 1
        if angle_direction <= -np.pi/4  and angle_direction < np.pi/4:
            x -= 10000*t
            self.dir = "right"
            self.ticks += 1
        self.pos = (x, y)
        if angle_direction >= np.pi/4 and angle_direction < 3*np.pi/4:
            y += 10000*t
            self.dir = "up"
            self.ticks += 1
        self.pos = (x, y)
        if angle_direction >= -3*np.pi/4 and angle_direction < -np.pi/4:
            y -= 10000*t
            self.dir = "down"
            self.ticks += 1
        self.pos = (x, y)      



"""
        if key[pygame.K_q]:
            x -= 100000*t
            self.dir = "left"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_d]:
            x += 100000*t
            self.dir = "right"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_z]:
            y -= 100000*t
            self.dir = "up"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_s]:
            y += 100000*t
            self.dir = "down"
            self.ticks += 1
        self.pos = (x, y)

"""
