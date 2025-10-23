"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier python contient la classe de la raquette
on definit la largeur la hauteur et la couleur de la raquette 
Il ne reste normalement rien à faire
"""

class Raquette:
    def __init__(self, x, y, vx, hauteur, largeur, couleur):
        self.x = x
        self.y = y
        self.vx = vx
        self.height = hauteur
        self.width = largeur
        self.color = couleur
        self.direction = 0

    def mouvement(self, largeur_c):

        self.x += self.x * self.direction
        if self.x < 0 or self.x > largeur_c:
            self.direction = 0
