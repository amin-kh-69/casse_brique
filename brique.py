"""
Casse-Brique - TP4 Souleymane ghamhi , Amin kouhouch CPE - 3ETI 2025-2026

Version finale de cettte partie du code 

Ajout de la classes Brique
Jeu orientée objet
Jeu avec tkinter 

il reste a tester le programmme pour voir les problemmes et tester ainsi le jeu au complet 

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
        self.id = self.canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill = couleur, outline = 'white')

    def detruire(self) :
        self.canvas.delete(self.id)
