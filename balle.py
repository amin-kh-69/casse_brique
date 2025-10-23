"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier contient la classe de la balle du jeu de casse briques
on definit la position la vitesse la couleur et le rayon de la balle 

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
    
    def mouvement(self, largeur_c, hauteur_c):

        self.x += self.vx
        self.y += self.vy
         
        if self.x - self.radius <= 0 or self.x + self.radius >= largeur_c:
            self.vx = -self.vx
        if self.y - self.radius <= 0:
            self.vy = -self.vy

        if self.y + self.radius >= hauteur_c:
            self.lost = True

    def collision_raquette(self, raquette):
        
        if (self.y + self.radius >= raquette.y and
            raquette.x <= self.x <= raquette.x + raquette.width):
            self.vy = -abs(self.vy) 
            






