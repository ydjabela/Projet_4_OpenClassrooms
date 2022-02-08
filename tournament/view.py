
# ---------------------------------------------------------------------------------------------------------------------#


class Sub_Choice:

    def sub_main_choice(self):
        print()
        print(" * * * Gestionnaire des Tournois. * * *\n")
        print(" /// Selectionnez le menu souhaité. /// \n")
        print(" 1 : Ajouter un tournoi.")
        print(" 2 : modifier un tournoi.")
        print(" 3 : Supprimmer un tournoi.")
        print(" 4 : Afficher les tournois.")
        print(" 6 : Supprimmer tous les tournois.")
        print(" 7 : Retour au menu principal.")
        print(" 8 : sortir du logiciel.")
        print()
        resultat = input("Quelle est votre choix : ")
        print('-------------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_modification_spec(self):
        print()
        print(" * * * Modification des tournois. * * *\n")
        print()
        print(" /// Selectionnez le menu souhaité. /// \n")
        print(" 1 : Modifier le Nom.")
        print(" 2 : Modifier le Lieu.")
        print(" 3 : Modifier la Date.")
        print(" 4 : Modifier le Tour.")
        print(" 5 : Modifier la Tournees.")
        print(" 6 : Modifier le Joueurs.")
        print(" 7 : Modifier le controle_temps.")
        print(" 8 : Modifier le Description.")

        resultat = input("Numero de l'élement de la  modif: ")
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#


class Tournament_view:

    def tournament_name_modification(self):
        print()
        name = input("Nouveau Nom: ")
        return name

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_lieu_modification(self):
        print()
        lieu = input("Nouveau Lieu: ")
        return lieu

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_date_modification(self):
        print()
        date = input("Nouveau date: ")
        return date

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_tour_modification(self):
        print()
        tour = input("Nouveau tour: ")
        return tour

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_Tournees_modification(self):
        print()
        Tournees = input("Nouvelle Tournees: ")
        return Tournees

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_Joueurs_modification(self):
        print()
        Joueurs = input("Nouveaux Joueurs: ")
        return Joueurs

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_controle_temps_modification(self):
        print()
        controle_temps = input("Nouveau controle temps: ")
        return controle_temps

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_Description_modification(self):
        print()
        Description = input("Nouvelle Description: ")
        return Description

    # ---------------------------------------------------------------------------------------------------------------------#

    def no_tournament(self):
        print('la liste des tournois est vide')

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_to_delete(self):
        print()
        print(" * * * Modification des tournois. * * *\n")
        print()

        resultat = input("Numéro  de tournoi que vous souhaité supprimer: ")
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def adding_tournament(self):

        nom = str(input('Nom : '))
        lieu = str(input('lieu: '))
        date = str(input('date : '))
        tour = str(input('tour: '))
        Tournees = str(input('Tournees : '))
        Joueurs = str(input('Joueurs: '))
        controle_temps = str(input('controle temps : '))
        Description = str(input('Description: '))

        serialized_tournoi = {
            'nom': nom,
            'lieu': lieu,
            'date': date,
            'tour': tour,
            'Tournees': Tournees,
            'Joueurs': Joueurs,
            'controle_temps': controle_temps,
            'Description': Description
        }
        return serialized_tournoi

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_modification_save(self):
        print()
        print(" * * * Modification Terminé. * * *\n")

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_modification(self):
        print()
        print(" * * * Modification des Tournois. * * *\n")
        print()

        resultat = input("Numéro  de tournoi que vous souhaité modifier: ")
        return resultat

# ---------------------------------------------------------------------------------------------------------------------#


class Error_enter:

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number

        print("\n ERREUR : vous devez entrer un chiffre correspondant à votre choix .")
