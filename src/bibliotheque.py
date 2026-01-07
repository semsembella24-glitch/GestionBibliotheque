# src/bibliotheque.py
from livre import Livre
from utilisateur import Utilisateur
from emprunt import Emprunt

class Bibliotheque:
    def __init__(self):
        self._livres = []
        self._utilisateurs = []
        self._emprunts_actifs = []

    @property
    def livres(self):
        return self._livres.copy()

    @property
    def utilisateurs(self):
        return self._utilisateurs.copy()

    @property
    def emprunts_actifs(self):
        return self._emprunts_actifs.copy()

    def ajouter_livre(self, livre):
        self._livres.append(livre)

    def inscrire_utilisateur(self, utilisateur):
        self._utilisateurs.append(utilisateur)

    def emprunter_livre(self, utilisateur, livre):
        if utilisateur.emprunter_livre(livre):
            emprunt = Emprunt(utilisateur, livre)
            self._emprunts_actifs.append(emprunt)
            return emprunt
        return None

    def retourner_livre(self, emprunt):
        if emprunt in self._emprunts_actifs:
            emprunt.cloturer()
            self._emprunts_actifs.remove(emprunt)

    def afficher_etat(self):
        print("📚 Livres :")
        for livre in self._livres:
            print(livre)
        print("\n📄 Emprunts actifs :")
        for emprunt in self._emprunts_actifs:
            print(f"{emprunt.livre.titre} emprunté par {emprunt.utilisateur.nom}")
