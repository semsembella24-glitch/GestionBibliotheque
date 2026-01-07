# src/livre.py
class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
        self._disponible = True

    @property
    def titre(self):
        return self._titre

    @property
    def auteur(self):
        return self._auteur

    @property
    def disponible(self):
        return self._disponible

    def emprunter(self):
        if self._disponible:
            self._disponible = False
            return True
        return False

    def retourner(self):
        self._disponible = True

    def __str__(self):
        etat = "Disponible" if self._disponible else "Emprunté"
        return f"{self._titre} par {self._auteur} - {etat}