from model.model_tournament import Tournament
from view.view_tournament import Tournament_view

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
            return
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

    # -----------------------------------------------------------------------------------------------------------------#

    def start_playing_tournament(self, players):

        tournaments = self.search_tournament()

        tournament_number = 0
        if len(tournaments) == 0:
            self.no_tournament()
            # add tournament if len(tournaments) = 0
            serialized_tournament = self.adding_tournament()
            self.save_tournament(serialized_tournament=serialized_tournament)
            tournament_number = 0
        elif len(tournaments) == 1:
                tournament_number = 0
        else:
            try:
                self.search_tournament_view(tournaments=tournaments)
                tournament_number = int(self.tournament_to_play())-1
            except:
                self.print_error_enter_int()
                self.start_playing_tournament()
        self.tournament_chosed_view(tournament_number=tournament_number, tournaments=tournaments)
        value = list()
        for player in players:
            value.append(player['familly_name'])
        self.ask_change_tournament_value(tournament_number=tournament_number, key='Joueurs', value=str(value))

        return tournament_number, tournaments
