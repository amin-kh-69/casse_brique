"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier python contient la classe de la raquette
on definit la raquette et on definit son déplacement

"""

class Raquette :
    def __init__(self, canvas, largeur = 100, hauteur = 15, couleur = 'blue') :
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.x = (int(canvas['width']) - largeur)//2
        self.y = int(canvas['height']) - 40
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + largeur, self.y + hauteur, fill = couleur)
        self.vitesse = 20
        self.direction = 0

    def deplacer(self):
        self.canvas.move(self.id, self.direction*self.vitesse, 0)
        coords = self.canvas.coords(self.id)
        if coords[0] < 0:
            self.canvas.move(self.id, -coords[0], 0)
        elif coords[2] > int(self.canvas['width']):
            self.canvas.move(self.id, int(self.canvas['width']) - coords[2], 0)

    def set_direction(self, dir):
        self.direction = dir

    def stop(self, event=None):
        self.direction = 0
