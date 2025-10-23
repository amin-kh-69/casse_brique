"""Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier contient la classe d'affichage du jeu du casse_brique

Il reste à tester le programme pour voir les potentiels problèmes
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
        self.bouton_jouer = tk.Button(self.root, text="Jouer", font=("Helvetica", 24), width=10, command=self.lancer_jeu)
        self.bouton_quitter = tk.Button(self.root, text="Quitter", font=("Helvetica", 24), width=10, command=self.root.destroy)

        # Position boutons sur le canvas
        self.canvas.create_window(400, 300, window=self.bouton_jouer)
        self.canvas.create_window(400, 400, window=self.bouton_quitter)

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


if __name__ == "__main__":
    AffichageMenuAnimé()