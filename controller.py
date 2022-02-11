from player.model import Player, Player_Stat
from view.view_player import Player_view
from tournament.model import Tournament
from view.view_tournament import Tournament_view
from view.principal_view import Choice
import settings
# ---------------------------------------------------------------------------------------------------------------------#


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


class TournamentMenu(Tournament, Tournament_view):

    def sub_menu_tournament_1(self):

        resultat = 0
        try:
            resultat = int(self.tournament_sub_main_choice())
        except:
            self.print_error_enter_int()
            self.sub_menu_tournament_1()

        # Ajouter un tournament.
        if resultat == 1:
            serialized_tournament = self.adding_tournament()
            self.save_tournament(serialized_tournament=serialized_tournament)

        # modifier un tournament.
        elif resultat == 2:
            self.sub_menu_tournament_2()
        # Supprimmer un tournament.
        elif resultat == 3:
            self.delete_tournament()

        # Affichage des tournaments.
        elif int(resultat) == 4:
            tournaments = self.search_tournament()

            self.search_tournament_view(tournaments=tournaments)
            if len(tournaments) == 0:
                self.no_tournament()
        # Supprimmer tous les tournaments.
        elif int(resultat) == 5:
            self.delete_all_tournament()

        # Retour au menu principal
        elif resultat == 6:
            self.message_retour()
            return

        # sortir du logiciel
        elif resultat == 7:
            self.message_visit()
            exit()

        else:
            self.print_error_enter_int()
        self.sub_menu_tournament_1()

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_tournament_2(self):
        tournament_number = 0
        resultat_modif = 0
        try:
            tournaments = self.search_tournament()
            if len(tournaments) == 0:
                self.no_tournament()
                self.sub_menu_tournament_1()
            elif len(tournaments) == 1:
                tournament_number = 0
            else:
                tournament_number = int(self.tournament_modification()) - 1

            resultat_modif = int(self.tournament_modification_spec())
        except:
            self.print_error_enter_int()
            self.sub_menu_tournament_2()

        if resultat_modif == 1:
            name = self.tournament_name_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='nom', value=name)
            self.tournament_modification_save()
        elif resultat_modif == 2:
            lieu = self.tournament_lieu_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='lieu', value=lieu)
        elif resultat_modif == 3:
            date = self.tournament_date_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='date', value=date)
        elif resultat_modif == 4:
            tour = self.tournament_tour_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='tour', value=tour)
        elif resultat_modif == 5:
            Tournees = self.tournament_Tournees_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='Tournees', value=Tournees)
        elif resultat_modif == 6:
            Joueurs = self.tournament_Joueurs_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='Joueurs', value=Joueurs)
        elif resultat_modif == 7:
            controle_temps = self.tournament_controle_temps_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='controle_temps', value=controle_temps)
        elif resultat_modif == 8:
            controle_temps = self.tournament_Description_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='controle_temps', value=controle_temps)
        else:
            self.print_error_enter_int()
            self.sub_menu_tournament_2()
    # -----------------------------------------------------------------------------------------------------------------#

    def delete_tournament(self):
        tournaments = self.search_tournament()
        self.search_tournament_view(tournaments=tournaments)
        tournament_number = 0
        if len(tournaments) == 0:
            self.no_tournament()
        elif len(tournaments) == 1:
                tournament_number = 0
        else:
            try:
                tournament_number = int(self.tournament_to_delete())-1
            except:
                self.print_error_enter_int()
                self.delete_tournament()
            self.ask_delete_tournament(tournament_number=tournament_number)
            self.tournament_modification_save()

# ---------------------------------------------------------------------------------------------------------------------#


class MainMenu(Choice, TournamentMenu, PlayerMenu):

    def menu(self):
        resultat = 0
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
