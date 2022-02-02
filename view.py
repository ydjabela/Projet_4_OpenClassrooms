
# ---------------------------------------------------------------------------------------------------------------------#


class Choice:

    def main_choice(self):
        print()
        print("Bienvenue sur le gestionnaire de jeu d'échec.\n")
        print("Selectionnez le menu souhaité.\n")
        print(" 1 : ajouter les joueurs.")
        print(" 2 : création d'un tournoi.")
        print(" 3 : Affichage des joueurs.")
        print(" 4 : Afficher  le tournois.")
        print(" 5 : sortir du logiciel.")

        print("\nQuelle est votre choix : ")
        resultat = input()
        print('-------------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number

        print("\n ERREUR : vous devez entrer un chiffre correspondant à votre choix .")

    # ---------------------------------------------------------------------------------------------------------------------#
