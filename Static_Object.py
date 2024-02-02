from PIL import Image
import numpy as np
import knn
import random as rd
import matplotlib.pyplot as plt
NB_SALLES = 12
MAP_SIZE = 64
SIZE_MAX_SALLE = 16
SIZE_MIN_SALLE = 5





def point_intermediaire(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2 :
        return (x1, rd.randint(min(y1, y2), max(y1, y2)))
    elif y1 == y2 :
        return (rd.randint(min(x1, x2), max(x1, x2)), y1)
    else :
        val = rd.random()
        if val < 0.5 :
            return (x1, y2)
        else:
            return (x2, y1)


class Salle :
    def __init__(self, position, hauteur, largeur) :
        self.position = position
        self.dimension = hauteur, largeur
        self.portes = []
        self.voisins = [] #position des voisins
        self.nb_voisins = rd.randint(1, 3)
        self.sommets = []
        

    def print_info(self) :
        print("Salle de position : " + str(self.position) + " de dimension : " + str(self.dimension) + " et de porte : " + str(self.porte))

    def set_sommet(self) :
        self.sommets = [(self.position[0], self.position[1]), (self.position[0] + self.dimension[1], self.position[1]), (self.position[0] + self.dimension[1], self.position[1] + self.dimension[0]), (self.position[0], self.position[1] + self.dimension[0])]

    def set_voisins(self, liste_salles) :
        self.voisins = knn.knn(self.nb_voisins, self.position, liste_salles)

    def set_porte(self, voisin) :
        val = rd.random()
        if val < 0.5 :
            if voisin[0] > self.position[0] :
                self.portes.append((self.sommets[2][0], rd.randint(self.sommets[1][1], self.sommets[2][1])))
            else : 
                self.portes.append((self.sommets[0][0], rd.randint(self.sommets[0][1], self.sommets[3][1])))
        else :
            if voisin[1] > self.position[1] :
                self.portes.append((rd.randint(self.sommets[3][0], self.sommets[3][0]), self.sommets[2][1]))
            else :
                self.portes.append((rd.randint(self.sommets[0][0], self.sommets[1][0]), self.sommets[0][1]))
    
    def get_voisins(self) :
        return self.voisins
    
    def get_portes(self):
        return self.portes


class Chemin :
    def __init__(self, width, debut, fin) :
        self.debut = debut
        self.fin = fin
        self.coord = [min(debut[0], fin[0]), max(debut[0], fin[0]), min(debut[1], fin[1]), max(debut[1], fin[1])]
        self.virage = []
        self.listepoints = []
        self.width = width
    
    def creer_chemin(self) :
        nb_point = rd.randint(0,2)
        virage_temp = []
        virage = []
        for i in range(nb_point) :
            virage_temp.append((rd.randint(self.coord[0], self.coord[1]), rd.randint(self.coord[2], self.coord[3])))
        if nb_point !=0:
            virage.append(point_intermediaire(self.debut, virage_temp[0]))
            for i in range(nb_point-1):
                virage.append(virage_temp[i])
                virage.append(point_intermediaire(virage_temp[i], virage_temp[i+1]))
            virage.append(virage_temp[nb_point-1])
            virage.append(point_intermediaire(virage_temp[nb_point-1], self.fin)) 
        else:
            virage.append(point_intermediaire(self.debut, self.fin)) 
        self.virage = virage   


    def set_listepoints(self) :
        self.listepoints.append(self.debut)
        for x in self.virage :
            self.listepoints.append(x)
        self.listepoints.append(self.fin)

    def get_listepoints(self) :
        return self.listepoints
    
def relier_salles(coord_salle, dico_salles):
    voisins = dico_salles[coord_salle].get_voisins()
    chemins = []
    for i in range(len(voisins)) :
        coord_salle_voisine = voisins[i]
        dico_salles[coord_salle].set_porte(coord_salle_voisine)
        dico_salles[coord_salle_voisine].set_porte(coord_salle)
        chemins.append((dico_salles[coord_salle].get_portes()[-1], dico_salles[coord_salle_voisine].get_portes()[-1]))
    return dico_salles, chemins

def check_connection(dico_salle):
    L = {}
    i = 0
    for x in dico_salle.keys() :
        L[x] = i
        i += 1
    for z in dico_salle.keys():
        for x in dico_salle.keys() :
            voisins = dico_salle[x].get_voisins()
            for y in voisins :
                if L[y] <= L[x] :
                    L[y] = L[x]
                else :
                    L[x] = L[y]
    for x in dico_salle.keys() :
        if L[x] != 0 :
            return False
    return True






def generer_salles():
    dico_salle = {}
    liste_coord_salle = []
    liste_coord_chemin = []
    dico_chemin = {}
    for i in range(NB_SALLES//4):
        X_pos = rd.randint(0, (MAP_SIZE)//2)
        Y_pos = rd.randint((MAP_SIZE)//2, MAP_SIZE - SIZE_MAX_SALLE)
        hauteur = rd.randint(SIZE_MIN_SALLE, SIZE_MAX_SALLE)
        largeur = rd.randint(SIZE_MIN_SALLE, SIZE_MAX_SALLE)
        liste_coord_salle.append((X_pos,Y_pos))
        dico_salle[(X_pos, Y_pos)] = Salle((X_pos, Y_pos), hauteur, largeur)
    for i in range(NB_SALLES//4):
        X_pos = rd.randint((MAP_SIZE)//2, MAP_SIZE - SIZE_MAX_SALLE)
        Y_pos = rd.randint(0, (MAP_SIZE)//2)
        hauteur = rd.randint(SIZE_MIN_SALLE, SIZE_MAX_SALLE)
        largeur = rd.randint(SIZE_MIN_SALLE, SIZE_MAX_SALLE)
        liste_coord_salle.append((X_pos,Y_pos))
        dico_salle[(X_pos, Y_pos)] = Salle((X_pos, Y_pos), hauteur, largeur)
    for i in range(NB_SALLES//4):
        X_pos = rd.randint(0, (MAP_SIZE)//2)
        Y_pos = rd.randint(0, (MAP_SIZE)//2)
        hauteur = rd.randint(SIZE_MIN_SALLE, SIZE_MAX_SALLE)
        largeur = rd.randint(SIZE_MIN_SALLE, SIZE_MAX_SALLE)
        liste_coord_salle.append((X_pos,Y_pos))
        dico_salle[(X_pos, Y_pos)] = Salle((X_pos, Y_pos), hauteur, largeur)
    for i in range(NB_SALLES//4):
        X_pos = rd.randint((MAP_SIZE)//2, MAP_SIZE - SIZE_MAX_SALLE)
        Y_pos = rd.randint((MAP_SIZE)//2, MAP_SIZE - SIZE_MAX_SALLE)
        hauteur = rd.randint(SIZE_MIN_SALLE, SIZE_MAX_SALLE)
        largeur = rd.randint(SIZE_MIN_SALLE, SIZE_MAX_SALLE)
        liste_coord_salle.append((X_pos,Y_pos))
        dico_salle[(X_pos, Y_pos)] = Salle((X_pos, Y_pos), hauteur, largeur)
    for x in dico_salle.keys():
        dico_salle[x].set_sommet()
        dico_salle[x].set_voisins(liste_coord_salle)
    for x in dico_salle.keys():
        dico_salle, chemins = relier_salles(x, dico_salle)
        for y in chemins:
            liste_coord_chemin.append(y)
    for x in liste_coord_chemin:
        dico_chemin[x] = Chemin(1, [x[0][0], x[0][1]], [x[1][0], x[1][1]])
        dico_chemin[x].creer_chemin()
        dico_chemin[x].set_listepoints()
    return dico_salle, dico_chemin, liste_coord_salle, liste_coord_chemin



def print_map(map):
    for x in map:
        print(x)

def set_map(dico_salle, dico_chemin):
    map = np.zeros((MAP_SIZE, MAP_SIZE))
    for x in dico_salle.keys():
        piece = dico_salle[x]
        for i in range(piece.sommets[0][0], piece.sommets[2][0]):
            for j in range(piece.sommets[0][1], piece.sommets[2][1]):
                map[i][j] = 1
    for x in dico_chemin.keys():
        points = dico_chemin[x].get_listepoints()
        print(points)
        for j in range(len(points)-1):
            x1, y1 = points[j]
            x2, y2 = points[j+1]
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    map[x1][i] = 1
            else:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    map[i][y2] = 1
    for i in range(MAP_SIZE):
        map[i][0] = 0
        map[i][MAP_SIZE-1] = 0
        map[0][i] = 0
        map[MAP_SIZE-1][i] = 0
    return map


def mask_mur(map):
    mask = np.ones((MAP_SIZE, MAP_SIZE))
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            if map[i][j] == 0:
                if (i-1 > 0 and map[i-1][j] == 1) or (i+1 < MAP_SIZE and map[i+1][j] == 1) or (j-1 > 0 and map[i][j-1] == 1) or (j+1 < MAP_SIZE and map[i][j-1] == 1) or ((i-1 > 0) and (j-1 > 0) and (map[i-1][j-1] == 1)) or ((i+1 < MAP_SIZE) and (j-1 > 0) and (map[i+1][j-1] == 1)) or ((i+1 < MAP_SIZE) and (j+1 < MAP_SIZE) and (map[i+1][j+1] == 1)) or ((i-1 > 0)  and (j+1 < MAP_SIZE) and (map[i-1][j+1] == 1)) :
                    mask[i][j] = 0
                else :
                    mask[i][j] = 9
                
    return mask
                

def generate_all():
    dico_salle, dico_chemin, liste_coord_salle, liste_coord_chemin = generer_salles()
    while not check_connection(dico_salle):
        dico_salle, dico_chemin, liste_coord_salle, liste_coord_chemin = generer_salles()
        print(check_connection(dico_salle))
    temp = set_map(dico_salle, dico_chemin)

    plt.imshow(temp, cmap='hot')
    plt.show()

    plt.imshow(mask_mur(temp), cmap='hot')
    plt.show()

    return mask_mur(temp)



generate_all()





    




