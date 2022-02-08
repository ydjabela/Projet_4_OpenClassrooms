
# ---------------------------------------------------------------------------------------------------------------------#


class Choice:

    def main_choice(self):
        print()
        print('\033[92m' + " * * * Bienvenue sur le gestionnaire de jeu d'échec. * * * \n" + "\x1b[0m")
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Gestion des joueurs." + "\x1b[0m")
        print('\033[93m'+" 2 : Gestion des tournois." + "\x1b[0m")
        print('\033[93m'+" 5 : sortir du logiciel." + "\x1b[0m")

        print('\033[91m'+"\nQuelle est votre choix : " + "\x1b[0m")
        resultat = input()
        print('-------------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number

        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à votre choix ." + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#
