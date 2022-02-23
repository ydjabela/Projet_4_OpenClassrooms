from view.principal_view import Choice
from controller.controller_tournament import TournamentMenu
from controller.controller_player import PlayerMenu

# ---------------------------------------------------------------------------------------------------------------------#


class Match(TournamentMenu, PlayerMenu):

    def match(
            self,
            ref_joueur_1,
            ref_joueur_2,
            score_joueur_1=None,
            score_joueur_2=None
    ):

        if score_joueur_1 == None:
            score_joueur_1 = 0

        if score_joueur_2 == None:
            score_joueur_2 = 0

        joueur_1 = [ref_joueur_1, score_joueur_1]
        joueur_2 = [ref_joueur_2, score_joueur_2]

        return joueur_1, joueur_2

    # -----------------------------------------------------------------------------------------------------------------#

    def start_playing_tournament(self, selected_players):

        # selectionner un tournoi à jouer
        tournament_number, tournaments = self.choose_tournament(selected_players=selected_players)

        # trier les selected_players  par classement
        players_tried = self.tri_player_by_rang(selected_players=selected_players)
        self.search_player_view(players=players_tried)
        instance_players_tried = [i for i in range(len(players_tried))]

        # divisez les joueurs classés en deux moitiés
        player_list_sup = list()
        player_list_inf = list()
        length = len(instance_players_tried)
        div_length = int(length/2)
        for i in range(0, div_length):
            player_list_sup.append(instance_players_tried[i])
        for j in range(div_length, length):
            player_list_inf.append(instance_players_tried[j])

        # jumelé Le meilleur joueur de la moitié supérieure avec le meilleur joueur de la moitié inférieure
        # 1 er tour
        # definir les paires de joueurs
        tour = list()
        for k in range(0, div_length):
            ref_joueur_1 = player_list_sup[k]
            ref_joueur_2 = player_list_inf[k]
            match_player = self.match(ref_joueur_1=ref_joueur_1, ref_joueur_2=ref_joueur_2)
            tour.append(match_player)

        print('==========>1', tour)


        # Un tirage au sort des joueurs définira qui joue en blanc et qui joue en noir ;
        # il n'est donc pas nécessaire de mettre en place un équilibrage des couleurs.
        # TODO

        # Sauvegarder les résultats pour chaque paire
        # TODO

        # 2, 3 et 4e tour
        # Définir les paires de joueurs
        # triez tous les joueurs en fonction de leur nombre total de points.
        # Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        # TODO

        # Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite.
        # Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        # TODO

        # Sauvegarder les résultats pour chaque paire
        # TODO

    # -----------------------------------------------------------------------------------------------------------------#


class MainMenu(Choice, Match):

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


