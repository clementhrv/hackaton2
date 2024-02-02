from knn import knn
import random as rd

dico_salles = {}

class Salle :
    def __init__(self, position, hauteur, largeur, voisins = [], nb_voisins= 0) :
        self.position = position
        self.dimension = hauteur, largeur
        self.portes = []
        self.voisins = voisins #position des voisins
        self.nb_voisins = nb_voisins
        self.sommets = []
        

    def print_info(self) :
        print("Salle de position : " + str(self.position) + " de dimension : " + str(self.dimension) + " et de porte : " + str(self.porte))

    def set_sommet(self) :
        self.sommets = [(self.position[0], self.position[1]), (self.position[0] + self.dimension[1], self.position[1]), (self.position[0] + self.dimension[1], self.position[1] + self.dimension[0]), (self.position[0], self.position[1] + self.dimension[0])]

    def set_voisins(self, liste_salles) :
        for i in range(self.nb_voisins) :
            self.voisins.append((knn(self.position, liste_salles)))

    def set_porte(self, voisin) :
        val = rd.random()
        if val < 0.5 :
            if voisin[0] > self.position[0] :
                self.portes.append(("droite", self.sommets[2][0], rd.randint(self.sommets[1][1], self.sommets[2][1])))
            else : 
                self.portes.append(("gauche", self.sommets[0][0], rd.randint(self.sommets[0][1], self.sommets[3][1])))
        else :
            if self.voisins[i][1] > self.position[1] :
                self.portes.append(("haut", rd.randint(self.sommets[3][0], self.sommets[3][0]), self.sommets[2][1]))
            else :
                self.portes.append(("bas", rd.randint(self.sommets[0][0], self.sommets[1][0]), self.sommets[0][1]))
    
    def get_voisins(self) :
        return self.voisins
    
    def get_portes(self):
        return self.portes


class Chemin :
    def __init__(self, width, porte1, porte2) :
        self.porte1 = porte1
        self.porte2 = porte2
        self.coord = [min(porte1[0], porte2[0]), max(porte1[0], porte2[0]), min(porte1[1], porte2[1]), max(porte1[1], porte2[1])]
        self.virage = []
        self.listepoints = []
        self.width = width
    
    def random_virage(self) :
        nb_point = rd.randint(0,2)
        virage = []
        for i in range(nb_point) :
            virage.append((rd.randint(,self.width), rd.randint(0,self.width)))
        self.virage = virage
        


    def creer_chemin(self) :


    def set_listepoints(self) :
        self.listepoints.append(self.porte1)
        for x in self.virage :
            self.listepoints.append(x)
        self.listepoints.append(self.porte2)

    


def relier_salles(coord_salle):
    current_salle = dico_salles[coord_salle]
    voisins = current_salle.get_voisins()
    for i in range(len(voisins)) :
        coord_salle_voisine = voisins[i]
        salle_voisine = dico_salles[coord_salle_voisine]
        current_salle.set_portes(coord_salle_voisine)
        salle_voisine.set_portes(current_salle.get_portes())[-1]
        


        




