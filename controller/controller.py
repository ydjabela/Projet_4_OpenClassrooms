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
        # init
        resultat = 0
        try:
            # Demander et affichage du menu gestion des joueurs
            resultat = int(self.player_sub_main_choice())
        except ValueError:
            self.print_error_enter_int()
            self.sub_menu_player_1()

        # Ajouter un joueur.
        if resultat == 1:
            familly_name, first_name, age, sex, classement = self.adding_player()
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
            # menu modification du joueur
            self.sub_menu_player_2()

        # Supprimmer un joueur.
        elif resultat == 3:
            # menu supprimer un joueur
            self.delete_player()

        # Affichage des joueurs.
        elif int(resultat) == 4:
            # voir les joueurs existant
            players = self.search_player()
            # Affichage des joueurs existant
            self.search_player_view(players=players)
            # si aucun joueur n'existe
            if len(players) == 0:
                self.no_player()

        # classement des joueurs
        elif int(resultat) == 5:
            # triage des joueur par ordre de classement et par ordre alphabetique
            player_tri_ranking, player_tri_alphabet = self.stat_classement()
            # Affichage des statistiques
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
        # init
        resultat_modif = 0
        player_number = 0

        try:
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
            resultat_modif = int(self.player_modification_spec())
        # en cas d'erreur
        except ValueError or IndexError:
            self.print_error_enter_int()
            self.sub_menu_player_2()
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
            self.change_age_player(
                player_number=player_number
            )
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
            self.change_classement_player(
                player_number=player_number
            )
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
        except ValueError:
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
        except ValueError:
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
        except ValueError:
            self.print_error_enter_int()
            self.delete_player()

    # ---------------------------------------------------------------------------------------------------------------------#

    def select_and_add_players(self):
        # init
        selected_players = list()
        first_list = list()
        second_list = list()
        # Chercher les joueurs existent
        players = self.search_player()
        # Si aucun joueur n'existe'
        if len(players) == 0:
            self.no_player()

        # construire une liste avec les nom dee tous les joueurs
        for player in players:
            first_list.append(player['familly_name'])

        for player in players:
            second_list.append(player['familly_name'])

        # Selectionner la list des joueurs qui vont jouer la partie
        while len(selected_players) < settings.nbr_player_max:
            # S'il manque des  joueurs
            if len(players) < settings.nbr_player_max:
                # Voir les  joueurs existent
                self.search_player_view(players=players)
                #  Affichage de  message qu'il faut ajouter des  joueurs
                self.need_add_players()
                # Ajouter  un  joueur
                familly_name, first_name, age, sex, classement = self.adding_player()
                # créer un object player
                player = Player(
                    familly_name=familly_name,
                    first_name=first_name,
                    age=age,
                    sex=sex,
                    classement=classement
                )
                # sauvegarder  le  joueurs
                player.save_player()
                # reactuliser  les  joueurs
                players = self.search_player()
                # actualiser  la selection des  joueurs
                selected_players = [i for i in range(len(players))]
            # S'il existe plus de  joueur qu'ona  besoin
            elif len(players) > settings.nbr_player_max:
                # Selectionner et afficher les joueurs a selectionner de la premiere liste
                selected_player = self.select_player(players=first_list)
                # Voir  la  position du joueur selectionné dans la seconde  liste
                pos = list(
                    np.where(np.array(second_list) == selected_player)[0]
                )
                # Ajouter la premier  position de joueur selectionner
                selected_players.append(int(pos[0]))
                # Supprimmer le joueur deja selectionner de  la  premiere liste
                del first_list[first_list.index(selected_player)]
            # S'il existe le  nombre exacte des joueurs  qu'il faut
            else:
                # Affichage des joueurs existent
                self.search_player_view(players=players)
                # Actualiser la liste des joueurs
                players = self.search_player()
                # Selectionner  la refecrence des joueurs
                selected_players = [i for i in range(len(players))]
                # Affichage d'un essage que la selection est complete
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
        # init
        resultat = 0
        #  Menu tournois
        try:
            resultat = int(self.tournament_sub_main_choice())
        except ValueError:
            self.print_error_enter_int()
            self.sub_menu_tournament_1()

        # Ajouter un tournament.
        if resultat == 1:
            nom, lieu, date, tour, Tournees, Joueurs, controle_temps, Description = self.adding_tournament()
            tournament = Tournament(
                nom=nom,
                lieu=lieu,
                date=date,
                tour=tour,
                Tournees=Tournees,
                Joueurs=Joueurs,
                controle_temps=controle_temps,
                Description=Description
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
        # Init
        tournament_number = 0
        resultat_modif = 0
        #  menu modification d'un  tournoi
        try:
            # voir le nombre de tournois
            tournaments = self.search_tournament()
            self.search_tournament_view(tournaments=tournaments)

            if len(tournaments) == 0:
                self.no_tournament()
                self.sub_menu_tournament_1()
            elif len(tournaments) == 1:
                tournament_number = 0
            else:
                tournament_number = int(self.tournament_modification()) - 1

            resultat_modif = int(self.tournament_modification_spec())
        except ValueError:
            self.print_error_enter_int()
            self.sub_menu_tournament_2()
        # modifier  le  nom
        if resultat_modif == 1:
            name = self.tournament_name_modification()
            self.ask_change_tournament_value(
                tournament_number=tournament_number,
                key='nom', value=name
            )
            self.tournament_modification_save()
        # modifier le  lieu
        elif resultat_modif == 2:
            lieu = self.tournament_lieu_modification()
            self.ask_change_tournament_value(
                tournament_number=tournament_number,
                key='lieu', value=lieu
            )
        # modifier la date
        elif resultat_modif == 3:
            date = self.tournament_date_modification()
            self.ask_change_tournament_value(
                tournament_number=tournament_number,
                key='date', value=date
            )
        # modifier nombre de tour
        elif resultat_modif == 4:
            tour = self.tournament_tour_modification()
            self.ask_change_tournament_value(tournament_number=tournament_number, key='tour', value=tour)
        # modifier la tournee
        elif resultat_modif == 5:
            self.tournament_tournees_modification()
        # modifier les joueurs
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
        # Init
        tournament_number = 0
        # voir les tournois existent
        tournaments = self.search_tournament()
        self.search_tournament_view(tournaments=tournaments)
        if len(tournaments) == 0:
            self.no_tournament()
            return
        elif len(tournaments) == 1:
            tournament_number = 0
        else:
            # Selectionner  le joueur a supprimer
            try:
                tournament_number = int(self.tournament_to_delete()) - 1
            except ValueError:
                self.print_error_enter_int()
                self.delete_tournament()
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
            try:
                self.search_tournament_view(tournaments=tournaments)
                tournament_number = int(self.tournament_to_play()) - 1
            except ValueError or IndexError:
                self.print_error_enter_int()
                tournament_number, tournaments = self.choose_tournament()

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
                color_joueur_2=color_joueur_1
            )
            tour_list.append(match_player)
        return tour_list, matchs_already_played

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
        joueurs = tournament['Joueurs']
        # Si les joueurs sont pas deja selectionnés
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
        #
        try:
            for selected_player in selected_players:
                dict_points[selected_player] = 0
            # verifier la tournée
            Tournees = tournament['Tournees']

            start_round = 1
            # si aucune tournee n'existe
            if Tournees == '':
                start_round = 1
            # S'il existe aumoins  une tournee voir  le  nombre de  match qui ont ete  jouer deja
            else:
                for match in Tournees:
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

                tournee_length = len(Tournees)
                if tournee_length == 4:
                    start_round = 2
                elif tournee_length == 8:
                    start_round = 3
                elif tournee_length == 12:
                    start_round = 4
                else:
                    # check if  he need to restart or quit
                    resultat = 0
                    try:
                        resultat = int(self.restart_round_choice())
                    except ValueError:
                        self.print_error_enter_int()
                        self.start_playing_tournament()

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
            # Demarrer  le  round
            for round in range(start_round, settings.TURNS + 1):

                # 1 er tour
                Round = 'Round {}'.format(round)
                self.round_view(Round=Round)

                if round == 1:
                    # trier les selected_players  par classement
                    players_tried = self.tri_player_by_rang(selected_players=selected_players)
                    # self.search_player_view(players=players_tried)
                    instance_players_tried = list()
                    for i in range(len(players_tried)):
                        ref_joueur, classement = players_tried[i]
                        instance_players_tried.append(ref_joueur)
                    # divisez les joueurs classés en deux moitiés
                    player_list_sup = list()
                    player_list_inf = list()
                    length = len(players_tried)
                    div_length = int(length / 2)
                    # liste des joueurs partie superieur
                    for i in range(0, div_length):
                        player_list_sup.append(instance_players_tried[i])
                    # liste des joueurs partie inférieur
                    for j in range(div_length, length):
                        player_list_inf.append(instance_players_tried[j])

                    # jumelé Le meilleur joueur de la moitié supérieure
                    # avec le meilleur joueur de la moitié inférieure
                    # Définir les paires de joueurs
                    tour_list = [Round]
                    for k in range(0, div_length):
                        # joueur de la partie superieur
                        ref_joueur_1 = player_list_sup[k]
                        # joueur de la partie inferieur
                        ref_joueur_2 = player_list_inf[k]
                        # match à jouer
                        match_to_play_1 = ref_joueur_1, ref_joueur_2
                        match_to_play_2 = ref_joueur_2, ref_joueur_1

                        # Enregistre les  match deja jouer sachant que
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
                            color_joueur_2=color_joueur_1,
                        )
                        tour_list.append(match_player)
                else:
                    # Trier par le nombre de points gagner
                    # triez tous les joueurs en fonction de leur nombre total de points.
                    # Et s'ils ont les meme points les classés par ordre de classement
                    instance_players_tried = list()
                    players_tried = self.tri_player_by_points(selected_players=selected_players,
                                                              dict_points=dict_points)
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

                # Sauvegarder les résultats pour chaque paire de joueur
                self.ask_change_tournament_value(
                    tournament_number=tournament_number,
                    key='Tournees',
                    value=matchs_round
                )
            # triage final
            players_tried = self.tri_player_by_points(selected_players=selected_players, dict_points=dict_points)
            self.search_player_view_classement(players=players_tried)

        except ValueError:
            self.print_error_enter_int()
            self.start_playing_tournament()

    # -----------------------------------------------------------------------------------------------------------------#

    def sub_menu_start_end_round(self, tour_list):
        # init
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
        # Demander de demarrer un match  ou de  le finir
        while True:
            try:
                if match_finished_1 and match_finished_2 and match_finished_3 and match_finished_4 is True:
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

            except ValueError:
                self.print_error_enter_int()
                match = self.sub_menu_start_end_round(tour_list)
            # Demmarrer ou finir  le match  n° 1
            if resultat_enter == 1:
                match_1, match_alerady_started_1, match_finished_1 = self.start_end_match(
                    match=match_1,
                    match_finished=match_finished_1,
                    match_alerady_started=match_alerady_started_1
                )
            # Demmarrer ou finir  le match  n° 2
            elif resultat_enter == 2:
                match_2, match_alerady_started_2, match_finished_2 = self.start_end_match(
                    match=match_2,
                    match_finished=match_finished_2,
                    match_alerady_started=match_alerady_started_2
                )
            # Demmarrer ou finir  le match  n° 3
            elif resultat_enter == 3:
                match_3, match_alerady_started_3, match_finished_3 = self.start_end_match(
                    match=match_3,
                    match_finished=match_finished_3,
                    match_alerady_started=match_alerady_started_3
                )
            # Demmarrer ou finir  le match  n° 4
            elif resultat_enter == 4:
                match_4, match_alerady_started_4, match_finished_4 = self.start_end_match(
                    match=match_4,
                    match_finished=match_finished_4,
                    match_alerady_started=match_alerady_started_4
                )
            # Arreter la tournee et le tournoi
            elif resultat_enter == 5:
                self.message_retour()
                self.menu()
                return
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
        # Init
        ref_joueur_1, score_joueur_1, color_joueur_1 = match[0]
        ref_joueur_2, score_joueur_2, color_joueur_2 = match[1]
        start_match_time = match[2]
        end_match_time = match[3]
        # Si le match n'est pas fini
        if not match_finished:
            # Si le  match n'a pas demarrer
            if not match_alerady_started:
                match_alerady_started = True
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
            color_joueur_2=color_joueur_1,
            start_match_time=start_match_time,
            end_match_time=end_match_time
        )

        return match, match_alerady_started, match_finished

    # -----------------------------------------------------------------------------------------------------------------#


class MainMenu(Choice, Match_Menu):

    def menu(self):
        # init
        resultat = 0
        try:
            # Affichage du menu principal et demander quel menu souhaiter a acceder
            resultat = int(self.main_choice())
        except ValueError:
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
