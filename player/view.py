
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
        print()
        resultat = input("Quelle est votre choix : ")
        print('-------------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_modification_spec(self):
        print()
        print(" * * * Modification des joueurs. * * *\n")
        print()
        print(" /// Selectionnez le menu souhaité. /// \n")
        print(" 1 : Modifier le  Nom.")
        print(" 2 : Modifier le  Prenom.")
        print(" 3 : Modifier le  l'age.")
        print(" 4 : Modifier le  le sex.")
        print(" 5 : Modifier le  Classement.")

        resultat = input("Numero de l'élement de la  modif: ")
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#


class Player_view:

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
        return genre

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_classement_modification(self):
        print()
        classement = input("Nouveau classement: ")
        return classement
    # ---------------------------------------------------------------------------------------------------------------------#

    def no_player(self):
        print('la liste des joueurs est vide')

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_to_delete(self):
        print()
        print(" * * * Modification des joueurs. * * *\n")
        print()

        resultat = input("Numéro  de joueur que vous souhaité supprimer: ")
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def add_age(self):
        error_enter = Error_enter()
        try:
            age = int(input('age: '))
        except:
            error_enter.print_error_enter_int_age()
            age = self.add_age()
        return age
    # ---------------------------------------------------------------------------------------------------------------------#

    def add_classement(self):
        error_enter = Error_enter()
        try:
            Classement = int(input('Classement: '))
        except:
            error_enter.print_error_enter_int_classement()
            Classement = self.add_classement()
        return Classement

    # ---------------------------------------------------------------------------------------------------------------------#

    def adding_player(self):

        familly_name = str(input('familly_name : '))
        first_name = str(input('first_name: '))
        age = self.add_age()
        sex = str(input('sex: '))
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
        print(" * * * Modification Terminé. * * *\n")

    # ---------------------------------------------------------------------------------------------------------------------#

    def player_modification(self):
        print()
        print(" * * * Modification des joueurs. * * *\n")
        print()

        resultat = input("Numéro  de joueur que vous souhaité modifier: ")
        return resultat

# ---------------------------------------------------------------------------------------------------------------------#


class Error_enter:

    def print_error_enter_int_age(self):
        # indicates to the user that he must enter a number

        print("\n ERREUR : vous devez entrer un chiffre correspondant à l'age de  joueur! .")

    def print_error_enter_int_classement(self):
        # indicates to the user that he must enter a number

        print("\n ERREUR : vous devez entrer un chiffre correspondant au classement du joueur! .")

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number

        print("\n ERREUR : vous devez entrer un chiffre correspondant à votre choix .")
