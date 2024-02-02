import numpy as np
import pygame

class Mapfinale:

    def __init__(self, init_map):
        self.init_map = init_map
        self.map = np.zeros((64, 64))

    def coin_generation(self, init_map, coin_probability=0.01):
        mask = np.random.rand(64, 64) < coin_probability
        init_map = np.where((init_map == 1) & mask, 2, init_map)
        return init_map  

    def coeur_generation(self, init_map, coeur_probability=0.01):
        mappiece = self.coin_generation(init_map)
        mask = np.random.rand(64, 64) < coeur_probability
        mappiece = np.where((mappiece == 1) & mask, 3, mappiece)
        return mappiece  

    def affichage(self, screen, map):
        cell_size = 8
        for row_index, row in enumerate(map):
            for col_index, value in enumerate(row):
                if value == 1:
                    color = (255, 255, 255)
                    pygame.draw.rect(screen, color, (col_index * cell_size, row_index * cell_size, cell_size, cell_size))
                elif value == 2:
                    color = (255, 0, 255)  # pièce
                    pygame.draw.rect(screen, color, (col_index * cell_size, row_index * cell_size, cell_size, cell_size))
                elif value == 3:
                    color = (255, 255, 0)  # coeur
                    pygame.draw.rect(screen, color, (col_index * cell_size, row_index * cell_size, cell_size, cell_size))





    
