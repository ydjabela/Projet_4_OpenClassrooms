
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
            color_joueur_1,
            color_joueur_2,
            score_joueur_1=None,
            score_joueur_2=None
    ):
        if color_joueur_1 == 'Blanche':
            bullet_joueur_1 = u"\u2765"
            bullet_joueur_2 = '\033[90m' + u"\u2765" + "\x1b[0m"
        else:
            bullet_joueur_1 = '\033[90m' + u"\u2765" + "\x1b[0m"
            bullet_joueur_2 = u"\u2765"
        print(
            'Match N°{}:'.format(match_number),
            '\033[92m' +
            " joueur N°{}".format(joueur_1) +
            "\x1b[0m" +
            " {} ".format(bullet_joueur_1) +
            "VS " +
            "{} ".format(bullet_joueur_2) +
            '\033[92m' +
            "joueur N°{} ".format(joueur_2)+"\x1b[0m" + "| Score : ({}-{})".format(score_joueur_1, score_joueur_2)
        )

    # ---------------------------------------------------------------------------------------------------------------------#

    def round_view(self, Round):
        print('\033[92m' + '\n{}:'.format(Round) + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number

        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à votre choix ." + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#
