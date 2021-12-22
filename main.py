from player import Player
from tournament import Tournament


class choice:

    def main_choice():
        print()
        print("Bienvenue sur le gestionnaire de jeu d'échec.\n")
        print("Selectionnez le menu souhaité.\n")
        print(" 1 : ajouter les joueurs.")
        print(" 2 : création d'un tournoi.")
        print(" 3 : Voir les joueurs.")
        print(" 10 : sortir du logiciel.")
        print("\nQuelle est votre choix : ")
        resultat = input()
        return resultat


while True:
    try:
        resultat = choice.main_choice()
        if int(resultat) == 1:
            Player().add_players()
        elif int(resultat) == 2:
            Tournament().add_tournament()
        elif int(resultat) == 3:
            Player().search_player()
        elif int(resultat) == 10:
            break
        else:
            print("===>choix nest pas valable, veuillez saisir un chifres 1 et 4")
    except Exception as e:
        print("1===>choix nest pas valable, veuillez saisir un chifres 1 et 4", e)

print('herr')
