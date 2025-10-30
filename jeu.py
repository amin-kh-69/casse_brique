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
- Faire apparaitre les icones des bonus qu'on a
"""

import tkinter as tk
from raquette import Raquette
from balle import Balle
from brique import Brique
from bonus import Bonus
from PIL import Image, ImageTk

class CasseBrique:
    def __init__(self): # Création de la fenêtre principale
        self.bonus_image_id = None  # Pour gérer l'affichage unique du bonus
        self.root = tk.Tk()
        self.root.title('Casse-Brique - CPE 3ETI')
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()
        self.h_canva = int(self.canvas['height'])
        self.l_canva = int(self.canvas['width'])
        self.root.focus_force()  # Donne le focus à la fenêtre du jeu

        self.briques = [] # Liste des briques à casser
        self._creer_briques()
        self.bonus = Bonus()
        self.raquette = Raquette(self.canvas)
        self.balle = Balle(self.bonus, self.canvas, self.raquette, self.briques)

        self.score = 0      # Initialisation du score et des vies
        self.vies = 3
        self.label = tk.Label(self.root, text=f'Score: {self.score}   Vies: {self.vies}', font=('Arial', 12))
        self.label.pack()

        # Importation de l'image du bonus ralentissement de la balle
        self.escargot = Image.open("escargot.jpg") 
        self.l_esc, self.h_esc = self.l_canva // 10, self.h_canva // 10
        self.escargot = self.escargot.resize((self.l_esc, self.h_esc), resample=Image.Resampling.LANCZOS)
        self.photo_esc = ImageTk.PhotoImage(self.escargot)

        # Importation de l'image du bonus d'augmentation de la taille de la raquette
        self.augmentation = Image.open("augmentation.png")
        self.l_aug, self.h_aug = self.l_canva // 10, self.h_canva // 10
        self.augmentation = self.augmentation.resize((self.l_aug, self.h_aug), resample=Image.Resampling.LANCZOS)
        self.photo_aug = ImageTk.PhotoImage(self.augmentation)

        self.root.bind('<Left>', lambda e: self.raquette.set_direction(-1))     # Gestion des entrées clavier pour contrôler la raquette et les bonus
        self.root.bind('<Right>', lambda e: self.raquette.set_direction(1))
        self.root.bind('<KeyRelease>', self.raquette.stop)
        self.root.bind('<a>', lambda e: self._activer_bonus())

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

    def _afficher_bonus(self):
        # Efface l'ancienne image de bonus si elle existe
        if self.bonus_image_id is not None:
            self.canvas.delete(self.bonus_image_id)
            self.bonus_image_id = None
        print("Affichage bonus :", list(self.balle.stock_bonus)) # test
        # Affiche l'image correspondant au bonus au sommet de la pile (dernier bonus ajouté)
        if self.balle.stock_bonus != [] and self.balle.stock_bonus[-1] == 'agrandir_raquette':
            self.bonus_image_id = self.canvas.create_image(10, self.h_canva - self.h_aug, image = self.photo_aug, anchor = 'sw')
        elif self.balle.stock_bonus != [] and self.balle.stock_bonus[-1] == 'ralentir_balle':
            self.bonus_image_id = self.canvas.create_image(10, self.h_canva - self.h_esc, image = self.photo_esc, anchor = 'sw')
        self.root.after(15, self._afficher_bonus)

    def _activer_bonus(self):
        if self.balle.stock_bonus:
            bonus = self.balle.stock_bonus.pop() # utilisation d'une pile (First In, Last Out)
            print("Activation bonus :", bonus)
            if bonus == 'agrandir_raquette':
                self.bonus.agrandir(self.raquette)
            elif bonus == 'ralentir_balle':
                self.bonus.ralentir(self.balle)
    
    def _loop(self):    # Vérifie si la balle est perdue
        try:
            self.raquette.deplacer() 
            self.balle.move()

            if self.balle.lost:
                self.vies -= 1
                if self.vies == 0:
                    self._fin_jeu('Perdu !')
                    return
                else:  # Réinitialise la balle pour continuer la partie
                    self.canvas.delete(self.balle.id)
                    self.balle = Balle(self.bonus, self.canvas, self.raquette, self.briques)

            if len(self.briques) == 0:
                self._fin_jeu('Victoire !')
                return

            self.label.config(text=f'Score: {self.score + (50 * (50 - len(self.briques)))}   Vies: {self.vies}')    # Mise à jour du score (chaque brique détruite vaut 50 points)
        except Exception as e:
            print('Erreur dans la boucle principale :', e)
        self.root.after(15, self._loop)        # Relance la boucle toutes les 15 ms

    def _fin_jeu(self, msg):
        self.canvas.create_text(400, 300, text=msg, fill='white', font=('Helvetica', 36))


if __name__ == '__main__': # Lancement du jeu uniquement si le fichier est exécuté directement
    CasseBrique()
