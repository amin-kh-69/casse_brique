"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier Python contient la classe Raquette utilisée dans le jeu de Casse-Brique
Elle définit l’apparence et le comportement de la raquette contrôlée par le joueur.

La raquette peut se déplacer horizontalement à l’intérieur des limites du canvas.
Le joueur contrôle sa direction à l’aide des touches du clavier (gauche / droite).
La classe gère aussi les collisions avec les bords pour empêcher la raquette
de sortir de la zone de jeu.

Il reste à :
- Tester la réactivité et la fluidité du déplacement
- Ajuster la vitesse pour un contrôle optimal du jeu.
"""

class Raquette :
    def __init__(self, canvas, largeur = 100, hauteur = 15, couleur = 'blue') :
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.x = (int(canvas['width']) - largeur)//2  # Position initiale centrée horizontalement, proche du bas du canvas
        self.y = int(canvas['height']) - 40
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + largeur, self.y + hauteur, fill = couleur) # Création graphique de la raquette
        self.vitesse = 20
        self.direction = 0   # Vitesse de déplacement et direction (0 = immobile)

    def deplacer(self):
        self.canvas.move(self.id, self.direction*self.vitesse, 0)    # Déplacement horizontal
        coords = self.canvas.coords(self.id)  # Récupération des coordonnées après mouvement
        if coords[0] < 0:     # Empêche de dépasser le bord gauche
            self.canvas.move(self.id, -coords[0], 0)
        elif coords[2] > int(self.canvas['width']):        # Empêche de dépasser le bord droit
            self.canvas.move(self.id, int(self.canvas['width']) - coords[2], 0)

    def set_direction(self, dir): #Définit la direction du mouvement.
        self.direction = dir 

    def stop(self, event=None): #Arrête le déplacement (utilisé lors du relâchement d’une touche).
        self.direction = 0
