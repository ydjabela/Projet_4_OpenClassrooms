from player import Player
from tournament import Tournament

class choice:

    def main_choice():
        print()
        print("Bienvenue sur le gestionnaire de jeu d'échec.\n")
        print("Selectionnez le menu souhaité.\n")
        print(" 1 : ajouter un joueur.")
        print(" 2 : création d'un tournoi.")
        print(" 3 : sortir du logiciel.")
        print("\nQuelle est votre choix : ")
        resultat = input()
        return resultat


resultat = int(choice.main_choice())
if resultat == 1:
    Player().add_players()
elif resultat == 2:
    Tournament().add_tournament()
elif resultat == 3:
    exit()
else:
    resultat = choice.main_choice()