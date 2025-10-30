"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Cette partie contient la classe AffichageMenuAnimé responsable de la création et de l’animation
du menu principal du jeu Casse-Brique. Il gère l’affichage du titre les boutons d’interaction
(Jouer, Crédits, Quitter) ainsi qu’une animation des briques au fond
L’objectif est d’offrir une interface d’accueil dynamique avant le lancement du jeu principal
 

Il reste à :
- Tester le bon fonctionnement de l’interface graphique (affichage, boutons, animations).
- Vérifier la transition entre le menu et le lancement du jeu (fonction `lancer_jeu`).
- Il reste à tester le programme pour voir les potentiels problèmes
"""
from jeu import CasseBrique
import tkinter as tk
import random
import math


class AffichageMenuAnimé:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Casse-Brique")
        self.root.geometry("800x600")
        self.root.configure(bg='black')

        # Canvas pour l'animation
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Titre du jeu
        self.titre = self.canvas.create_text(400, 100, text="CASSE-BRIQUE", font=("Helvetica", 48, "bold"), fill="white")

        # Boutons Jouer et Quitter
        self.bouton_credits = tk.Button(self.root, text="Crédits", font=("Helvetica", 24), width=10, command=self.afficher_credits)
        self.bouton_jouer = tk.Button(self.root, text="Jouer", font=("Helvetica", 24), width=10, command=self.lancer_jeu)
        self.bouton_quitter = tk.Button(self.root, text="Quitter", font=("Helvetica", 24), width=10, command=self.root.destroy)
        self.bouton_commandes = tk.Button(self.root, text="Commandes", font=("Helvetica", 24), width=10, command=self.afficher_commandes)


        # Position boutons sur le canvas
        self.canvas.create_window(400, 300, window=self.bouton_jouer)
        self.canvas.create_window(400, 350, window=self.bouton_credits)
        self.canvas.create_window(400, 400, window=self.bouton_quitter)
        self.canvas.create_window(400, 450, window=self.bouton_commandes)

        # Création des briques animées
        self.briques = []
        couleurs = ['#FF6666', '#FFB266', '#FFFF66', '#66FF66', '#66FFFF']
        for _ in range(20):
            x = random.randint(50, 750)
            y = random.randint(150, 550)
            largeur = random.randint(40, 60)
            hauteur = 20
            couleur = random.choice(couleurs)
            dx = random.choice([-2, -1, 1, 2])
            dy = random.choice([-1, 1])
            rect = self.canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill=couleur, outline="white")
            self.briques.append({"id": rect, "dx": dx, "dy": dy})

        self.animer_briques()
        self.root.mainloop()

    def animer_briques(self):
        for b in self.briques:
            self.canvas.move(b["id"], b["dx"], b["dy"])
            coords = self.canvas.coords(b["id"])
            # Rebond sur les murs
            if coords[0] <= 0 or coords[2] >= 800:
                b["dx"] = -b["dx"]
            if coords[1] <= 120 or coords[3] >= 580:
                b["dy"] = -b["dy"]
        self.root.after(50, self.animer_briques)

    def lancer_jeu(self):
        self.root.destroy()
        CasseBrique()

    def afficher_credits(self):
        self.canvas.delete("credits")  
        self.canvas.create_text(400, 550, text="AMIN KOUHOUCH / SOULEYMANE GHAMHI", font=("Helvetica", 24, "bold"), fill="white", tags="credits")
        self.root.after(3000, lambda: self.canvas.delete("credits"))
    
    def afficher_commandes(self):
        # Affiche un label d'aide bien visible dans la fenêtre
        label = tk.Label(self.root, text = "Pour déplacer la raquette ce sont les flèches\nPour utiliser vos bonus, c'est 'a'", font = ("Helvetica", 14), fg = 'black', bg = "light grey")
        label_id = self.canvas.create_window(400, 500, window = label)  # 550 est visible dans le canvas 800x600
        self.root.after(5000, lambda: self.canvas.delete(label_id))



if __name__ == "__main__":
    AffichageMenuAnimé()
