
# ---------------------------------------------------------------------------------------------------------------------#


class Sub_Choice_Tournament:

    def sub_main_choice(self):
        print()
        print('\033[92m' + " * * * Gestionnaire des Tournois. * * *\n" + "\x1b[0m")
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Ajouter un tournoi." + "\x1b[0m")
        print('\033[93m'+" 2 : modifier un tournoi." + "\x1b[0m")
        print('\033[93m'+" 3 : Supprimmer un tournoi." + "\x1b[0m")
        print('\033[93m'+" 4 : Afficher les tournois." + "\x1b[0m")
        print('\033[93m'+" 6 : Supprimmer tous les tournois." + "\x1b[0m")
        print('\033[93m'+" 7 : Retour au menu principal." + "\x1b[0m")
        print('\033[93m'+" 8 : sortir du logiciel." + "\x1b[0m")
        print()
        resultat = input('\033[91m'+"Quelle est votre choix : "+ "\x1b[0m")
        print('-------------------------------------------------------------------------------------------------------')
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_modification_spec(self):
        print()
        print('\033[92m' + " * * * Modification des tournois. * * *\n"+ "\x1b[0m")
        print()
        print(" /// Selectionnez le menu souhaité. /// \n")
        print('\033[93m'+" 1 : Modifier le Nom."+ "\x1b[0m")
        print('\033[93m'+" 2 : Modifier le Lieu."+ "\x1b[0m")
        print('\033[93m'+" 3 : Modifier la Date."+ "\x1b[0m")
        print('\033[93m'+" 4 : Modifier le Tour."+ "\x1b[0m")
        print('\033[93m'+" 5 : Modifier la Tournees."+ "\x1b[0m")
        print('\033[93m'+" 6 : Modifier le Joueurs."+ "\x1b[0m")
        print('\033[93m'+" 7 : Modifier le controle_temps."+ "\x1b[0m")
        print('\033[93m'+" 8 : Modifier le Description."+ "\x1b[0m")

        resultat = input('\033[91m'+"Numero de l'élement de la  modif: "+ "\x1b[0m")
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
        print('\033[92m' + 'la liste des tournois est vide' + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_to_delete(self):
        print()
        print('\033[92m' + " * * * Modification des tournois. * * *\n" + "\x1b[0m")
        print()

        resultat = input('\033[91m'+"Numéro  de tournoi que vous souhaité supprimer: " + "\x1b[0m")
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_modification_save(self):
        print()
        print('\033[92m' + " * * * Modification Terminé. * * *\n" + "\x1b[0m")

    # ---------------------------------------------------------------------------------------------------------------------#

    def tournament_modification(self):
        print()
        print('\033[92m' + " * * * Modification des tournois. * * *\n" + "\x1b[0m")
        print()

        resultat = input('\033[91m'+"Numéro  de tournoi que vous souhaité modifier: " + "\x1b[0m")
        return resultat

    # ---------------------------------------------------------------------------------------------------------------------#

    def adding_tournament(self):
        nom = str(input('Nom du tournoi: '))
        lieu = str(input('lieu: '))
        date = str(input('date: '))
        tour = input('tour: ')
        Tournees = input('Tournees: ')
        Joueurs = input('Joueurs: ')
        controle_temps = input('controle_temps: ')
        Description = str(input('Description: '))
        serialized_player = {
            'nom': nom,
            'lieu': lieu,
            'date': date,
            'tour': tour,
            'Tournees': Tournees,
            'Joueurs': Joueurs,
            'controle_temps': controle_temps,
            'Description': Description
     }
        return serialized_player


# ---------------------------------------------------------------------------------------------------------------------#


class Msg_Tournament:
    def message_visit(self):
        print('Merci pour  votre visite')

    def message_retour(self):
        print('Retour au menu principal')
# ---------------------------------------------------------------------------------------------------------------------#


class Error_enter_Tournament:

    def print_error_enter_int(self):
        # indicates to the user that he must enter a number

        print('\033[91m'+"\n ERREUR : vous devez entrer un chiffre correspondant à votre choix." + "\x1b[0m")