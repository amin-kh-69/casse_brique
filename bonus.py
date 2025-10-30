""" 
Amin Kouhouch, Souleymane Ghamhi, 3ETI, Jeudi 30 octobre 2025

Cette partie définit la classe Bonus. Elle définit les différents bonus
potentiels du joueur, ainsi que le temps actif de ces derniers.

Fonctions principales : 
    - définit les bonus et leurs effets
    - définit le temps actif des bonus

Possibles améliorations :
    - Ajout de bonus/malus
    -possibilité de gérer le temps actif des effets en fonction de l'avancement dans la partie
"""
import time

class Bonus:
    def __init__(self):
        # Chaînes représentant les types de bonus
        self.agrandir_raquette = "agrandir_raquette"  # Bonus qui agrandit temporairement la raquette
        self.ralentir_balle = "ralentir_balle"        # Bonus qui ralentit temporairement la balle

    def ralentir(self, balle):
        # Applique un ralentissement temporaire à la balle
        self.ralentissement = 0.7
        balle.vx *= self.ralentissement
        balle.vy *= self.ralentissement
        # Après 7 secondes, restaure la vitesse initiale
        if hasattr(balle.canvas, 'after'):
            balle.canvas.after(7000, lambda: self._retablir_vitesse(balle))

    def _retablir_vitesse(self, balle):
        # Restaure la vitesse de la balle après le ralentissement
        balle.vx /= self.ralentissement
        balle.vy /= self.ralentissement

    def agrandir(self, raquette):
        # Agrandit temporairement la raquette
        raquette.largeur_base = raquette.largeur
        raquette.largeur *= 1.4
        # Redessine la raquette avec la nouvelle largeur
        coords = raquette.canvas.coords(raquette.id)
        raquette.canvas.coords(raquette.id, coords[0], coords[1], coords[0] + raquette.largeur, coords[3])
        # Après 7 secondes, restaure la taille initiale
        if hasattr(raquette.canvas, 'after'):
            raquette.canvas.after(7000, lambda: self._retablir_taille(raquette))

    def _retablir_taille(self, raquette):
        # Restaure la taille de la raquette après l'effet temporaire
        raquette.largeur = raquette.largeur_base
        coords = raquette.canvas.coords(raquette.id)
        raquette.canvas.coords(raquette.id, coords[0], coords[1], coords[0] + raquette.largeur, coords[3])
        