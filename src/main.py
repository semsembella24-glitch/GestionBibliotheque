# src/main.py

from livre import Livre
from utilisateur import Utilisateur
from bibliotheque import Bibliotheque

if __name__ == "__main__":
    bibliotheque = Bibliotheque()

    # Création des livres
    livre1 = Livre("Une brève histoire de presque tout", "Bill Bryson")
    livre2 = Livre("Le Gène égoïste", "Richard Dawkins")
    livre3 = Livre("Cosmos", "Carl Sagan")
    livre4 = Livre("La Cuillère disparue", "Sam Kean")

    for livre in [livre1, livre2, livre3, livre4]:
        bibliotheque.ajouter_livre(livre)

    # Création des utilisateurs
    mouna = Utilisateur("mouna")
    wissam = Utilisateur("wissam")
    bibliotheque.inscrire_utilisateur(mouna)
    bibliotheque.inscrire_utilisateur(wissam)

    # Emprunts
    emprunt1 = bibliotheque.emprunter_livre(wissam, livre1)
    emprunt2 = bibliotheque.emprunter_livre(mouna, livre3)

    # Affichage initial
    bibliotheque.afficher_etat()

    # Retour d'un livre
    bibliotheque.retourner_livre(emprunt1)
    print("\nAprès retour d'un livre :")
    bibliotheque.afficher_etat()
