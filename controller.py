from player.model import Player
from player.view import Sub_Choice_Player, Player_view, Error_enter_Player
from tournament.model import Tournament
from tournament.view import Sub_Choice_Tournament, Tournament_view, Error_enter_Tournament
from view import Choice

# ---------------------------------------------------------------------------------------------------------------------#


class MainMenu:

    def menu(self):
        choice = Choice()
        tournament = TournamentMenu()
        player_menu = PlayerMenu()

        try:
            resultat = int(choice.main_choice())
        except:
            choice.print_error_enter_int()
            self.menu()

        if resultat == 1:
            player_menu.sub_menu()

        elif resultat == 2:
            tournament.sub_menu()

        elif resultat == 5:
            print('Merci pour  votre visite')
            exit()

        else:
            choice.print_error_enter_int()
        print('-------------------------------------------------------------------------------------------------------')
        self.menu()

# ---------------------------------------------------------------------------------------------------------------------#


class PlayerMenu:

    def sub_menu(self):
        error_enter =Error_enter_Player()
        sub_choice = Sub_Choice_Player()
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
        elif int(resultat) == 5:
            player_tri_ranking, player_tri_alphabet = player.stat_classement()
        # Supprimmer tous les joueurs.
        elif int(resultat) == 6:
            player.delete_all_player()

        # Retour au menu principal
        elif resultat == 7:
            print('Retour au menu principal')
            return

        # sortir du logiciel
        elif resultat == 8:
            print('Merci pour  votre visite')
            exit()

        else:
            error_enter.print_error_enter_int()
        print('-------------------------------------------------------------------------------------------------------')
        self.sub_menu()

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_player(self):
        error_enter = Error_enter_Player()
        sub_choice = Sub_Choice_Player()
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
        else:
            error_enter.print_error_enter_int()
            self.sub_menu_player()

    # -----------------------------------------------------------------------------------------------------------------#

    def change_age_player(self, player_number):
        player = Player()
        player_view = Player_view()
        error_enter = Error_enter_Player()
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
        error_enter = Error_enter_Player()
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
        error_enter = Error_enter_Player()
        try:
            player_number = int(player_view.player_to_delete())-1
            player.ask_delete_player(player_number=player_number)
            player_view.player_modification_save()
        except:
            error_enter.print_error_enter_int()
            self.delete_player()

    # ---------------------------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------------------------#


class TournamentMenu:

    def sub_menu(self):
        error_enter =Error_enter_Tournament()
        sub_choice = Sub_Choice_Tournament()
        tournament = Tournament()
        tournament_view = Tournament_view()

        try:
            resultat = int(sub_choice.sub_main_choice())
        except:
            error_enter.print_error_enter_int()
            self.sub_menu()

        # Ajouter un tournament.
        if resultat == 1:
            serialized_tournament = tournament_view.adding_tournament()
            tournament.save_tournament(serialized_tournament)

        # modifier un tournament.
        elif resultat == 2:
            self.sub_menu_tournament()
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
            print('Retour au menu principal')
            return

        # sortir du logiciel
        elif resultat == 8:
            print('Merci pour  votre visite')
            exit()

        else:
            error_enter.print_error_enter_int()
        print('-------------------------------------------------------------------------------------------------------')
        self.sub_menu()

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_tournament(self):
        error_enter = Error_enter_Tournament()
        sub_choice = Sub_Choice_Tournament()
        tournament = Tournament()
        tournament_view = Tournament_view()

        try:
            tournaments = tournament.search_tournament()
            if len(tournaments) == 0:
                tournament_view.no_tournament()
                self.sub_menu()
            elif len(tournaments) == 1:
                tournament_number = 0
            else:
                tournament_number = int(tournament_view.tournament_modification()) - 1

            resultat_modif = int(sub_choice.tournament_modification_spec())
        except:
            error_enter.print_error_enter_int()
            self.sub_menu_tournament()

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
            self.sub_menu_tournament()
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
