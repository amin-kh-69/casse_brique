"""
Casse-Brique - TP4 Souleymane ghamhi , Amin kouhouch CPE - 3ETI 2025-2026

Version améliorée :

Ajout de 3 classes : Balle, Raquette, Brique
Jeu orientée objet
Jeu complet fonctionnel sous Tkinter interface grapique vu en cours 

"""

import tkinter as tk
import random
import math

# Classe Brique

class Brique:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur = 'orange') :
        self.canvas = canvas
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + self.largeur, self.y + self.hauteur, fill=self.couleur)
        self.active = True