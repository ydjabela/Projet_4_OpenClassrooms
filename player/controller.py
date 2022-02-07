from player.model import Player
from player.view import Sub_Choice

# ---------------------------------------------------------------------------------------------------------------------#


class PlayerMenu:

    def sub_menu(self):
        sub_choice = Sub_Choice()
        player = Player()

        try:
            resultat = int(sub_choice.sub_main_choice())
        except:
            sub_choice.print_error_enter_int()
            self.sub_menu()

        # Ajouter un joueur.
        if resultat == 1:
            player.save_player()

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
                sub_choice.no_player()

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
            sub_choice.print_error_enter_int()
        print('-------------------------------------------------------------------------------------------------------')
        self.sub_menu()

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_player(self):
        sub_choice = Sub_Choice()
        player = Player()

        try:
            players = player.search_player()
            if len(players) == 0:
                sub_choice.no_player()
                self.sub_menu()
            elif len(players) == 1:
                player_number = 0
            else:
                player_number = int(sub_choice.player_modification()) - 1

            resultat_modif = int(sub_choice.player_modification_spec())
        except:
            sub_choice.print_error_enter_int()
            self.sub_menu_player()

        if resultat_modif == 1:
            name = sub_choice.player_name_modification()
            player.ask_change_name(name=name, player_number=player_number)
            sub_choice.player_modification_save()
        elif resultat_modif == 2:
            prenom = sub_choice.player_first_name_modification()
            player.ask_change_first_name(prenom=prenom, player_number=player_number)
        elif resultat_modif == 3:
            self.change_age_player(player_number=player_number)
        elif resultat_modif == 4:
            sex = sub_choice.player_sex_modification()
            player.ask_change_sex(sex=sex, player_number=player_number)
        elif resultat_modif == 5:
            self.change_classement_player(player_number=player_number)

    # -----------------------------------------------------------------------------------------------------------------#

    def change_age_player(self, player_number):
        sub_choice = Sub_Choice()
        player = Player()
        try:
            age = int(sub_choice.player_age_modification())
            player.ask_change_age(age=age, player_number=player_number)
        except:
            sub_choice.print_error_enter_int()
            self.change_age_player(player_number=player_number)

    # -----------------------------------------------------------------------------------------------------------------#

    def change_classement_player(self, player_number):
        sub_choice = Sub_Choice()
        player = Player()
        try:
            classement = int(sub_choice.player_classement_modification())
            player.ask_change_classement(classement=classement, player_number=player_number)
        except:
            sub_choice.print_error_enter_int()
            self.change_classement_player(player_number=player_number)

    # -----------------------------------------------------------------------------------------------------------------#

    def delete_player(self):
        sub_choice = Sub_Choice()
        player = Player()
        players = player.search_player()
        try:
            player_number = int(sub_choice.player_to_delete())-1
            player.ask_delete_player(player_number=player_number)
            sub_choice.player_modification_save()
        except:
            sub_choice.print_error_enter_int()
            self.delete_player()
# ---------------------------------------------------------------------------------------------------------------------#
