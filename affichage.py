"""Amin Kouhouch, 3ETI Jeudi 16 Octobre
Ce fichier contient la classe d'affichage du jeu du casse_brique

Il reste à dessiner les briques la raquette et la balle
"""
import tkinter as tk


class Affichage:
    def __init__(self, largeur, hauteur):
        self.root = tk.Tk()
        self.canva = tk.Canvas(self.root, width = largeur, height = hauteur, bg = 'white')
        self.canvas.pack()
