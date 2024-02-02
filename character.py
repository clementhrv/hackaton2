import pygame
import time
class Character:


    def __init__(self, position):
        self.pos = position
        self.sheet = pygame.image.load("images/protagonist.gif")
        print(self.sheet.get_width())
        self.Sprites = {}
        self.dir = "up"


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
        
        if self.ticks == 5000:
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




