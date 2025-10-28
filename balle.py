"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Cette partie définit la classe Balle qui représente la balle du jeu de Casse-Brique.
Elle gère les déplacements les rebonds sur les murs et la raquette ainsi que les
collisions avec les briques à l’aide du canvas Tkinter.

Fonctionnalités principales :
- Mouvement automatique de la balle avec gestion des rebonds.
- Détection des collisions avec les murs, la raquette et les briques.
- Gestion de la perte de balle (sortie par le bas de l’écran).

Il reste à :
- Tester la précision des collisions avec la raquette notament les coter verticale de la raquette et les briques.
- Donc ajuster la vitesse et les angles de rebond 
"""
import random
import tkinter as tk

class Balle:
    def __init__(self, canvas, raquette, briques, couleur='red'):
        self.canvas = canvas
        self.raquette = raquette
        self.briques = briques
        self.couleur = couleur
        self.id = self.canvas.create_oval(390, 350, 410, 370, fill=couleur)
        self.vx = random.choice([-3, 3])
        self.vy = -3  # la balle part vers le haut
        self.lost = False    # Indique si la balle est perdue (tombée en bas)

    def move(self):
        self.canvas.move(self.id, self.vx, self.vy)
        pos = self.canvas.coords(self.id) # coordonnées actuelles de la balle

        # rebond sur murs
        if pos[0] <= 0 or pos[2] >= int(self.canvas['width']):
            self.vx = -self.vx
        if pos[1] <= 0:
            self.vy = -self.vy

        # touche le bas
        if pos[3] >= int(self.canvas['height']):
            self.lost = True

        # collision avec raquette
        if self._collision(self.raquette.id):
            self.vy = -abs(self.vy)

        # collision avec briques
        for brique in list(self.briques):
            if self._collision(brique.id):
                self.vy = -self.vy
                brique.detruire()
                self.briques.remove(brique) # retire la brique de la liste

    def _collision(self, obj_id):
        pos_balle = self.canvas.coords(self.id)
        pos_obj = self.canvas.coords(obj_id)    # Test de non-superposition des rectangles
        return not (pos_balle[2] < pos_obj[0] or pos_balle[0] > pos_obj[2] or pos_balle[3] < pos_obj[1] or pos_balle[1] > pos_obj[3])  # balle à gauche a  droite en haut ou en bas de l'objet







