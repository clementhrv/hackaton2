import pygame
class Character:


    def __init__(self, position):
        self.pos = position

    def render(self, screen):
        pygame.draw.rect(screen, (0, 100, 255), (self.pos[0], self.pos[1], 10, 10))

    def update(self, key, t):
        x = self.pos[0]
        y = self.pos[1]
        if key[pygame.K_LEFT]:
            x -= 10000*t
        self.pos = (x, y)



