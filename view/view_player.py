
# ---------------------------------------------------------------------------------------------------------------------#


class Msg_Player:

    @staticmethod
    def print_error_enter_int_age():
        # indicates to the user that he must enter a number
        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à l'age de  joueur! ." + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def print_error_enter_int_classement():
        # indicates to the user that he must enter a number
        print(
            '\033[91m' +
            "\n ERREUR : vous devez entrer un chiffre correspondant au classement du joueur! ." +
            "\x1b[0m"
        )

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def print_error_enter_int():
        # indicates to the user that he must enter a number
        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à votre choix ." + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def message_visit():
        print('Merci pour  votre visite')

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def message_retour():
        print('Retour au menu principal')

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def message_player_max():
        print('\033[91m'+'\nLe nombre maximum des joueurs est atteint' + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def message_selection_complete():
        print('\033[91m'+'\nLa selection des  joueur est complete' + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def print_error_classement_exist():
        # indicates to the user that he must enter a number
        print(
            '\033[91m' +
            "\n ERREUR :classement existe deja! ." +
            "\x1b[0m"
        )

    # -----------------------------------------------------------------------------------------------------------------#


class Player_view(Msg_Player):

    def player_sub_main_choice(self):
        print('\033[92m' + "\n * * * Gestionnaire des joueurs. * * *\n" + "\x1b[0m")
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Ajouter un joueur." + "\x1b[0m")
        print('\033[93m'+" 2 : modifier un joueur." + "\x1b[0m")
        print('\033[93m'+" 3 : Supprimmer un joueur." + "\x1b[0m")
        print('\033[93m'+" 4 : Affichage des joueurs." + "\x1b[0m")
        print('\033[93m'+" 5 : Afficher le classement des joueurs." + "\x1b[0m")
        print('\033[93m'+" 6 : Supprimmer tous les joueurs." + "\x1b[0m")
        print('\033[93m'+" 7 : Retour au menu principal." + "\x1b[0m")
        print('\033[93m'+" 8 : sortir du logiciel." + "\x1b[0m")
        try:
            resultat = int(input('\033[91m'+"\nQuelle est votre choix : " + "\x1b[0m"))
            if resultat > 8 or resultat <= 0:
                self.print_error_enter_int()
                resultat = self.player_sub_main_choice()
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.player_sub_main_choice()
        print('-----------------------------------------------------------------------------------------------------')
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    def player_modification_spec(self):
        print('\033[92m' + "\n * * * Modification des joueurs. * * *\n" + "\x1b[0m")
        print("\n /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Modifier le  Nom." + "\x1b[0m")
        print('\033[93m'+" 2 : Modifier le  Prenom." + "\x1b[0m")
        print('\033[93m'+" 3 : Modifier le  l'age." + "\x1b[0m")
        print('\033[93m'+" 4 : Modifier le  le sex." + "\x1b[0m")
        print('\033[93m'+" 5 : Modifier le  Classement." + "\x1b[0m")

        try:
            resultat = int(input('\033[91m' + "Numero de l'élement de la  modif: " + "\x1b[0m"))
            # En cas le  player number n'existe pas
            if resultat >= 6 or resultat < 0:
                self.print_error_enter_int()
                resultat = self.player_modification_spec()
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.player_modification_spec()
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def player_name_modification():
        name = input("\nNouveau Nom: ")
        return name

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def player_first_name_modification():
        prenom = input("\nNouveau prénom: ")
        return prenom

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def player_age_modification():
        age = input("\nNouveau age: ")
        return age

    # -----------------------------------------------------------------------------------------------------------------#

    def player_sex_modification(self):
        genre = input("\nNouveau genre: ")
        if genre not in ['m', 'M', 'f', 'F']:
            print('\033[91m' + 'Veuillez saisir M/m ou F/f' + "\x1b[0m")
            genre = self.player_sex_modification()
        return genre

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def player_classement_modification():
        classement = input("\nNouveau classement: ")

        return classement

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def no_player():
        print('\033[92m' + 'la liste des joueurs est vide' + "\x1b[0m")

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def need_add_players():
        print('\033[92m' + 'Il faut ajouter 8 joueurs pour commencer la partie' + "\x1b[0m")

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def player_to_delete():
        print('\033[92m' + "\n * * * Modification des joueurs. * * *\n" + "\x1b[0m")
        resultat = input('\033[91m'+"Numéro  de joueur que vous souhaité supprimer: " + "\x1b[0m")
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    def player_to_select(self, players):
        try:
            resultat = int(input('\033[91m' + "Numéro  de joueur que vous souhaité selectionné: " + "\x1b[0m"))
            if resultat > len(players) - 1 or resultat < 0:
                self.print_error_enter_int()
                resultat = self.player_to_select(players=players)
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.player_to_select(players=players)
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    def add_age(self):
        try:
            age = int(input('age: '))
            if age <= 0 or age > 120:
                self.print_error_enter_int_age()
                age = self.add_age()
        except ValueError:
            self.print_error_enter_int_age()
            age = self.add_age()
        return age

    # -----------------------------------------------------------------------------------------------------------------#

    def add_classement(self, players):
        first_list = list()
        # construire une liste avec les noms de tous les joueurs
        for player in players:
            first_list.append(player['classement'])
        try:
            Classement = int(input('Classement: '))
            if Classement <= 0:
                self.print_error_enter_int_age()
                Classement = self.add_classement(players=players)
            if Classement in first_list:
                self.print_error_classement_exist()
                Classement = self.add_classement(players=players)
        except ValueError:
            self.print_error_enter_int_classement()
            Classement = self.add_classement(players=players)
        return Classement

    # -----------------------------------------------------------------------------------------------------------------#

    def add_sex(self):
        sex = str(input('sex (M or F): '))
        if sex not in ['m', 'M', 'f', 'F']:
            print('\033[91m'+'Veuillez saisir M/m ou F/f' + "\x1b[0m")
            sex = self.add_sex()
        return sex

    # -----------------------------------------------------------------------------------------------------------------#

    def adding_player(self, players):

        familly_name = str(input('Nom : '))
        first_name = str(input('prénom: '))
        age = self.add_age()
        sex = self.add_sex()
        classement = self.add_classement(players=players)

        return familly_name, first_name, age, sex, classement

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def player_modification_save():
        print('\033[92m' + "\n * * * Modification Terminé. * * *\n" + "\x1b[0m")

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def search_player_view(players):
        try:
            if not len(players) == 0:
                i = 0
                print('\nles joueurs sont : ')
                print(
                    "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                        "N°", "Familly name", "First name", "Age", "Sex", "Classement"
                    )
                )
                for player in players:
                    familly_name = player['familly_name']
                    first_name = player['first_name']
                    age = player['age']
                    sex = player['sex']
                    classement = player['classement']
                    print(
                        "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                            i, familly_name, first_name, age, sex, classement
                        )
                    )
                    i += 1

        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def player_modification(self, players):
        print('\033[92m' + "\n * * * Modification des joueurs. * * *\n" + "\x1b[0m")
        try:
            resultat = int(input('\033[91m'+"Numéro  de joueur que vous souhaité modifier: " + "\x1b[0m"))
            # En cas le  player number n'existe pas
            if resultat >= len(players) or resultat < 0:
                self.print_error_enter_int()
                resultat = self.player_modification(players=players)
        except (ValueError, IndexError):
            self.print_error_enter_int()
            resultat = self.player_modification(players=players)
        return resultat

    # -----------------------------------------------------------------------------------------------------------------#

    def select_player(self, players):
        print('les  joueurs a selectionner sont: ')
        i = 0
        for player in players:
            print(i, ':', player)
            i += 1
        player_number = self.player_to_select(players=players)
        selected_player = players[player_number]

        return selected_player

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def view_statique_player(player_tri_ranking, player_tri_alphabet):
        try:
            if not len(player_tri_ranking) == 0:
                i = 1
                print('Classement des  joueurs  par ordre de classement : ')
                print(
                    "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                        "N°", "Familly name", "First name", "Age", "Sex", "Classement"
                    )
                )
                for player in player_tri_ranking:
                    familly_name = player['familly_name']
                    first_name = player['first_name']
                    age = player['age']
                    sex = player['sex']
                    classement = player['classement']
                    print(
                        "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                            i, familly_name, first_name, age, sex, classement
                        )
                    )
                    i += 1

                print('\nClassement des  joueurs  par ordre alphabetique : ')
                print(
                    "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                        "N°", "Familly name", "First name", "Age", "Sex", "Classement"
                    )
                )
                i = 1

                for player in player_tri_alphabet:
                    familly_name = player['familly_name']
                    first_name = player['first_name']
                    age = player['age']
                    sex = player['sex']
                    classement = player['classement']
                    print(
                        "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                            i, familly_name, first_name, age, sex, classement
                        )
                    )
                    i += 1

        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    @staticmethod
    def search_player_view_classement(players):
        print('\nClassement des  joueurs  par ordre de classement : ')
        print("{:<25} {:<25} {:<25}".format('Joueur', 'points', 'classement'))
        for player in players:
            if len(player) == 3:
                Joueur, points, classement = player
                print("{:<25} {:<25} {:<25}".format(Joueur, points, classement))
            else:
                Joueur, classement = player
                points = 0
                print("{:<25} {:<25} {:<25}".format(Joueur, points, classement))

    # -----------------------------------------------------------------------------------------------------------------#
