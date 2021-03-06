import settings


# ---------------------------------------------------------------------------------------------------------------------#


class Msg_Tournament:

    @staticmethod
    def message_visit():
        print('Merci pour  votre visite')

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def message_retour():
        print('Retour au menu principal')

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def print_error_enter_int():
        # indicates to the user that he must enter a number
        print('\033[91m' +
              "\n ERREUR : vous devez entrer un chiffre correspondant à votre choix." +
              "\x1b[0m"
              )

# ---------------------------------------------------------------------------------------------------------------------#


class Tournament_view(Msg_Tournament):
    def tournament_sub_main_choice(self):
        print('\033[92m' +
              "\n * * * Gestionnaire des Tournois. * * *\n" +
              "\x1b[0m"
              )
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Ajouter un tournoi." + "\x1b[0m")
        print('\033[93m'+" 2 : modifier un tournoi." + "\x1b[0m")
        print('\033[93m'+" 3 : Supprimmer un tournoi." + "\x1b[0m")
        print('\033[93m'+" 4 : Afficher les tournois." + "\x1b[0m")
        print('\033[93m'+" 5 : Supprimmer tous les tournois." + "\x1b[0m")
        print('\033[93m'+" 6 : Retour au menu principal." + "\x1b[0m")
        print('\033[93m'+" 7 : sortir du logiciel." + "\x1b[0m")

        try:
            resultat = int(input('\033[91m'+"\nQuelle est votre choix : " + "\x1b[0m"))
            if resultat > 7 or resultat <= 0:
                self.print_error_enter_int()
                resultat = self.tournament_sub_main_choice()
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.tournament_sub_main_choice()
        print('-----------------------------------------------------------------------------------------------------')
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    def tournament_modification_spec(self):
        print('\033[92m' +
              " \n* * * Modification des tournois. * * *\n" +
              "\x1b[0m"
              )
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Modifier le Nom." + "\x1b[0m")
        print('\033[93m'+" 2 : Modifier le Lieu." + "\x1b[0m")
        print('\033[93m'+" 3 : Modifier la Date." + "\x1b[0m")
        print('\033[93m'+" 4 : Modifier le Tour." + "\x1b[0m")
        print('\033[93m'+" 5 : Modifier la Tournees." + "\x1b[0m")
        print('\033[93m'+" 6 : Modifier le Joueurs." + "\x1b[0m")
        print('\033[93m'+" 7 : Modifier le controle_temps." + "\x1b[0m")
        print('\033[93m'+" 8 : Modifier le Description." + "\x1b[0m")
        try:
            resultat = int(input('\033[91m' + "Numero de l'élement de la  modif: " + "\x1b[0m"))
            if resultat > 8 or resultat <= 0:
                self.print_error_enter_int()
                resultat = self.tournament_modification_spec()
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.tournament_modification_spec()
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_name_modification():
        name = input("\nNouveau Nom: ")
        return name

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_lieu_modification():
        lieu = input("\nNouveau Lieu: ")
        return lieu

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_date_modification():
        date = input("\nNouveau date: ")
        return date

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_tour_modification():
        tour = input("\nNouveau tour: ")
        return tour

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_tournees_modification():
        print(
            '\033[91m' +
            "\nVous ne  pouvez pas  modifier cette  partie" +
            "\x1b[0m"
        )

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_Joueurs_modification():
        Joueur = input("\nNouveau Joueur: ")
        return Joueur

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_controle_temps_modification():
        controle_temps = input("\nNouveau controle temps: ")
        return controle_temps

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_Description_modification():
        Description = input("\nNouvelle Description: ")
        return Description

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def no_tournament():
        print(
            '\033[92m' +
            'la liste des tournois est vide' +
            "\x1b[0m"
        )

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def one_tournament_existed():
        print(
            '\033[92m' +
            'il existe  un seul tournois' +
            "\x1b[0m"
        )

    # -----------------------------------------------------------------------------------------------------------------#

    def tournament_to_delete(self, tournaments):
        print(
            '\n\033[92m' +
            " * * * Modification des tournois. * * *\n" +
            "\x1b[0m"
        )
        try:
            resultat = int(input(
                '\033[91m' +
                "Numéro  de tournoi que vous souhaité supprimer: " +
                "\x1b[0m"
            )) - 1
            if resultat > len(tournaments) - 1 or resultat <= 0:
                self.print_error_enter_int()
                resultat = self.tournament_to_delete(tournaments=tournaments)
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.tournament_to_delete(tournaments=tournaments)

        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    def tournament_to_play(self, tournaments):
        try:
            resultat = int(input(
                '\033[91m' +
                "\nNuméro  de tournoi que vous souhaité commencé a jouer: " +
                "\x1b[0m"
            )) - 1
            if resultat > len(tournaments)-1 or resultat < 0:
                self.print_error_enter_int()
                resultat = self.tournament_to_play(tournaments=tournaments)
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.tournament_to_play(tournaments=tournaments)
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    def tournament_chosed_view(self, tournament_number, tournaments):

        print('\033[92m' + "Le Tournoi qui à été choisi est :" + "\x1b[0m")
        tournament = tournaments[tournament_number]
        self.search_tournament_view(tournaments=[tournament])

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def tournament_modification_save():
        print('\033[92m' + "\n * * * Modification Terminé. * * *\n" + "\x1b[0m")

    # -----------------------------------------------------------------------------------------------------------------#

    def tournament_modification(self, tournaments):
        print(
            '\033[92m' +
            "\n * * * Modification des tournois. * * *\n" +
            "\x1b[0m"
        )
        try:
            resultat = int(input(
                '\033[91m' +
                "Numéro  de tournoi que vous souhaité modifier: " +
                "\x1b[0m"
            )) - 1
            if resultat > len(tournaments)-1 or resultat <= 0:
                self.print_error_enter_int()
                resultat = self.tournament_modification(tournaments=tournaments)
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.tournament_modification(tournaments=tournaments)
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def adding_tournament(without_player=True):
        nom = str(input('Nom du tournoi: '))
        lieu = str(input('lieu: '))
        date = str(input('date: '))
        tour = settings.TURNS
        tournees = ''
        joueurs = ''
        if not without_player:
            joueurs = list(input('Joueurs: '))
        controle_temps = input('controle_temps: ')
        description = str(input('Description: '))

        return nom, lieu, date, tour, tournees, joueurs, controle_temps, description

    # -----------------------------------------------------------------------------------------------------------------#

    def match_round_x_view(self, Tournees, dict_points):
        match_number = 1
        for match in Tournees:
            if match_number == 1:
                print('\nRound 1:')
            if match_number == 5:
                print('\nRound 2:')
            if match_number == 9:
                print('\nRound 3:')
            if match_number == 13:
                print('\nRound 4:')
            joueur_1, joueur_2, start_match_time, end_match_time = match
            ref_joueur_1, score_joueur_1, color_joueur_1 = joueur_1
            ref_joueur_2, score_joueur_2, color_joueur_2 = joueur_2
            if color_joueur_1 == 'Blanche':
                bullet_joueur_1 = u"\u2765"
                bullet_joueur_2 = '\033[90m' + u"\u2765" + "\x1b[0m"
            else:
                bullet_joueur_1 = '\033[90m' + u"\u2765" + "\x1b[0m"
                bullet_joueur_2 = u"\u2765"
            if start_match_time != 0:
                start_match = ' Demmarer à: {}'.format(start_match_time)
                if end_match_time != 0:
                    end_match = ' Terminé à: {}'.format(end_match_time)
                else:
                    end_match = "Le Match n'est pas encore Terminé"
            else:
                start_match = "le match n'a pas encore demmaré"
                end_match = ''
            print(
                'Match N°{}:'.format(match_number),
                '\033[92m' + " joueur N°{}".format(ref_joueur_1) + "\x1b[0m" +
                " {} ".format(bullet_joueur_1) + "VS " + "{} ".format(bullet_joueur_2) +
                '\033[92m' + "joueur N°{} ".format(ref_joueur_2) + "\x1b[0m" +
                "| Score : ({}-{})".format(score_joueur_1, score_joueur_2) +
                start_match + end_match
            )
            match_number += 1
            dict_points[ref_joueur_1] += score_joueur_1
            dict_points[ref_joueur_2] += score_joueur_2

    # -----------------------------------------------------------------------------------------------------------------#

    def search_tournament_view(self, tournaments):
        dict_points = dict()
        if not len(tournaments) == 0:
            print('\033[92m' + " \nTournois:\n" + "\x1b[0m")
            i = 1
            for tournament in tournaments:
                nom = tournament['nom']
                lieu = tournament['lieu']
                date = tournament['date']
                tour = tournament['tour']
                Joueurs = tournament['Joueurs']
                controle_temps = tournament['controle_temps']
                Description = tournament['Description']
                print("N°: {} \n Nom: {} \n Lieu: {} \n Date: {} \n Tour: {} \n Joueurs: {} \n Controle temps: {} \n "
                      "Description: {}".format(i, nom, lieu, date, tour, Joueurs, controle_temps, Description))
                for joueur in Joueurs:
                    dict_points[joueur] = 0
                Tournees = tournament['Tournees']
                if Tournees != '':
                    try:
                        self.match_round_x_view(Tournees=Tournees, dict_points=dict_points)
                        sorted_points = sorted(dict_points.items(), key=lambda t: t[1], reverse=True)
                        print('\033[92m' + " \nClassement des joueurs  par  nombre de  points:" + "\x1b[0m")
                        print("{:<25} {:<25} {:<25}".format("Classement", "joueurs", "Points"))
                        k = 1
                        for key, value in sorted_points:
                            print("{:<25} {:<25} {:<25}".format(k, key, value))
                            k += 1
                    except (ValueError, IndexError):
                        print("Les matchs  n'ont pas encore debuté  pour ce tournoi")
                else:
                    print("Les matchs  n'ont pas encore debuté  pour ce tournoi")
                i += 1
                print('-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-')

# ---------------------------------------------------------------------------------------------------------------------#
