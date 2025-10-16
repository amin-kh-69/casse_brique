"""Amin Kouhouch, 3ETI Jeudi 16 Octobre
Ce fichier contient la classe de la balle du jeu de casse briques
"""

class Balle:
    def __init__(self, x, y, vx, vy, rayon, couleur):
        self.x = x
        self.y = y
        self.vx = vx 
        self.vy = vy
        self.color = couleur
        self.radius = rayon
        self.lost = False




