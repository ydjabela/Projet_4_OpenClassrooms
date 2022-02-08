from tournament.model import Tournament
from tournament.view import Sub_Choice, Tournament_view, Error_enter

# ---------------------------------------------------------------------------------------------------------------------#


class TournamentMenu:

    def sub_menu(self):
        error_enter =Error_enter()
        sub_choice = Sub_Choice()
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
        error_enter = Error_enter()
        sub_choice = Sub_Choice()
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
        error_enter = Error_enter()
        try:
            tournament_number = int(tournament_view.tournament_to_delete())-1
            tournament.ask_delete_tournament(tournament_number=tournament_number)
            tournament_view.tournament_modification_save()
        except:
            error_enter.print_error_enter_int()
            self.delete_tournament()

# ---------------------------------------------------------------------------------------------------------------------#
