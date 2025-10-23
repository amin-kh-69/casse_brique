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

class Jeu:
    def __init__(self):
        # --- Initialisation des objets principaux ---
        self.affichage = Affichage(500, 700)
        self.raquette = Raquette(300, 500, 20, 15, 100, 'blue')
        self.balle = Balle(400, 300, 3, 3, 5, 'red')

        # Création des briques
        self.brique = [
            Brique(x * (self.affichage.width // 10) + 30, y * 30 + 50,
                   self.affichage.width // 10 - 10, 20)
            for x in range(10)
            for y in range(5)
        ]

        # --- Gestion des touches ---
        self.affichage.root.bind("<Left>", self.gauche)
        self.affichage.root.bind("<Right>", self.droite)
        self.affichage.root.bind("<KeyRelease>", self.stop)

    # --- Déplacements raquette ---
    def gauche(self, event=None):
        self.raquette.direction = -1
   
    def droite(self, event=None):
        self.raquette.direction = 1

    def stop(self, event=None):
        self.raquette.direction = 0

    def limites_raquette(self):
        position = self.affichage.canva.coords(self.affichage.raquette)

        # Limites gauche/droite
        if (position[0] + self.raquette.direction * self.raquette.vx < 0 or
            position[2] + self.raquette.direction * self.raquette.vx > int(self.affichage.canva['width'])):
            self.raquette.direction = 0

        # Déplacement de la raquette
        self.affichage.canva.move(
            self.affichage.raquette,
            self.raquette.vx * self.raquette.direction, 0
        )

        self.affichage.canva.after(20, self.limites_raquette)

    # --- Déplacement balle ---
    def mouv_balle(self):
        self.affichage.canva.move(self.affichage.balle, self.balle.vx, self.balle.vy)
        coords = self.affichage.canva.coords(self.affichage.balle)
        self.balle.x = (coords[0] + coords[2]) / 2
        self.balle.y = (coords[1] + coords[3]) / 2

        # Rebonds sur les murs
        if self.balle.x - self.balle.radius <= 0 or self.balle.x + self.balle.radius >= self.affichage.width:
            self.balle.vx = -self.balle.vx
        if self.balle.y - self.balle.radius <= 0:
            self.balle.vy = -self.balle.vy

        # Si la balle tombe : reset
        if self.balle.y > self.affichage.height:
            self.balle.lost = True

        self.affichage.canva.after(20, self.mouv_balle)

    # --- Gestion des collisions ---
    def verif_collisions(self):
        # Collision balle - raquette
        #if (
        #    self.balle.y + self.balle.radius >= self.raquette.y and
        #    self.raquette.x <= self.balle.x <= self.raquette.x + self.raquette.width
        #):
        #    self.balle.vy = -abs(self.balle.vy)

        # Collision balle - briques
        for brique in self.brique:
            if not brique.destroyed:
                if (brique.x <= self.balle.x <= brique.x + brique.width and
                    brique.y <= self.balle.y <= brique.y + brique.height):
                    brique.destroyed = True
                    self.affichage.canva.delete(brique.forme)
                    self.balle.vy = -self.balle.vy
                    break
       
        self.affichage.canva.after(20, self.verif_collisions)

    # --- Boucle principale du jeu ---
    def boucle_principale(self):
        while self.balle.lost == False:
            self.affichage.balle_affichage(self.balle)
            self.affichage.raquette_affichage(self.raquette)
            for brique in self.brique:
               self.affichage.brique_affichage(brique)
       
            self.limites_raquette()
            self.mouv_balle()
            self.verif_collisions()
            self.affichage.root.mainloop()
            


if __name__ == "__main__":
    jeu_instance = Jeu()
    jeu_instance.boucle_principale()





