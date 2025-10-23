"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier contient la classe d'affichage du jeu du casse_brique

Il reste à tester le programme pour voir les potentiels problèmes
"""
import tkinter as tk
from balle import Balle
from brique import Brique
from raquette import Raquette


class Affichage:

    def __init__(self, largeur, hauteur):

        self.root = tk.Tk()
        self.canva = tk.Canvas(self.root, width = largeur, height = hauteur, bg = 'white')
        self.canva.pack()
        self.width = largeur
        self.height = hauteur

    def balle_affichage(self, balle):

        self.balle = self.canva.create_oval(
            balle.x - balle.radius, balle.y - balle.radius,
            balle.x + balle.radius, balle.y + balle.radius,
            fill = balle.color
            )
        
    def raquette_affichage(self, raquette):

        self.raquette = self.canva.create_rectangle(
            raquette.x, raquette.y,
            raquette.x + raquette.width, raquette.y + raquette.height,
            fill = raquette.color
        )
    
    def brique_affichage(self, brique):

        self.brique = self.canva.create_rectangle(
            brique.x, brique.y,
            brique.x + brique.width, brique.y + brique.height,
            fill = brique.color
        )

