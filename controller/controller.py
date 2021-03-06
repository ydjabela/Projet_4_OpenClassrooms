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
        # reactualiser les joueurs
        players = self.search_player()
        # Demander et affichage du menu gestion des joueurs
        resultat = self.player_sub_main_choice()
        # Ajouter un joueur.
        if resultat == 1:
            familly_name, first_name, age, sex, classement = self.adding_player(players=players)
            # sauvegarde du joueur ajouter
            player = Player(
                familly_name=familly_name,
                first_name=first_name,
                age=age,
                sex=sex,
                classement=classement
            )
            # modification terminer
            player.save_player()
        # modifier un joueur.
        elif resultat == 2:
            # menu modification des joueurs
            self.sub_menu_player_2()
        # Supprimer un joueur.
        elif resultat == 3:
            # menu supprimer un joueur
            self.delete_player()
        # Affichage des joueurs.
        elif resultat == 4:
            # voir les joueurs existent
            players = self.search_player()
            # Affichage des joueurs existant
            self.search_player_view(players=players)
            # si aucun joueur n'existe
            if len(players) == 0:
                self.no_player()
        # classement des joueurs
        elif resultat == 5:
            # triage des joueurs par ordre de classement et par ordre alphabétique
            player_tri_ranking, player_tri_alphabet = self.stat_classement()
            # Affichage des statistiques
            self.view_statique_player(
                player_tri_ranking=player_tri_ranking,
                player_tri_alphabet=player_tri_alphabet
            )
        # Supprimmer tous les joueurs.
        elif resultat == 6:
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
        player_number = 0
        # voir les joueurs existent dans la base de donnée
        players = self.search_player()
        # affichage des joueurs
        self.search_player_view(players=players)
        # si aucun joueur n'existe
        if len(players) == 0:
            self.no_player()
            self.sub_menu_player_1()
        # s'il existe un seul joueur
        elif len(players) == 1:
            player_number = 0
        # Si y a plusieurs joueurs
        else:
            # Demander le numéro de joueur à modifier
            player_number = self.player_modification(players=players)
        # Demander quels parametre de joueur qu'il faut modifier
        resultat_modif = self.player_modification_spec()
        # Modifier le nom
        if resultat_modif == 1:
            name = self.player_name_modification()
            self.ask_change_value(
                player_number=player_number,
                key='familly_name',
                value=name
            )
            self.player_modification_save()
        # Modifier le prenom
        elif resultat_modif == 2:
            prenom = self.player_first_name_modification()
            self.ask_change_value(
                player_number=player_number,
                key='first_name',
                value=prenom
            )
        # modifier l'age
        elif resultat_modif == 3:
            self.change_age_player(player_number=player_number)
        # modifier le sex
        elif resultat_modif == 4:
            sex = self.player_sex_modification()
            self.ask_change_value(
                player_number=player_number,
                key='sex',
                value=sex
            )
        # modifier le classement
        elif resultat_modif == 5:
            self.change_classement_player(player_number=player_number)
        # Index error
        else:
            self.print_error_enter_int()
            self.sub_menu_player_2()

    # -----------------------------------------------------------------------------------------------------------------#

    def change_age_player(self, player_number):
        try:
            # Demander de changer l'age
            age = int(self.player_age_modification())
            # en cas l'age n'est pas inclu dans l'interval
            if age <= 0 or age > 120:
                self.print_error_enter_int_age()
                age = self.change_age_player(player_number=player_number)
            # save age
            self.ask_change_value(
                player_number=player_number,
                key='age',
                value=age
            )
        except (ValueError, IndexError):
            self.print_error_enter_int_age()
            age = self.change_age_player(player_number=player_number)
        return age

    # -----------------------------------------------------------------------------------------------------------------#

    def change_classement_player(self, player_number):
        try:
            # Demander de changer le classement
            classement = int(self.player_classement_modification())
            # en cas  le classment est  inferior ou egal a zero
            if classement <= 0:
                self.print_error_enter_int_age()
                classement = self.change_classement_player(
                    player_number=player_number
                )
            # save classement
            self.ask_change_value(
                player_number=player_number,
                key='classement',
                value=classement
            )
        except (ValueError, IndexError):
            self.print_error_enter_int_classement()
            classement = self.change_classement_player(
                player_number=player_number
            )
        return classement

    # -----------------------------------------------------------------------------------------------------------------#

    def delete_player(self):
        # voir les joueurs
        players = self.search_player()
        # Affichage
        self.search_player_view(players=players)
        try:
            # Demander le numéro de joueur à suprimmer
            player_number = int(self.player_to_delete())
            # Suprimer  le joueur
            self.ask_delete_player(player_number=player_number)
            # affichage de  fin de  modification
            self.player_modification_save()
        except (ValueError, IndexError):
            self.print_error_enter_int()
            self.delete_player()

    # ---------------------------------------------------------------------------------------------------------------------#

    def select_and_add_players(self):
        # init
        selected_players = list()
        first_list = list()
        # Chercher les joueurs existent
        players = self.search_player()
        # Si aucun joueur n'existe'
        if len(players) == 0:
            self.no_player()
        # construire une liste avec les noms de tous les joueurs
        for player in players:
            first_list.append(player['familly_name'])
        second_list = first_list.copy()
        # Selectionner la list des joueurs qui vont jouer la partie
        while len(selected_players) < settings.nbr_player_max:
            # S'il manque des joueurs
            if len(players) < settings.nbr_player_max:
                # Voir les joueurs existent
                self.search_player_view(players=players)
                #  Affichage de message qu'il faut ajouter des joueurs
                self.need_add_players()
                # Ajouter un joueur
                familly_name, first_name, age, sex, classement = self.adding_player(players=players)
                # créer un object player
                player = Player(
                    familly_name=familly_name, first_name=first_name, age=age, sex=sex, classement=classement
                )
                # sauvegarder le joueur
                player.save_player()
                # reactualiser les joueurs
                players = self.search_player()
                # actualiser la selection des joueurs
                selected_players = [i for i in range(len(players))]
            # S'il existe plus de joueur qu'on a besoin
            elif len(players) > settings.nbr_player_max:
                # Selectionner et afficher les joueurs a selectionner de la premiere liste
                selected_player = self.select_player(players=first_list)
                # Voir la position du joueur seléctionner dans la seconde liste
                pos = list(np.where(np.array(second_list) == selected_player)[0])
                # Ajouter la premiere position de joueur selectionné
                selected_players.append(int(pos[0]))
                # Supprimer le joueur deja selectionner de la premiere liste
                first_list.remove(selected_player)
            # S'il existe le nombre exact des joueurs qu'il faut
            else:
                # Affichage des joueurs existent
                self.search_player_view(players=players)
                # Actualiser la liste des joueurs
                players = self.search_player()
                # Selectionné la reference des joueurs
                selected_players = [i for i in range(len(players))]
                # Affichage d'un message que la selection est complete
                self.message_selection_complete()
        return selected_players

    # ---------------------------------------------------------------------------------------------------------------------#

    def tri_player_by_rang(self, selected_players):
        # init
        instance_players = list()
        # Voir les joueurs existent
        players = self.search_player()
        # Créer une  nouvelle  liste avec la selection des  joueurs et le classement
        for ref_player in selected_players:
            selected_player = players[ref_player]
            classement = selected_player["classement"]
            x2 = ref_player, classement
            instance_players.append(x2)
        # trier la  liste des  joueurs par classement
        players_tried = sorted(
            instance_players,
            key=lambda t: (t[1]),
            reverse=False)
        return players_tried

    # ---------------------------------------------------------------------------------------------------------------------#

    def tri_player_by_points(self, selected_players, dict_points):
        # init
        instance_players = list()
        # Voir les joueurs existent
        players = self.search_player()
        # Créer une  nouvelle  liste avec la selection des  joueurs, par  points et le classement
        for ref_player in selected_players:
            selected_player = players[ref_player]
            classement = selected_player["classement"]
            points_joueur = dict_points[ref_player]
            x3 = ref_player, points_joueur, classement
            instance_players.append(x3)
        # trier la  liste des  joueurs par ponits  puis par classement
        players_tried_dict = sorted(
            instance_players,
            key=lambda t: (t[1], -t[2]),
            reverse=True)
        return players_tried_dict

