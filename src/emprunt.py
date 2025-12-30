# src/emprunt.py

from datetime import datetime

class Emprunt:
    def __init__(self, utilisateur, livre):
        self.utilisateur = utilisateur
        self.livre = livre
        self.date_emprunt = datetime.now()
        self.actif = True

    def clore_emprunt(self):
        self.actif = False
        self.livre.retourner()
