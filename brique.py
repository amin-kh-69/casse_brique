"""
Casse-Brique - TP4 Souleymane ghamhi , Amin kouhouch CPE - 3ETI 2025-2026
Version finale de cette partie du code.

Cette partie définit la classe Brique utilisée dans le jeu de Casse-Brique.
Chaque brique est un objet graphique créé sur le canvas Tkinter, avec une position,
une taille et une couleur spécifiques.

Le jeu suit une approche orientée objet : chaque élément (balle, raquette, brique, etc.)
est représenté par une classe dédiée.

Il reste à :
- Tester le programme complet pour vérifier le bon fonctionnement de la classe `Brique`.
- Confirmer la bonne détection et destruction des briques lors des collisions.

"""

# Classe Brique

class Brique:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur = 'orange') :
        self.canvas = canvas
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.id = self.canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill = couleur, outline = 'white') # Création graphique de la brique sur le canvas

    def detruire(self) :
        self.canvas.delete(self.id) #Supprime la brique du canvas lorsqu'elle est touchée par la balle
