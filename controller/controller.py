from view.principal_view import Choice
from model.model_tournament import Tournament
from view.view_tournament import Tournament_view
from model.model_player import Player, Player_Stat
from view.view_player import Player_view
from model.model_match import Match
import settings
import time
import numpy as np

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

    def select_and_add_players(self):
        players = self.search_player()

        if len(players) == 0:
            self.no_player()
        selected_players = list()

        # construire une liste avec les nom dee tous les joueurs
        first_list = list()
        for player in players:
            first_list.append(player['familly_name'])
        second_list = list()
        for player in players:
            second_list.append(player['familly_name'])

        # selectionne la list des joeurs qui vont jouer la partie
        while len(selected_players) < settings.nbr_player_max:
            if len(players) < settings.nbr_player_max:
                self.search_player_view(players=players)
                self.need_add_players()
                serialized_player = self.adding_player()
                self.save_player(serialized_player)
                players = self.search_player()
                selected_players = [i for i in range(len(players))]

            elif len(players) > settings.nbr_player_max:
                selected_player = self.select_player(players=first_list)
                pos = list(np.where(np.array(second_list) == selected_player)[0])
                selected_players.append(int(pos[0]))
                del first_list[first_list.index(selected_player)]

            else:
                self.search_player_view(players=players)
                players = self.search_player()
                selected_players = [i for i in range(len(players))]
                self.message_selection_complete()
        return selected_players

    # ---------------------------------------------------------------------------------------------------------------------#

    def tri_player_by_rang(self, selected_players):
        players = self.search_player()
        players_tried = self.tri_rank_selected_player(players=players, selected_players=selected_players)
        return players_tried

    # ---------------------------------------------------------------------------------------------------------------------#

    def tri_player_by_points(self, selected_players, dict_points):
        players = self.search_player()
        selected_players_list = list()
        for selected_player in selected_players:
            selected_players_list.append(players[selected_player])
        instance_players = list()
        for i in range(len(selected_players_list)):
            selected_player = selected_players_list[i]
            classement = selected_player["classement"]
            points_joueur = dict_points[i]
            x3 = i, points_joueur, classement
            instance_players.append(x3)
        players_tried_dict = sorted(instance_players, key=lambda t: (t[1], -t[2]), reverse=True)

        return players_tried_dict

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
            self.ask_change_tournament_value(tournament_number=tournament_number, key='Joueurs', value=list(Joueurs))
        elif resultat_modif == 7:
            controle_temps = self.tournament_controle_temps_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='controle_temps',
                                             value=controle_temps)
        elif resultat_modif == 8:
            controle_temps = self.tournament_Description_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='controle_temps',
                                             value=controle_temps)
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
                tournament_number = int(self.tournament_to_delete()) - 1
            except:
                self.print_error_enter_int()
                self.delete_tournament()
        self.ask_delete_tournament(tournament_number=tournament_number)
        self.tournament_modification_save()

    # -----------------------------------------------------------------------------------------------------------------#

    def choose_tournament(self, selected_players):
        tournaments = self.search_tournament()

        tournament_number = 0
        # Si y'a  pas de tournois
        if len(tournaments) == 0:
            self.no_tournament()
            # add tournament if len(tournaments) = 0
            serialized_tournament = self.adding_tournament(without_player=True)
            # Sauvegarder le tournoi
            self.save_tournament(serialized_tournament=serialized_tournament)
            tournaments = self.search_tournament()
            tournament_number = 0
        # Si y'a un seul tournoi
        elif len(tournaments) == 1:
            tournament_number = 0
        # Si y'a un plusieurs tournois
        else:
            try:
                self.search_tournament_view(tournaments=tournaments)
                tournament_number = int(self.tournament_to_play()) - 1
            except:
                self.print_error_enter_int()
                tournament_number, tournaments = self.choose_tournament(selected_players=selected_players)
        self.ask_change_tournament_value(tournament_number=tournament_number, key='Joueurs',
                                         value=list(selected_players))
        tournaments = self.search_tournament()
        self.tournament_chosed_view(tournament_number=tournament_number, tournaments=tournaments)

        return tournament_number, tournaments

# ---------------------------------------------------------------------------------------------------------------------#


