"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier contient la classe de la balle du jeu de casse briques


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
        self.vy = -3
        self.lost = False

    def move(self):
        self.canvas.move(self.id, self.vx, self.vy)
        pos = self.canvas.coords(self.id)

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
                self.briques.remove(brique)

    def _collision(self, obj_id):
        pos_balle = self.canvas.coords(self.id)
        pos_obj = self.canvas.coords(obj_id)
        return not (pos_balle[2] < pos_obj[0] or pos_balle[0] > pos_obj[2] or pos_balle[3] < pos_obj[1] or pos_balle[1] > pos_obj[3])







