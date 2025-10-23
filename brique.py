"""
Casse-Brique - TP4 Souleymane ghamhi , Amin kouhouch CPE - 3ETI 2025-2026

Version finale de cettte partie du code 

Ajout de la classes Brique
Jeu orientée objet
Jeu avec tkinter 

il reste a tester le programmme pour voir les problemmes et tester ainsi le jeu au complet 

"""

import tkinter as tk

# Classe Brique

class Brique:
    def __init__(self, x, y, largeur, hauteur, couleur = 'orange') :
        self.x = x
        self.y = y
        self.width = largeur
        self.height = hauteur
        self.color = couleur
        self.destroyed = False
