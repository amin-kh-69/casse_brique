""" Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier python contient le code du jeu du cassse briques

Il reste à coder la boucle principale du projet et régler les potentiels problèmes
"""

import tkinter as tk
import random
from affichage import Affichage
from raquette import Raquette
from balle import Balle
from brique import Brique

class jeu:
    def __init__(self):
        self.affichage = Affichage()
        self.raquette = Raquette(300, 500, 20, 100, 15, 'blue')
        self.balle = Balle(400, 300, 3, 3, 5, 'red')
        self.brique = [Brique(x * self.affichage.largeur//10 + 30, y * 30 + 50, self.affichage.largeur//10, 20) for x in range(10) for y in range(5)]
        self.affichage.root.bind("<Left>", self.gauche)
        self.affichage.root.bind("<Right>", self.droite)

    def gauche(self, event = None):
        self.raquette.direction = -1
    
    def droite(self, event = None):
        self.raquette.direction = 1

    def stop(self, event = None):
        self.raquette.direction = 0
    
    def limites_raquette(self):

        position = self.affichage.canva.coords(self.affichage.raquette)

        if position[0] + self.raquette.direction < 0 or position[2] + self.raquette.direction > self.affichage.canva['width']:
            self.raquette.direction = 0
        self.affichage.canva.move(self.affichage.raquette, self.raquette.vx, 0)
        self.affichage.canva.after(20, self.limites_raquette)
    
    def mouv_balle(self):
        self.affichage.canva.move(self.affichage.balle, self.balle.vx, self.balle.vy)
        self.affichage.canva.after(20, self.mouv_balle)
    
    def verif_collisions(self):
        
        if self.raquette.y <= self.balle.y + self.balle.radius and self.raquette.x <= self.balle.x <= self.raquette.y + self.raquette.width:
            self.balle.vy = -self.balle.vy

        for brique in self.brique:
            if brique.detruite == False:
                if brique.x <= self.balle.x <= brique.x + self.affichage.largeur//10 and brique.y <= self.balle.y <= brique.y + brique.hauteur:
                    brique.detruite = True
                    self.balle.vy = -self.balle.vy
                    break
        
        self.affichage.canva.after(20, self.verif_collisions)
    





