from player.model import Player
from player.view import Sub_Choice, Player_view, Error_enter

# ---------------------------------------------------------------------------------------------------------------------#


class PlayerMenu:

    def sub_menu(self):
        error_enter =Error_enter()
        sub_choice = Sub_Choice()
        player = Player()
        player_view = Player_view()

        try:
            resultat = int(sub_choice.sub_main_choice())
        except:
            error_enter.print_error_enter_int()
            self.sub_menu()

        # Ajouter un joueur.
        if resultat == 1:
            serialized_player = player_view.adding_player()
            player.save_player(serialized_player)

        # modifier un joueur.
        elif resultat == 2:
            self.sub_menu_player()
        # Supprimmer un joueur.
        elif resultat == 3:
            self.delete_player()

        # Affichage des joueurs.
        elif int(resultat) == 4:
            players = player.search_player()
            if len(players) == 0:
                player_view.no_player()

        # Supprimmer tous les joueurs.
        elif int(resultat) == 5:
            player.delete_all_player()

        # Retour au menu principal
        elif resultat == 6:
            print('Retour au menu principal')
            return

        # sortir du logiciel
        elif resultat == 7:
            print('Merci pour  votre visite')
            exit()

        else:
            error_enter.print_error_enter_int()
        print('-------------------------------------------------------------------------------------------------------')
        self.sub_menu()

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_player(self):
        error_enter = Error_enter()
        sub_choice = Sub_Choice()
        player = Player()
        player_view = Player_view()

        try:
            players = player.search_player()
            if len(players) == 0:
                player_view.no_player()
                self.sub_menu()
            elif len(players) == 1:
                player_number = 0
            else:
                player_number = int(player_view.player_modification()) - 1

            resultat_modif = int(sub_choice.player_modification_spec())
        except:
            error_enter.print_error_enter_int()
            self.sub_menu_player()

        if resultat_modif == 1:
            name = player_view.player_name_modification()
            player.ask_change_name(name=name, player_number=player_number)
            player_view.player_modification_save()
        elif resultat_modif == 2:
            prenom = player_view.player_first_name_modification()
            player.ask_change_first_name(prenom=prenom, player_number=player_number)
        elif resultat_modif == 3:
            self.change_age_player(player_number=player_number)
        elif resultat_modif == 4:
            sex = player_view.player_sex_modification()
            player.ask_change_sex(sex=sex, player_number=player_number)
        elif resultat_modif == 5:
            self.change_classement_player(player_number=player_number)

    # -----------------------------------------------------------------------------------------------------------------#

    def change_age_player(self, player_number):
        player = Player()
        player_view = Player_view()
        error_enter = Error_enter()
        try:
            age = int(player_view.player_age_modification())
            player.ask_change_age(age=age, player_number=player_number)
        except:
            error_enter.print_error_enter_int_age()
            self.change_age_player(player_number=player_number)

    # -----------------------------------------------------------------------------------------------------------------#

    def change_classement_player(self, player_number):
        player = Player()
        player_view = Player_view()
        error_enter = Error_enter()
        try:
            classement = int(player_view.player_classement_modification())
            player.ask_change_classement(classement=classement, player_number=player_number)
        except:
            error_enter.print_error_enter_int_classement()
            self.change_classement_player(player_number=player_number)

    # -----------------------------------------------------------------------------------------------------------------#

    def delete_player(self):
        player_view = Player_view()
        player = Player()
        players = player.search_player()
        error_enter = Error_enter()
        try:
            player_number = int(player_view.player_to_delete())-1
            player.ask_delete_player(player_number=player_number)
            player_view.player_modification_save()
        except:
            error_enter.print_error_enter_int()
            self.delete_player()

# ---------------------------------------------------------------------------------------------------------------------#
