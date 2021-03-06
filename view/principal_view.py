
# ---------------------------------------------------------------------------------------------------------------------#


class Choice:

    @staticmethod
    def main_choice():
        # Menu principal
        print('\033[92m' + "\n * * * Bienvenue sur le gestionnaire de jeu d'échec. * * * \n" + "\x1b[0m")
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Gestion des joueurs." + "\x1b[0m")
        print('\033[93m'+" 2 : Gestion des tournois." + "\x1b[0m")
        print('\033[93m'+" 3 : Demmarer un tournoi." + "\x1b[0m")
        print('\033[93m'+" 5 : sortir du logiciel." + "\x1b[0m")

        print('\033[91m'+"\nQuelle est votre choix : " + "\x1b[0m")
        resultat = input()
        print('-----------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def message_visit():
        # Message de quitter le menu
        print('Merci pour  votre visite')

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def match_view(
            joueur_1,
            joueur_2,
            match_number,
            color_joueur_1,
            score_joueur_1=0,
            score_joueur_2=0,
            start_match_time=0,
            end_match_time=0
    ):
        # Init color
        if color_joueur_1 == 'Blanche':
            bullet_joueur_1 = u"\u2765"
            bullet_joueur_2 = '\033[90m' + u"\u2765" + "\x1b[0m"
        else:
            bullet_joueur_1 = '\033[90m' + u"\u2765" + "\x1b[0m"
            bullet_joueur_2 = u"\u2765"
        # Init Temps des matchs
        if start_match_time != 0:
            start_match = ' Demmarer à: {}'.format(start_match_time)
            if end_match_time != 0:
                end_match = ' Terminé à: {}'.format(end_match_time)
            else:
                end_match = " Le Match n'est pas encore Terminé"
        else:
            start_match = " le match n'est pas encore commencé"
            end_match = ''
        # Affichage du match
        print(
            'Match N°{}:'.format(match_number),
            '\033[92m' +
            " joueur N°{}".format(joueur_1) +
            "\x1b[0m" +
            " {} ".format(bullet_joueur_1) +
            "VS " +
            "{} ".format(bullet_joueur_2) +
            '\033[92m' +
            "joueur N°{} ".format(joueur_2)+"\x1b[0m" + "| Score : ({}-{})".format(score_joueur_1, score_joueur_2) +
            start_match +
            end_match
        )

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def round_view(round_x):
        # Affichage des rounds
        print('\033[92m' + '\n{}:'.format(round_x) + "\x1b[0m")

    # -----------------------------------------------------------------------------------------------------------------#

    def restart_round_choice(self):
        # Affichage de menu redemmarer un tournoi ou de quitter
        print("\n /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m' + " 1 : Redemarrer le tournoi." + "\x1b[0m")
        print('\033[93m' + " 2 : Sortir du tournoi." + "\x1b[0m")
        try:
            resultat = int(input('\033[91m' + "\nQuelle est votre choix : " + "\x1b[0m"))
            if resultat > 2 or resultat <= 0:
                self.print_error_enter_int()
                resultat = self.restart_round_choice()
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.restart_round_choice()
        print('-----------------------------------------------------------------------------------------------------')
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def match_finished():
        # match finished
        print('\033[91m'+"\n le match est deja fini." + "\x1b[0m")

    # -----------------------------------------------------------------------------------------------------------------#

    def start_end_match_view(
            self,
            m_finished_1, m_finished_2, m_finished_3, m_finished_4, m_al_sta_1, m_al_sta_2, m_al_sta_3, m_al_sta_4
    ):
        # Affichage de menu jouer les matchs et d'inséré les resultats
        print('\033[92m' + " Démarré ou mettre fin a un match \n" + "\x1b[0m")
        print(" /// Selectionnez le menu souhaité. /// \n")
        if not m_finished_1:
            if m_al_sta_1:
                print('\033[93m'+" 1 : Arreter le match 1." + "\x1b[0m")
            else:
                print('\033[93m'+" 1 : Démarrer le match 1." + "\x1b[0m")
        else:
            print('\033[93m'+" 1 : le Match 1 est terminé." + "\x1b[0m")
        if not m_finished_2:
            if m_al_sta_2:
                print('\033[93m'+" 2 : Arreter le match 2." + "\x1b[0m")
            else:
                print('\033[93m'+" 2 : Démarrer le match 2." + "\x1b[0m")
        else:
            print('\033[93m'+" 2 : le Match 2 est terminé." + "\x1b[0m")
        if not m_finished_3:
            if m_al_sta_3:
                print('\033[93m'+" 3 : Arreter le match 3." + "\x1b[0m")
            else:
                print('\033[93m'+" 3 : Démarrer le match 3." + "\x1b[0m")
        else:
            print('\033[93m'+" 3 : le Match 3 est terminé." + "\x1b[0m")
        if not m_finished_4:
            if m_al_sta_4:
                print('\033[93m'+" 4 : Arreter le match 4." + "\x1b[0m")
            else:
                print('\033[93m'+" 4 : Démarrer le match 4." + "\x1b[0m")
        else:
            print('\033[93m'+" 4 : le Match 4 est terminé." + "\x1b[0m")
        print('\033[93m' + " 5 : Quitter le tournoi." + "\x1b[0m")
        # Inserer le resultat du match
        try:
            resultat = int(input('\033[91m'+"\nQuelle est votre choix : " + "\x1b[0m"))
            if resultat > 5 or resultat <= 0:
                self.print_error_enter_int()
                resultat = self.start_end_match_view(
                    m_finished_1=m_finished_1, m_finished_2=m_finished_2, m_finished_3=m_finished_3,
                    m_finished_4=m_finished_4, m_al_sta_1=m_al_sta_1, m_al_sta_2=m_al_sta_2,  m_al_sta_3=m_al_sta_3,
                    m_al_sta_4=m_al_sta_4)
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.start_end_match_view(
                m_finished_1=m_finished_1, m_finished_2=m_finished_2, m_finished_3=m_finished_3,
                m_finished_4=m_finished_4, m_al_sta_1=m_al_sta_1, m_al_sta_2=m_al_sta_2,  m_al_sta_3=m_al_sta_3,
                m_al_sta_4=m_al_sta_4)
        print('-----------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def enter_resultat_player(self, ref_joueur):
        # Inserer un résultat
        try:
            resultat = float(input('\033[92m' + " resultat du joueur N°{}: ".format(ref_joueur) + "\x1b[0m"))
            if resultat not in [0, 0.5, 1]:
                self.print_error_enter_int()
                resultat = self.enter_resultat_player(ref_joueur)
        except (ValueError, IndexError):
            resultat = self.enter_resultat_player(ref_joueur)
            self.print_error_enter_int()
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def print_error_enter_int():
        # indicates to the user that he must enter a number
        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à votre choix ." + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#