# ---------------------------------------------------------------------------------------------------------------------#


class TournamentMenu(Tournament, Tournament_view):

    def sub_menu_tournament_1(self):
        #  Menu tournois
        resultat = self.tournament_sub_main_choice()
        # Ajouter un tournament.
        if resultat == 1:
            nom, lieu, date, tour, tournees, joueurs, controle_temps, description = self.adding_tournament()
            tournament = Tournament(
                nom=nom,
                lieu=lieu,
                date=date,
                tour=tour,
                Tournees=tournees,
                Joueurs=joueurs,
                controle_temps=controle_temps,
                Description=description
            )
            # SAuvegarder un Tournoi
            tournament.save_tournament()
        # modifier un tournament.
        elif resultat == 2:
            self.sub_menu_tournament_2()
        # Supprimmer un tournament.
        elif resultat == 3:
            self.delete_tournament()
        # Affichage des tournaments.
        elif resultat == 4:
            tournaments = self.search_tournament()
            self.search_tournament_view(tournaments=tournaments)
            if len(tournaments) == 0:
                self.no_tournament()
        # Supprimmer tous les tournaments.
        elif resultat == 5:
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
        # Init
        tournament_number = 0
        #  menu modification d'un tournoi
        # voir le nombre de tournois
        tournaments = self.search_tournament()
        self.search_tournament_view(tournaments=tournaments)
        if len(tournaments) == 0:
            self.no_tournament()
            self.sub_menu_tournament_1()
        elif len(tournaments) == 1:
            tournament_number = 0
        else:
            tournament_number = self.tournament_modification(tournaments=tournaments)
        resultat_modif = self.tournament_modification_spec()

        # modifier  le  nom
        if resultat_modif == 1:
            name = self.tournament_name_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='nom', value=name)
            self.tournament_modification_save()
        # modifier le lieu
        elif resultat_modif == 2:
            lieu = self.tournament_lieu_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='lieu', value=lieu)
        # modifier la date
        elif resultat_modif == 3:
            date = self.tournament_date_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='date', value=date)
        # modifier nombre de tour
        elif resultat_modif == 4:
            tour = self.tournament_tour_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='tour', value=tour)
        # modifier la tournee
        elif resultat_modif == 5:
            self.tournament_tournees_modification()
        # modifier les joueurs
        elif resultat_modif == 6:
            joueurs = self.tournament_Joueurs_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='Joueurs', value=list(joueurs))
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
        # Init
        # voir les tournois existent
        tournaments = self.search_tournament()
        self.search_tournament_view(tournaments=tournaments)
        if len(tournaments) == 0:
            self.no_tournament()
            return
        elif len(tournaments) == 1:
            tournament_number = 0
        else:
            # Selectionner  le tournoi a supprimer
            tournament_number = self.tournament_to_delete(tournaments=tournaments)

        # Supprimer le joueur selctionner
        self.ask_delete_tournament(tournament_number=tournament_number)
        self.tournament_modification_save()

    # -----------------------------------------------------------------------------------------------------------------#

    def choose_tournament(self):
        tournaments = self.search_tournament()
        tournament_number = 0
        # Si y'a  pas de tournois
        if len(tournaments) == 0:
            self.no_tournament()
            # add tournament if len(tournaments) = 0
            nom, lieu, date, tour, tournees, joueurs, controle_temps, description = self.adding_tournament(
                without_player=True
            )
            # creation object tournament
            tournament = Tournament(
                nom=nom,
                lieu=lieu,
                date=date,
                tour=tour,
                Tournees=tournees,
                Joueurs=joueurs,
                controle_temps=controle_temps,
                Description=description
            )
            # Sauvegarder le tournoi
            tournament.save_tournament()
        # Si y a un seul tournoi
        elif len(tournaments) == 1:
            self.one_tournament_existed()
        # Si y a un plusieurs tournois
        else:
            self.search_tournament_view(tournaments=tournaments)
            tournament_number = self.tournament_to_play(tournaments=tournaments)
        tournaments = self.search_tournament()
        self.tournament_chosed_view(tournament_number=tournament_number, tournaments=tournaments)
        return tournament_number, tournaments

