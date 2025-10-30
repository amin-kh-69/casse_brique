""" 
Amin Kouhouch, Souleymane Ghamhi, 3ETI, Jeudi 30 octobre 2025

"""
from balle import Balle
from raquette import Raquette
import time

class Bonus:
    def __init__(self):
        self.agrandir_raquette = "agrandir_raquette"
        self.ralentir_balle = "ralentir_balle"

    def ralentir(self, balle):
        self.balle = balle
        self.balle.vx_base, self.balle.vy_base = self.balle.vx, self.balle.vy
        self.balle.vx, self.balle.vy = self.balle.vx * 0.7, self.balle.vy * 0.7


        time.sleep(7)
        self.balle.vx, self.balle.vy = self.balle.vx_base, self.balle.vy_base


    def agrandir(self, raquette):
        self.raquette = raquette 
        self.raquette.largeur_base = self.raquette.largeur
        self.raquette.largeur *= 1.4


        time.sleep(7)
        self.raquette.largeur = self.raquette.largeur_base
        