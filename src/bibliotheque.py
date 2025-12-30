# src/bibliotheque.py

from livre import Livre
from utilisateur import Utilisateur
from emprunt import Emprunt

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []
        self.emprunts_actifs = []

    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

    def supprimer_livre(self, livre: Livre):
        self.livres.remove(livre)

    def inscrire_utilisateur(self, utilisateur: Utilisateur):
        self.utilisateurs.append(utilisateur)

    def emprunter_livre(self, utilisateur: Utilisateur, livre: Livre):
        if utilisateur.emprunter_livre(livre):
            emprunt = Emprunt(utilisateur, livre)
            self.emprunts_actifs.append(emprunt)
            return emprunt
        return None

    def retourner_livre(self, emprunt: Emprunt):
        if emprunt in self.emprunts_actifs:
            emprunt.clore_emprunt()
            self.emprunts_actifs.remove(emprunt)

    def afficher_etat(self):
        print("Livres dans la Bibliothèque:")
        for livre in self.livres:
            print(livre)
        print("\nEmprunts actifs:")
        for emprunt in self.emprunts_actifs:
            print(f"{emprunt.livre.titre} emprunté par {emprunt.utilisateur.nom}")
