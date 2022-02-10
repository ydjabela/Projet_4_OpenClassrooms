from player.model import Player, Player_Stat
from view.view_player import Player_view
from tournament.model import Tournament
from view.view_tournament import Sub_Choice_Tournament, Tournament_view, Error_enter_Tournament, Msg_Tournament
from view.principal_view import Choice

# ---------------------------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------------------------#


class PlayerMenu(Player, Player_view, Player_Stat):

    def sub_menu_player_1(self):

        try:
            resultat = int(self.sub_main_choice())
        except:
            self.print_error_enter_int()
            self.sub_menu_player_1()

        # Ajouter un joueur.
        if resultat == 1:
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
            self.ask_change_value(player_number=player_number, key='age', value=age)
        except:
            self.print_error_enter_int_age()
            self.change_age_player(player_number=player_number)

    # -----------------------------------------------------------------------------------------------------------------#

    def change_classement_player(self, player_number):
        try:
            classement = int(self.player_classement_modification())
            self.ask_change_value(player_number=player_number, key='classement', value=classement)
        except:
            self.print_error_enter_int_classement()
            self.change_classement_player(player_number=player_number)

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
# ---------------------------------------------------------------------------------------------------------------------#


class TournamentMenu:

    def sub_menu_tournament_1(self):
        error_enter =Error_enter_Tournament()
        sub_choice = Sub_Choice_Tournament()
        tournament = Tournament()
        tournament_view = Tournament_view()
        msg = Msg_Tournament()

        try:
            resultat = int(sub_choice.sub_main_choice())
        except:
            error_enter.print_error_enter_int()
            self.sub_menu_tournament_1()

        # Ajouter un tournament.
        if resultat == 1:
            serialized_tournament = tournament_view.adding_tournament()
            tournament.save_tournament(serialized_tournament)

        # modifier un tournament.
        elif resultat == 2:
            self.sub_menu_tournament_2()
        # Supprimmer un tournament.
        elif resultat == 3:
            self.delete_tournament()

        # Affichage des tournaments.
        elif int(resultat) == 4:
            tournaments = tournament.search_tournament()
            if len(tournaments) == 0:
                tournament_view.no_tournament()
        elif int(resultat) == 5:
            tournament_tri_ranking, tournament_tri_alphabet = tournament.stat_classement()
        # Supprimmer tous les tournaments.
        elif int(resultat) == 6:
            tournament.delete_all_tournament()

        # Retour au menu principal
        elif resultat == 7:
            msg.message_retour()
            return

        # sortir du logiciel
        elif resultat == 8:
            msg.message_visit()
            exit()

        else:
            error_enter.print_error_enter_int()
        self.sub_menu_tournament_1()

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_tournament_2(self):
        error_enter = Error_enter_Tournament()
        sub_choice = Sub_Choice_Tournament()
        tournament = Tournament()
        tournament_view = Tournament_view()

        try:
            tournaments = tournament.search_tournament()
            if len(tournaments) == 0:
                tournament_view.no_tournament()
                self.sub_menu_tournament_1()
            elif len(tournaments) == 1:
                tournament_number = 0
            else:
                tournament_number = int(tournament_view.tournament_modification()) - 1

            resultat_modif = int(sub_choice.tournament_modification_spec())
        except:
            error_enter.print_error_enter_int()
            self.sub_menu_tournament_2()

        if resultat_modif == 1:
            name = tournament_view.tournament_name_modification()
            tournament.ask_change_name(name=name, tournament_number=tournament_number)
            tournament_view.tournament_modification_save()
        elif resultat_modif == 2:
            lieu = tournament_view.tournament_lieu_modification()
            tournament.ask_change_lieu(lieu=lieu, tournament_number=tournament_number)
        elif resultat_modif == 3:
            date = tournament_view.tournament_date_modification()
            tournament.ask_change_date(date=date, tournament_number=tournament_number)
        elif resultat_modif == 4:
            tour = tournament_view.tournament_tour_modification()
            tournament.ask_change_tour(tour=tour, tournament_number=tournament_number)
        elif resultat_modif == 5:
            Tournees = tournament_view.tournament_Tournees_modification()
            tournament.ask_change_Tournees(Tournees=Tournees, tournament_number=tournament_number)
        elif resultat_modif == 6:
            Joueurs = tournament_view.tournament_Joueurs_modification()
            tournament.ask_change_Joueurs(Joueurs=Joueurs, tournament_number=tournament_number)
        elif resultat_modif == 7:
            controle_temps = tournament_view.tournament_controle_temps_modification()
            tournament.ask_change_controle_temps(controle_temps=controle_temps, tournament_number=tournament_number)
        elif resultat_modif == 8:
            Description = tournament_view.tournament_Description_modification()
            tournament.ask_change_Description(Description=Description, tournament_number=tournament_number)
        else:
            error_enter.print_error_enter_int()
            self.sub_menu_tournament_2()
    # -----------------------------------------------------------------------------------------------------------------#

    def delete_tournament(self):
        tournament_view = Tournament_view()
        tournament = Tournament()
        tournaments = tournament.search_tournament()
        error_enter = Error_enter_Tournament()
        try:
            tournament_number = int(tournament_view.tournament_to_delete())-1
            tournament.ask_delete_tournament(tournament_number=tournament_number)
            tournament_view.tournament_modification_save()
        except:
            error_enter.print_error_enter_int()
            self.delete_tournament()

# ---------------------------------------------------------------------------------------------------------------------#


class MainMenu(Choice, TournamentMenu, PlayerMenu):

    def menu(self):

        try:
            resultat = int(self.main_choice())
        except:
            self.print_error_enter_int()
            self.menu()

        if resultat == 1:
            self.sub_menu_player_1()

        elif resultat == 2:
            self.sub_menu_tournament_1()

        elif resultat == 5:
            self.message_visit()
            exit()

        else:
            self.print_error_enter_int()
        self.menu()

# ---------------------------------------------------------------------------------------------------------------------#
