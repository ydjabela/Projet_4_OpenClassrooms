
# ---------------------------------------------------------------------------------------------------------------------#


class Sub_Choice:

    def sub_main_choice(self):
        print()
        print(" * * * Gestionnaire des joueurs. * * *\n")
        print(" /// Selectionnez le menu souhaité. /// \n")
        print(" 1 : Ajouter un joueur.")
        print(" 2 : modifier un joueur.")
        print(" 3 : Supprimmer un joueur.")
        print(" 4 : Affichage des joueurs.")
        print(" 5 : Supprimmer tous les joueurs.")
        print(" 6 : Retour au menu principal.")
        print(" 7 : sortir du logiciel.")

        print("\nQuelle est votre choix : ")
        resultat = input()
        print('-------------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number

        print("\n ERREUR : vous devez entrer un chiffre correspondant à votre choix .")

    # ---------------------------------------------------------------------------------------------------------------------#


class Error_enter:

    def print_error_enter_int_age(self):
        # indicates to the user that he must enter a number

        print("\n ERREUR : vous devez entrer un chiffre correspondant à votre choix .")
