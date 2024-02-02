import numpy as np
import pygame



class Coin():

    def __init__(self, init_map):
        self.init_map = init_map
        self.map = np.zeros((64, 64))


    def coin_generation(self, init_map, coin_probability=0.2):
        random_map = (np.random.rand(64, 64)<coin_probability).astype(int)
        coin_map = (random_map+init_map==2).astype(int)
        total_map = init_map + coin_map
        self.map = total_map


    def 
