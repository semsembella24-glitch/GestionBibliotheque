# src/utilisateur.py
class Utilisateur:
    def __init__(self, nom):
        self._nom = nom
        self._livres_empruntes = []

    @property
    def nom(self):
        return self._nom

    @property
    def livres_empruntes(self):
        return self._livres_empruntes.copy()

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self._livres_empruntes.append(livre)
            return True
        return False

    def retourner_livre(self, livre):
        if livre in self._livres_empruntes:
            livre.retourner()
            self._livres_empruntes.remove(livre)
            return True
        return False