class Match_Menu(TournamentMenu, PlayerMenu, Match):

    # -----------------------------------------------------------------------------------------------------------------#

    def rounds_matchs(self, Round, matchs_already_played, instance_players_tried):

        # jumelé Le meilleur joueur de avec le deuxieme meilleur joueur
        tour_list = [Round]
        for k in range(1, settings.TURNS + 1):
            ref_joueur_1 = instance_players_tried[0]
            ref_joueur_2 = self.matchs_already_played_function(
                ref_joueur_1=ref_joueur_1,
                matchs_already_played=matchs_already_played,
                instance_players_tried=instance_players_tried
            )
            match_to_play1 = (ref_joueur_1, ref_joueur_2)
            match_to_play2 = (ref_joueur_2, ref_joueur_1)

            matchs_already_played.append(match_to_play1)
            matchs_already_played.append(match_to_play2)
            del instance_players_tried[instance_players_tried.index(ref_joueur_1)]
            del instance_players_tried[instance_players_tried.index(ref_joueur_2)]

            # Un tirage au sort des joueurs définira qui joue en blanc et qui joue en noir ;
            color_joueur_1, color_joueur_2 = self.player_color()

            match_player = self.match(
                ref_joueur_1=ref_joueur_1,
                ref_joueur_2=ref_joueur_2,
                color_joueur_1=color_joueur_1,
                color_joueur_2=color_joueur_2
            )
            self.match_view(
                joueur_1=ref_joueur_1,
                joueur_2=ref_joueur_2,
                match_number=k + 1,
                color_joueur_1=color_joueur_1,
                color_joueur_2=color_joueur_1
            )
            tour_list.append(match_player)
        return tour_list, matchs_already_played

    # -----------------------------------------------------------------------------------------------------------------#

    def start_playing_tournament(self, selected_players):

        # selectionner un tournoi à jouer
        tournament_number, tournaments = self.choose_tournament(selected_players=selected_players)
        matchs_round = list()
        dict_points = dict()
        matchs_already_played = list()
        for selected_player in selected_players:
            dict_points[selected_player] = 0

        for round in range(1, settings.TURNS + 1):

            # 1 er tour
            Round = 'Round {}'.format(round)
            self.round_view(Round=Round)

            if round == 1:
                # trier les selected_players  par classement
                players_tried = self.tri_player_by_rang(selected_players=selected_players)
                self.search_player_view(players=players_tried)
                instance_players_tried = [i for i in range(len(players_tried))]
                # divisez les joueurs classés en deux moitiés
                player_list_sup = list()
                player_list_inf = list()
                length = len(instance_players_tried)
                div_length = int(length / 2)
                for i in range(0, div_length):
                    player_list_sup.append(instance_players_tried[i])
                for j in range(div_length, length):
                    player_list_inf.append(instance_players_tried[j])

                # jumelé Le meilleur joueur de la moitié supérieure avec le meilleur joueur de la moitié inférieure
                # Définir les paires de joueurs
                tour_list = [Round]
                for k in range(0, div_length):
                    ref_joueur_1 = player_list_sup[k]
                    ref_joueur_2 = player_list_inf[k]
                    match_to_play_1 = ref_joueur_1, ref_joueur_2
                    match_to_play_2 = ref_joueur_2, ref_joueur_1
                    matchs_already_played.append(match_to_play_1)
                    matchs_already_played.append(match_to_play_2)
                    # Un tirage au sort des joueurs définira qui joue en blanc et qui joue en noir ;
                    color_joueur_1, color_joueur_2 = self.player_color()

                    match_player = self.match(
                        ref_joueur_1=ref_joueur_1,
                        ref_joueur_2=ref_joueur_2,
                        color_joueur_1=color_joueur_1,
                        color_joueur_2=color_joueur_2
                    )
                    self.match_view(
                        joueur_1=ref_joueur_1,
                        joueur_2=ref_joueur_2,
                        match_number=k + 1,
                        color_joueur_1=color_joueur_1,
                        color_joueur_2=color_joueur_1,
                    )
                    tour_list.append(match_player)
            else:
                # trier par le nombre de points gagner
                # triez tous les joueurs en fonction de leur nombre total de points.
                # et si ils ont les meme points les classé par ordre de classment
                instance_players_tried = list()
                players_tried = self.tri_player_by_points(selected_players=selected_players, dict_points=dict_points)
                self.search_player_view_classement(players=players_tried)
                for i in range(len(players_tried)):
                    ref_joueur, points, classement = players_tried[i]
                    instance_players_tried.append(ref_joueur)
                tour_list, matchs_already_played = self.rounds_matchs(
                    Round=Round,
                    matchs_already_played=matchs_already_played,
                    instance_players_tried=instance_players_tried
                )
            matchs = self.sub_menu_start_end_round(tour_list=tour_list)
            for i in range(1, len(matchs)):
                match_players = matchs[i]
                ref_joueur_1, score_joueur_1, color_joueur_1 = match_players[0]
                ref_joueur_2, score_joueur_2, color_joueur_2 = match_players[1]
                start_match_time = match_players[2]
                end_match_time = match_players[3]
                match = self.match(
                    ref_joueur_1=ref_joueur_1,
                    ref_joueur_2=ref_joueur_2,
                    score_joueur_1=score_joueur_1,
                    score_joueur_2=score_joueur_2,
                    color_joueur_1=color_joueur_1,
                    color_joueur_2=color_joueur_2,
                    start_match_time=start_match_time,
                    end_match_time=end_match_time
                )
                self.match_view(
                    joueur_1=ref_joueur_1,
                    joueur_2=ref_joueur_2,
                    match_number=i,
                    score_joueur_1=score_joueur_1,
                    score_joueur_2=score_joueur_2,
                    color_joueur_1=color_joueur_1,
                    color_joueur_2=color_joueur_1,
                    start_match_time=start_match_time,
                    end_match_time=end_match_time
                )
                dict_points[ref_joueur_1] += score_joueur_1
                dict_points[ref_joueur_2] += score_joueur_2
                matchs_round.append(match)

        # Sauvegarder les résultats pour chaque paire
        self.ask_change_tournament_value(tournament_number=tournament_number, key='Tournees', value=matchs_round)

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_start_end_round(self, tour_list):
        match_alerady_started_1 = False
        match_alerady_started_2 = False
        match_alerady_started_3 = False
        match_alerady_started_4 = False
        match_finished_1 = match_finished_2 = match_finished_3 = match_finished_4 = False
        Round = tour_list[0]
        match_1 = tour_list[1]
        match_2 = tour_list[2]
        match_3 = tour_list[3]
        match_4 = tour_list[4]
        resultat_enter = 0
        match = [Round]

        while True:
            try:
                if match_finished_1 and match_finished_2 and match_finished_3 and match_finished_4 == True:
                    match.append(match_1)
                    match.append(match_2)
                    match.append(match_3)
                    match.append(match_4)
                    return match
                    break

                resultat_enter = self.start_end_match_view(
                    match_finished_1=match_finished_1,
                    match_finished_2=match_finished_2,
                    match_finished_3=match_finished_3,
                    match_finished_4=match_finished_4,
                    match_alerady_started_1=match_alerady_started_1,
                    match_alerady_started_2=match_alerady_started_2,
                    match_alerady_started_3=match_alerady_started_3,
                    match_alerady_started_4=match_alerady_started_4
                )

            except:
                self.print_error_enter_int()
                match = self.sub_menu_start_end_round(tour_list)

            if resultat_enter == 1:
                match_1, match_alerady_started_1, match_finished_1 = self.start_end_match(
                    match=match_1,
                    match_finished=match_finished_1,
                    match_alerady_started=match_alerady_started_1
                )
            elif resultat_enter == 2:
                match_2, match_alerady_started_2, match_finished_2 = self.start_end_match(
                    match=match_2,
                    match_finished=match_finished_2,
                    match_alerady_started=match_alerady_started_2
                )
            elif resultat_enter == 3:
                match_3, match_alerady_started_3, match_finished_3 = self.start_end_match(
                    match=match_3,
                    match_finished=match_finished_3,
                    match_alerady_started=match_alerady_started_3
                )
            elif resultat_enter == 4:
                match_4, match_alerady_started_4, match_finished_4 = self.start_end_match(
                    match=match_4,
                    match_finished=match_finished_4,
                    match_alerady_started=match_alerady_started_4
                )
            else:
                self.print_error_enter_int()
                match = self.sub_menu_start_end_round(tour_list)

    # -----------------------------------------------------------------------------------------------------------------#

    def start_end_match(
            self,
            match,
            match_finished,
            match_alerady_started
    ):
        ref_joueur_1, score_joueur_1, color_joueur_1 = match[0]
        ref_joueur_2, score_joueur_2, color_joueur_2 = match[1]
        start_match_time = match[2]
        end_match_time = match[3]
        if not match_finished:
            if not match_alerady_started:
                match_alerady_started = True
                start_match_time = time.time()
            else:
                end_match_time = time.time()
                score_joueur_1 = self.enter_resultat_player(ref_joueur=ref_joueur_1)
                score_joueur_2 = 1 - score_joueur_1
                match_finished = True

        else:
            self.match_finished()

        match = self.match(
            ref_joueur_1=ref_joueur_1,
            ref_joueur_2=ref_joueur_2,
            score_joueur_1=score_joueur_1,
            score_joueur_2=score_joueur_2,
            color_joueur_1=color_joueur_1,
            color_joueur_2=color_joueur_2,
            start_match_time=start_match_time,
            end_match_time=end_match_time
        )
        self.match_view(
            joueur_1=ref_joueur_1,
            joueur_2=ref_joueur_2,
            match_number=1,
            score_joueur_1=score_joueur_1,
            score_joueur_2=score_joueur_2,
            color_joueur_1=color_joueur_1,
            color_joueur_2=color_joueur_1,
            start_match_time=start_match_time,
            end_match_time=end_match_time
        )

        return match, match_alerady_started, match_finished

    # -----------------------------------------------------------------------------------------------------------------#


class MainMenu(Choice, Match_Menu):

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

        elif resultat == 3:
            selected_players = self.select_and_add_players()
            self.start_playing_tournament(selected_players=selected_players)
        elif resultat == 5:
            self.message_visit()
            exit()

        else:
            self.print_error_enter_int()
        self.menu()

#   -------------------------------------------------------------------------------------------------------------------#


