
# ---------------------------------------------------------------------------------------------------------------------#


class Msg_Player:


    def print_error_enter_int_age(self):
        # indicates to the user that he must enter a number
        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à l'age de  joueur! ." + "\x1b[0m")

    def print_error_enter_int_classement(self):
        # indicates to the user that he must enter a number
        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant au classement du joueur! ." + "\x1b[0m")

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number
        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à votre choix ." + "\x1b[0m")

    def message_visit(self):
        print('Merci pour  votre visite')

    def message_retour(self):
        print('Retour au menu principal')

    # ---------------------------------------------------------------------------------------------------------------------#


class Player_view(Msg_Player):

    def sub_main_choice(self):
        print()
        print('\033[92m' + " * * * Gestionnaire des joueurs. * * *\n" + "\x1b[0m")
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Ajouter un joueur." + "\x1b[0m")
        print('\033[93m'+" 2 : modifier un joueur." + "\x1b[0m")
        print('\033[93m'+" 3 : Supprimmer un joueur." + "\x1b[0m")
        print('\033[93m'+" 4 : Affichage des joueurs." + "\x1b[0m")
        print('\033[93m'+" 5 : Afficher le classement des joueurs." + "\x1b[0m")
        print('\033[93m'+" 6 : Supprimmer tous les joueurs." + "\x1b[0m")
        print('\033[93m'+" 7 : Retour au menu principal." + "\x1b[0m")
        print('\033[93m'+" 8 : sortir du logiciel." + "\x1b[0m")
        print()
        resultat = input('\033[91m'+"Quelle est votre choix : " + "\x1b[0m")
        print('-------------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_modification_spec(self):
        print()
        print('\033[92m' +" * * * Modification des joueurs. * * *\n" + "\x1b[0m")
        print()
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Modifier le  Nom." + "\x1b[0m")
        print('\033[93m'+" 2 : Modifier le  Prenom." + "\x1b[0m")
        print('\033[93m'+" 3 : Modifier le  l'age." + "\x1b[0m")
        print('\033[93m'+" 4 : Modifier le  le sex." + "\x1b[0m")
        print('\033[93m'+" 5 : Modifier le  Classement." + "\x1b[0m")

        resultat = input('\033[91m' + "Numero de l'élement de la  modif: " + "\x1b[0m")
        return resultat

    def player_name_modification(self):
        print()
        name = input("Nouveau Nom: ")
        return name

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_first_name_modification(self):
        print()
        prenom = input("Nouveau prénom: ")
        return prenom

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_age_modification(self):
        print()
        age = input("Nouveau age: ")
        return age

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_sex_modification(self):
        print()
        genre = input("Nouveau genre: ")
        if genre not in ['m', 'M', 'f', 'F']:
            print('\033[91m'+ 'Veuillez saisir M/m ou F/f' + "\x1b[0m")
            genre = self.player_sex_modification()
        return genre

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_classement_modification(self):
        print()
        classement = input("Nouveau classement: ")
        return classement

    # ---------------------------------------------------------------------------------------------------------------------#

    def no_player(self):
        print('\033[92m' +'la liste des joueurs est vide' + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_to_delete(self):
        print()
        print('\033[92m' +" * * * Modification des joueurs. * * *\n" + "\x1b[0m")
        print()

        resultat = input('\033[91m'+"Numéro  de joueur que vous souhaité supprimer: " + "\x1b[0m")
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def add_age(self):
        try:
            age = int(input('age: '))
            if age <= 0 and age > 120:
                self.print_error_enter_int_age()
                age = self.add_age()
        except:
            self.print_error_enter_int_age()
            age = self.add_age()
        return age

    # ---------------------------------------------------------------------------------------------------------------------#

    def add_classement(self):
        try:
            Classement = int(input('Classement: '))
        except:
            self.print_error_enter_int_classement()
            Classement = self.add_classement()
        return Classement

    # ---------------------------------------------------------------------------------------------------------------------#

    def add_sex(self):
        sex = str(input('sex (M or F): '))
        if sex not in ['m', 'M', 'f', 'F']:
            print('\033[91m'+'Veuillez saisir M/m ou F/f' + "\x1b[0m")
            sex = self.add_sex()
        return sex

    # ---------------------------------------------------------------------------------------------------------------------#

    def adding_player(self):

        familly_name = str(input('Nom : '))
        first_name = str(input('prénom: '))
        age = self.add_age()
        sex = self.add_sex()
        classement = self.add_classement()
        serialized_player = {
            'familly_name': familly_name,
            'first_name': first_name,
            'age': age,
            'sex': sex,
            'classement': classement
        }
        return serialized_player

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_modification_save(self):
        print()
        print('\033[92m' + " * * * Modification Terminé. * * *\n" + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    def search_player_view(self, players):
        try:
            if not len(players) == 0:
                i = 1
                print('les joueurs sont : ')
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

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_modification(self):
        print()
        print('\033[92m' + " * * * Modification des joueurs. * * *\n" + "\x1b[0m")
        print()

        resultat = input('\033[91m'+"Numéro  de joueur que vous souhaité modifier: " + "\x1b[0m")
        return resultat

    def view_statique_player(self, player_tri_ranking, player_tri_alphabet):
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
                print()
                print('Classement des  joueurs  par ordre alphabetique : ')
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


