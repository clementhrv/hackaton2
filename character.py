import pygame
import time

class Protagonist:

    def __init__(self, position):
        self.pos = position
        self.sheet = pygame.image.load("images/protagonist.gif")
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

    def update(self, key, t):
        x = self.pos[0]
        y = self.pos[1]
        if key[pygame.K_LEFT]:
            x -= 100000*t
            self.dir = "left"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_RIGHT]:
            x += 100000*t
            self.dir = "right"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_UP]:
            y -= 100000*t
            self.dir = "up"
            self.ticks += 1
        self.pos = (x, y)
        if key[pygame.K_DOWN]:
            y += 100000*t
            self.dir = "down"
            self.ticks += 1
        self.pos = (x, y)


