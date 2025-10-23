""" Amin Kouhouch, Souleymane Ghamhi, 3ETI Jeudi 16 Octobre
Ce fichier python contient le code du jeu du cassse briques

Il reste à tester le programme pour voir les potentiels problèmes
"""

import tkinter as tk
import random
from affichage import Affichage
from raquette import Raquette
from balle import Balle
from brique import Brique

class CasseBrique:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Casse-Brique - CPE 3ETI')
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()

        self.briques = []
        self._creer_briques()
        self.raquette = Raquette(self.canvas)
        self.balle = Balle(self.canvas, self.raquette, self.briques)

        self.score = 0
        self.vies = 3
        self.label = tk.Label(self.root, text=f'Score: {self.score}   Vies: {self.vies}', font=('Arial', 12))
        self.label.pack()

        self.root.bind('<Left>', lambda e: self.raquette.set_direction(-1))
        self.root.bind('<Right>', lambda e: self.raquette.set_direction(1))
        self.root.bind('<KeyRelease>', self.raquette.stop)

        self._loop()
        self.root.mainloop()

    def _creer_briques(self):
        couleurs = ['#FF6666', '#FFB266', '#FFFF66', '#66FF66', '#66FFFF']
        for i in range(5):
            for j in range(10):
                x = 60 + j * 70
                y = 50 + i * 25
                b = Brique(self.canvas, x, y, 60, 20, couleur=couleurs[i % len(couleurs)])
                self.briques.append(b)

    def _loop(self):
        self.raquette.deplacer()
        self.balle.move()

        if self.balle.lost:
            self.vies -= 1
            if self.vies == 0:
                self._fin_jeu('Perdu !')
                return
            else:
                self.canvas.delete(self.balle.id)
                self.balle = Balle(self.canvas, self.raquette, self.briques)

        if len(self.briques) == 0:
            self._fin_jeu('Victoire !')
            return

        self.label.config(text=f'Score: {self.score + (50 * (50 - len(self.briques)))}   Vies: {self.vies}')
        self.root.after(15, self._loop)

    def _fin_jeu(self, msg):
        self.canvas.create_text(400, 300, text=msg, fill='white', font=('Helvetica', 36))


if __name__ == '__main__':
    CasseBrique()