# ---------------------------------------------------------------------------------------------------------------------#


class MatchMenu(TournamentMenu, PlayerMenu, Match):

    # -----------------------------------------------------------------------------------------------------------------#

    def rounds_matchs(self, round, matchs_already_played, instance_players_tried):

        # jumelé Le meilleur joueur de avec le deuxieme meilleur joueur
        tour_list = [round]
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

            # instance match
            match_player = self.match(
                ref_joueur_1=ref_joueur_1,
                ref_joueur_2=ref_joueur_2,
                color_joueur_1=color_joueur_1,
                color_joueur_2=color_joueur_2
            )
            self.match_view(
                joueur_1=ref_joueur_1,
                joueur_2=ref_joueur_2,
                match_number=k,
                color_joueur_1=color_joueur_1,
            )
            tour_list.append(match_player)
        return tour_list, matchs_already_played

    # -----------------------------------------------------------------------------------------------------------------#

    def round_1(self, tour_list, selected_players, matchs_already_played):
        # trier les selected_players  par classement
        players_tried = self.tri_player_by_rang(selected_players=selected_players)
        self.search_player_view_classement(players=players_tried)
        instance_players_tried = list()
        for i in range(len(players_tried)):
            ref_joueur, classement = players_tried[i]
            instance_players_tried.append(ref_joueur)
        # divisez les joueurs classés en deux moitiés
        player_list_sup = list()
        player_list_inf = list()
        length = len(players_tried)
        div_length = int(length / 2)
        # liste des joueurs partie supérieure
        for i in range(0, div_length):
            player_list_sup.append(instance_players_tried[i])
        # liste des joueurs partie inférieure
        for j in range(div_length, length):
            player_list_inf.append(instance_players_tried[j])

        # jumelé Le meilleur joueur de la moitié supérieure
        # avec le meilleur joueur de la moitié inférieure
        # Définir les paires de joueurs

        for k in range(0, div_length):
            # joueur de la partie supérieure
            ref_joueur_1 = player_list_sup[k]
            # joueur de la partie inférieure
            ref_joueur_2 = player_list_inf[k]
            # match à jouer
            match_to_play_1 = ref_joueur_1, ref_joueur_2
            match_to_play_2 = ref_joueur_2, ref_joueur_1

            # Enregistre les matchs deja jouer sachant que
            # match_to_play_1 et match_to_play_1 est le meme match
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
            )
            tour_list.append(match_player)
        return tour_list, matchs_already_played

    # -----------------------------------------------------------------------------------------------------------------#

    def match_round_x(self, matchs, dict_points, matchs_round):
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
                start_match_time=start_match_time,
                end_match_time=end_match_time
            )
            dict_points[ref_joueur_1] += score_joueur_1
            dict_points[ref_joueur_2] += score_joueur_2
            matchs_round.append(match)
        return matchs_round, dict_points

    # -----------------------------------------------------------------------------------------------------------------#

    def select_players_for_tournament(self, tournament_number, tournaments):
        tournament = tournaments[tournament_number]
        joueurs = tournament['Joueurs']
        # Si les joueurs ne sont pas deja selectionnés
        if joueurs == '':
            # Choisir la liste des joueurs
            selected_players = self.select_and_add_players()

            # enregistrer la liste des joueurs dans la base de donnée tournois dans la case joueurs
            self.ask_change_tournament_value(
                        tournament_number=tournament_number,
                        key='Joueurs',
                        value=list(selected_players)
                    )
        # Si les joueurs sont deja selectionnés
        else:
            selected_players = joueurs
        return selected_players

    # -----------------------------------------------------------------------------------------------------------------#

    def start_round_x(self, tuple_round_x):
        tournament, matchs_round, matchs_already_played, dict_points, selected_players = tuple_round_x
        # verifier la tournée
        tournes = tournament['Tournees']

        start_round = 1
        # si aucune tournees n'existe
        if tournes == '':
            start_round = 1
        # S'il existe aumoins une tourne voir le nombre de match qui ont ete jouer deja
        else:
            for match in tournes:
                matchs_round.append(match)
                joueur_1, joueur_2, start_match_time, end_match_time = match
                ref_joueur_1, score_joueur_1, color_joueur_1 = joueur_1
                ref_joueur_2, score_joueur_2, color_joueur_2 = joueur_2
                match_to_play_1 = ref_joueur_1, ref_joueur_2
                match_to_play_2 = ref_joueur_2, ref_joueur_1
                matchs_already_played.append(match_to_play_1)
                matchs_already_played.append(match_to_play_2)
                dict_points[ref_joueur_1] += score_joueur_1
                dict_points[ref_joueur_2] += score_joueur_2

            tournee_length = len(tournes)
            if tournee_length == 4:
                start_round = 2
            elif tournee_length == 8:
                start_round = 3
            elif tournee_length == 12:
                start_round = 4
            else:
                # check if  he need to restart or quit
                resultat = self.restart_round_choice()
                if resultat == 1:
                    matchs_round = list()
                    dict_points = dict()
                    for selected_player in selected_players:
                        dict_points[selected_player] = 0
                    matchs_already_played = list()
                    start_round = 1

                elif resultat == 2:
                    self.message_retour()
                    self.menu()
                    return
                else:
                    self.print_error_enter_int()
                    self.start_playing_tournament()
        return tournament, matchs_round, matchs_already_played, dict_points, selected_players, start_round

    # -----------------------------------------------------------------------------------------------------------------#

    def start_playing_tournament(self):
        # Init
        matchs_round = list()
        dict_points = dict()
        matchs_already_played = list()
        # selectionner un tournoi à jouer
        tournament_number, tournaments = self.choose_tournament()
        tournament = tournaments[tournament_number]
        # selectionner les joueurs
        selected_players = self.select_players_for_tournament(tournament_number, tournaments)
        for selected_player in selected_players:
            dict_points[selected_player] = 0
        tuple_round_x = tournament, matchs_round, matchs_already_played, dict_points, selected_players
        tuple_round_x = self.start_round_x(tuple_round_x=tuple_round_x)
        tournament, matchs_round, matchs_already_played, dict_points, selected_players, start_round = tuple_round_x
        # Demarrer  le  round
        for round_x in range(start_round, settings.TURNS + 1):
            # 1 er tour
            self.round_view(round_x='Round {}'.format(round_x))

            if round_x == 1:
                tour_list = [round_x]
                match_player, matchs_already_played = self.round_1(
                    tour_list=tour_list,
                    selected_players=selected_players,
                    matchs_already_played=matchs_already_played
                )
            else:
                # Trier par le nombre de points gagner triez tous les joueurs en fonction de leur nombre total
                # de points. Et s'ils ont les meme points les classés par ordre de classement
                instance_players_tried = list()
                players_tried = self.tri_player_by_points(selected_players=selected_players,
                                                          dict_points=dict_points)
                self.search_player_view_classement(players=players_tried)
                for i in range(len(players_tried)):
                    ref_joueur, points, classement = players_tried[i]
                    instance_players_tried.append(ref_joueur)
                tour_list, matchs_already_played = self.rounds_matchs(
                    round=round_x,
                    matchs_already_played=matchs_already_played,
                    instance_players_tried=instance_players_tried
                )
            matchs = self.sub_menu_start_end_round(tour_list=tour_list)
            matchs_round, dict_points = self.match_round_x(
                matchs=matchs,
                dict_points=dict_points,
                matchs_round=matchs_round
            )
            # Sauvegarder les résultats pour chaque paire de joueur
            self.ask_change_tournament_value(
                tournament_number=tournament_number,
                key='Tournees',
                value=matchs_round
            )
        # triage final
        players_tried = self.tri_player_by_points(selected_players=selected_players, dict_points=dict_points)
        self.search_player_view_classement(players=players_tried)

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_start_end_round(self, tour_list):
        # init
        m_al_sta_1 = False
        m_al_sta_2 = False
        m_al_sta_3 = False
        m_al_sta_4 = False
        m_finished_1 = m_finished_2 = m_finished_3 = m_finished_4 = False
        match = [tour_list[0]]
        match_1 = tour_list[1]
        match_2 = tour_list[2]
        match_3 = tour_list[3]
        match_4 = tour_list[4]
        resultat_enter = 0

        # Demander de demarrer un match  ou de  le finir
        while True:

            if m_finished_1 and m_finished_2 and m_finished_3 and m_finished_4 is True:
                match.extend((match_1, match_2, match_3, match_4))
                return match
                break
            resultat_enter = self.start_end_match_view(
                m_finished_1=m_finished_1, m_finished_2=m_finished_2, m_finished_3=m_finished_3,
                m_finished_4=m_finished_4, m_al_sta_1=m_al_sta_1, m_al_sta_2=m_al_sta_2,
                m_al_sta_3=m_al_sta_3, m_al_sta_4=m_al_sta_4)
            # Demarrer ou finir le match n° 1
            if resultat_enter == 1:
                m_1_tuple = match_1, m_al_sta_1, m_finished_1
                m_1_tuple = self.start_end_match(match_tuple=m_1_tuple)
                match_1, m_al_sta_1, m_finished_1 = m_1_tuple
                # Demmarrer ou finir le match n° 2
            elif resultat_enter == 2:
                m_2_tuple = match_2, m_al_sta_2, m_finished_2
                m_2_tuple = self.start_end_match(match_tuple=m_2_tuple)
                match_2, m_al_sta_2, m_finished_2 = m_2_tuple
            # Demarrer ou finir le match n° 3
            elif resultat_enter == 3:
                m_3_tuple = match_3, m_al_sta_3, m_finished_3
                m_3_tuple = self.start_end_match(match_tuple=m_3_tuple)
                match_3, m_al_sta_3, m_finished_3 = m_3_tuple
            # Demarrer ou finir  le match n° 4
            elif resultat_enter == 4:
                m_4_tuple = match_4, m_al_sta_4, m_finished_4
                m_4_tuple = self.start_end_match(match_tuple=m_4_tuple)
                match_4, m_al_sta_4, m_finished_4 = m_4_tuple
            # Arreter la tournee et le tournoi
            elif resultat_enter == 5:
                self.message_retour()
                self.menu()
                return
            else:
                self.print_error_enter_int()
                match = self.sub_menu_start_end_round(tour_list)

    # -----------------------------------------------------------------------------------------------------------------#

    def start_end_match(self, match_tuple):
        # Init
        match, match_al_sta, match_finished = match_tuple
        ref_joueur_1, score_joueur_1, color_joueur_1 = match[0]
        ref_joueur_2, score_joueur_2, color_joueur_2 = match[1]
        start_match_time = match[2]
        end_match_time = match[3]
        # Si le match n'est pas fini
        if not match_finished:
            # Si le  match n'a pas demarrer
            if not match_al_sta:
                match_al_sta = True
                # Date de debut de match
                start_match_time = time.time()
            else:
                # Date de fin de  match
                end_match_time = time.time()
                # demander le score du joueur
                score_joueur_1 = self.enter_resultat_player(ref_joueur=ref_joueur_1)
                # Conclur le resultat de 2 eme joueur
                score_joueur_2 = 1 - score_joueur_1
                match_finished = True
        # Si le  match est fini
        else:
            self.match_finished()
        # instance match
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
        # Affichage du match
        self.match_view(
            joueur_1=ref_joueur_1,
            joueur_2=ref_joueur_2,
            match_number=1,
            score_joueur_1=score_joueur_1,
            score_joueur_2=score_joueur_2,
            color_joueur_1=color_joueur_1,
            start_match_time=start_match_time,
            end_match_time=end_match_time
        )
        return match, match_al_sta, match_finished

    # -----------------------------------------------------------------------------------------------------------------#


class MainMenu(Choice, MatchMenu):

    def menu(self):
        # init
        resultat = 0
        try:
            # Affichage du menu principal et demander quel menu souhaiter a acceder
            resultat = int(self.main_choice())
        except (ValueError, IndexError):
            self.print_error_enter_int()
            self.menu()
        # Gestion des joueurs
        if resultat == 1:
            self.sub_menu_player_1()
        # gestion des tournois
        elif resultat == 2:
            self.sub_menu_tournament_1()
        # Demmarer un tournois
        elif resultat == 3:
            self.start_playing_tournament()
        # Quitter le programme
        elif resultat == 5:
            self.message_visit()
            exit()
        # en cas d'erreur
        else:
            self.print_error_enter_int()
        self.menu()

#   -------------------------------------------------------------------------------------------------------------------#
