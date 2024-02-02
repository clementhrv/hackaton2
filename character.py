import pygame
class Character:


    def __init__(self, position):
        self.pos = position
        self.sheet = pygame.image.load("8596005_orig.gif")

        self.sprite = pygame.Surface((100, 0))
        self.sprite.blit(self.sheet, (30, 30))

    def render(self, screen):
        pygame.draw.rect(screen, (0, 100, 255), (self.pos[0], self.pos[1], 10, 10))
        self.sprite.blit(screen, self.pos)

    def update(self, key, t):
        x = self.pos[0]
        y = self.pos[1]
        if key[pygame.K_LEFT]:
            x -= 100000*t
        self.pos = (x, y)
        if key[pygame.K_RIGHT]:
            x += 100000*t
        self.pos = (x, y)
        if key[pygame.K_UP]:
            y -= 100000*t
        self.pos = (x, y)
        if key[pygame.K_DOWN]:
            y += 100000*t
        self.pos = (x, y)


