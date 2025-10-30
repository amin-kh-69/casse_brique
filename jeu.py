""" Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier Python contient le code principal du jeu du **Casse-Brique**.  
Il regroupe les éléments essentiels du jeu :
- la raquette contrôlée par le joueur,
- la balle en mouvement,
- les briques à détruire.
Il permet de :
- Gestion du score et des vies.
- Déplacement fluide de la raquette via les flèches gauche/droite.
- Détection des collisions entre la balle, la raquette et les briques.
- Fin de partie affichant "Perdu !" ou "Victoire !" selon le résultat.
Il reste à :
- Tester le programme pour identifier d’éventuels problèmes de collisions ou de synchronisation.
"""

import tkinter as tk
import random
from raquette import Raquette
from balle import Balle
from brique import Brique
from collections import deque
from bonus import Bonus

class CasseBrique:
    def __init__(self): # Création de la fenêtre principale
        self.root = tk.Tk()
        self.root.title('Casse-Brique - CPE 3ETI')
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()

        self.briques = [] # Liste des briques à casser
        self._creer_briques()
        self.raquette = Raquette(self.canvas)
        self.balle = Balle(self.canvas, self.raquette, self.briques)

        self.score = 0      # Initialisation du score et des vies
        self.vies = 3
        self.label = tk.Label(self.root, text=f'Score: {self.score}   Vies: {self.vies}', font=('Arial', 12))
        self.label.pack()

        self.bonus = Bonus()

        self.root.bind('<Left>', lambda e: self.raquette.set_direction(-1))     # Gestion des entrées clavier pour contrôler la raquette
        self.root.bind('<Right>', lambda e: self.raquette.set_direction(1))
        self.root.bind('<KeyRelease>', self.raquette.stop)
        self.root.bind('<A>', self.activer_bonus())

        self._loop()   # Démarrage de la boucle principale du jeu
        self.root.mainloop()
        
    def _creer_briques(self):
        couleurs = ['#FF6666', '#FFB266', '#FFFF66', '#66FF66', '#66FFFF']
        for i in range(5): # 5 lignes de briques
            for j in range(10): # 10 briques par ligne
                x = 60 + j * 70
                y = 50 + i * 25
                b = Brique(self.canvas, x, y, 60, 20, couleur=couleurs[i % len(couleurs)])
                self.briques.append(b)
    
    def activer_bonus(self):
        bonus = self.balle.stock_bonus.pop()
        if bonus == 'agrandir_raquette':
            self.bonus.agrandir()
        elif bonus == 'ralentir_balle':
            self.bonus.ralentir()

    def _loop(self):    # Vérifie si la balle est perdue
        self.raquette.deplacer() 
        self.balle.move()

        if self.balle.lost:
            self.vies -= 1
            if self.vies == 0:
                self._fin_jeu('Perdu !')
                return
            else:  # Réinitialise la balle pour continuer la partie
                self.canvas.delete(self.balle.id)
                self.balle = Balle(self.canvas, self.raquette, self.briques)

        if len(self.briques) == 0:
            self._fin_jeu('Victoire !')
            return

        self.label.config(text=f'Score: {self.score + (50 * (50 - len(self.briques)))}   Vies: {self.vies}')    # Mise à jour du score (chaque brique détruite vaut 50 points)
        self.root.after(15, self._loop)        # Relance la boucle toutes les 15 ms

    def _fin_jeu(self, msg):
        self.canvas.create_text(400, 300, text=msg, fill='white', font=('Helvetica', 36))


if __name__ == '__main__': # Lancement du jeu uniquement si le fichier est exécuté directement
    CasseBrique()
