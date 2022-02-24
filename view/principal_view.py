
# ---------------------------------------------------------------------------------------------------------------------#


class Choice:

    def main_choice(self):
        print()
        print('\033[92m' + " * * * Bienvenue sur le gestionnaire de jeu d'échec. * * * \n" + "\x1b[0m")
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Gestion des joueurs." + "\x1b[0m")
        print('\033[93m'+" 2 : Gestion des tournois." + "\x1b[0m")
        print('\033[93m'+" 3 : Demmarer un tournoi." + "\x1b[0m")
        print('\033[93m'+" 5 : sortir du logiciel." + "\x1b[0m")

        print('\033[91m'+"\nQuelle est votre choix : " + "\x1b[0m")
        resultat = input()
        print('-------------------------------------------------------------------------------------------------------')
        return resultat

    def message_visit(self):
        print('Merci pour  votre visite')

    # ---------------------------------------------------------------------------------------------------------------------#

    def match_view(
            self,
            joueur_1,
            joueur_2,
            match_number,
            score_joueur_1=None,
            score_joueur_2=None
    ):
        print(
            'Match N°{}:'.format(match_number),
            ',\033[92m' +
            " joueur N°{}  VS joueur N°{} | Score : ({}-{})".format(joueur_1, joueur_2, score_joueur_1, score_joueur_2) +
            "\x1b[0m"
        )

    # ---------------------------------------------------------------------------------------------------------------------#

    def round_view(self, Round):
        print('\033[92m' + '\n{}:'.format(Round) + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number

        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à votre choix ." + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#
