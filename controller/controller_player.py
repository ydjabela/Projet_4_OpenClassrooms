from model.model_player import Player, Player_Stat
from view.view_player import Player_view
import settings


class PlayerMenu(Player, Player_view, Player_Stat):

    def sub_menu_player_1(self):
        resultat = 0
        try:
            resultat = int(self.player_sub_main_choice())
        except:
            self.print_error_enter_int()
            self.sub_menu_player_1()

        # Ajouter un joueur.
        if resultat == 1:
            players = self.search_player()
            serialized_player = self.adding_player()
            self.save_player(serialized_player)

        # modifier un joueur.
        elif resultat == 2:
            self.sub_menu_player_2()

        # Supprimmer un joueur.
        elif resultat == 3:
            self.delete_player()

        # Affichage des joueurs.
        elif int(resultat) == 4:
            players = self.search_player()
            self.search_player_view(players=players)
            if len(players) == 0:
                self.no_player()

        # classement des joueurs
        elif int(resultat) == 5:
            player_tri_ranking, player_tri_alphabet = self.stat_classement()
            self.view_statique_player(
                player_tri_ranking=player_tri_ranking,
                player_tri_alphabet=player_tri_alphabet
            )

        # Supprimmer tous les joueurs.
        elif int(resultat) == 6:
            self.delete_all_player()

        # Retour au menu principal
        elif resultat == 7:
            self.message_retour()
            return

        # sortir du logiciel
        elif resultat == 8:
            self.message_visit()
            exit()

        else:
            self.print_error_enter_int()
        self.sub_menu_player_1()

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_player_2(self):
        resultat_modif = 0
        player_number = 0
        try:
            players = self.search_player()
            self.search_player_view(players=players)
            if len(players) == 0:
                self.no_player()
                self.sub_menu_player_1()
            elif len(players) == 1:
                player_number = 0
            else:
                player_number = int(self.player_modification()) - 1

            resultat_modif = int(self.player_modification_spec())
        except:
            self.print_error_enter_int()
            self.sub_menu_player_2()

        if resultat_modif == 1:
            name = self.player_name_modification()
            self.ask_change_value(player_number=player_number, key='familly_name', value=name)
            self.player_modification_save()
        elif resultat_modif == 2:
            prenom = self.player_first_name_modification()
            self.ask_change_value(player_number=player_number, key='first_name', value=prenom)
        elif resultat_modif == 3:
            self.change_age_player(player_number=player_number)
        elif resultat_modif == 4:
            sex = self.player_sex_modification()
            self.ask_change_value(player_number=player_number, key='sex', value=sex)
        elif resultat_modif == 5:
            self.change_classement_player(player_number=player_number)
        else:
            self.print_error_enter_int()
            self.sub_menu_player_2()

    # -----------------------------------------------------------------------------------------------------------------#

    def change_age_player(self, player_number):
        try:
            age = int(self.player_age_modification())
            if age <= 0 or age > 120:
                self.print_error_enter_int_age()
                age = self.change_age_player(player_number=player_number)
            self.ask_change_value(player_number=player_number, key='age', value=age)
        except:
            self.print_error_enter_int_age()
            age = self.change_age_player(player_number=player_number)
        return age

    # -----------------------------------------------------------------------------------------------------------------#

    def change_classement_player(self, player_number):
        try:
            classement = int(self.player_classement_modification())
            if classement <= 0:
                self.print_error_enter_int_age()
                classement = self.change_classement_player(player_number=player_number)
            self.ask_change_value(player_number=player_number, key='classement', value=classement)
        except:
            self.print_error_enter_int_classement()
            classement = self.change_classement_player(player_number=player_number)
        return classement

    # -----------------------------------------------------------------------------------------------------------------#

    def delete_player(self):
        players = self.search_player()
        self.search_player_view(players=players)
        try:
            player_number = int(self.player_to_delete())-1
            self.ask_delete_player(player_number=player_number)
            self.player_modification_save()
        except:
            self.print_error_enter_int()
            self.delete_player()

    # ---------------------------------------------------------------------------------------------------------------------#

    def select_player(self, players):
        try:
            print('les  joueurs a selectionner sont: ')
            i = 1
            for player in players:
                print(i, ':', player)
                i += 1
            player_number = int(self.player_to_select())-1
            selected_player = players[player_number]

        except:
            self.print_error_enter_int()
            selected_player = self.select_player(players=players)

        return selected_player

    # ---------------------------------------------------------------------------------------------------------------------#

    def select_and_add_players(self):
        players = self.search_player()

        if len(players) == 0:
            self.no_player()
        selected_players = list()

        # construire une liste avec les nom dee tous les joueurs
        first_list = list()
        for player in players:
            first_list.append(player['familly_name'])

        # selectionne la list des joeurs qui vont jouer la partie
        while len(selected_players) < settings.nbr_player_max:

            if len(players) < settings.nbr_player_max:
                self.search_player_view(players=players)
                self.need_add_players()
                serialized_player = self.adding_player()
                self.save_player(serialized_player)
                players = self.search_player()
                for player in players:
                    selected_players.append(player['familly_name'])
            elif len(players) > settings.nbr_player_max:
                selected_player = self.select_player(players=first_list)
                selected_players.append(selected_player)
                del first_list[first_list.index(selected_player)]

            else:
                self.search_player_view(players=players)
                players = self.search_player()
                selected_players = first_list
                self.message_selection_complete()

        return selected_players

# ---------------------------------------------------------------------------------------------------------------------#
