# src/emprunt.py

from datetime import datetime

class Emprunt:
    def __init__(self, utilisateur, livre):
        self._utilisateur = utilisateur
        self._livre = livre
        self._date = datetime.now()
        self._actif = True

    @property
    def utilisateur(self):
        return self._utilisateur

    @property
    def livre(self):
        return self._livre

    @property
    def date(self):
        return self._date

    @property
    def actif(self):
        return self._actif

    def cloturer(self):
        if self._actif:
            self._livre.retourner()
            self._actif = False
