import random
import settings

# ---------------------------------------------------------------------------------------------------------------------#


class Match:

    def player_color(self):
        colors = ['Noir', 'Blanche']
        color_joueur_1 = random.choice(colors)
        color_joueur_2 = [color for color in colors if color != color_joueur_1][0]

        return color_joueur_1, color_joueur_2

    # -----------------------------------------------------------------------------------------------------------------#

    def players_points(self, ref_joueur, dict_points, points):
        dict_points[ref_joueur] += points
        return dict_points

    # -----------------------------------------------------------------------------------------------------------------#

    def matchs_already_played_function(self, ref_joueur_1, matchs_already_played, instance_players_tried, k=1):

        ref_joueur_2 = instance_players_tried[k]
        match_to_play1 = ref_joueur_1, ref_joueur_2
        match_to_play2 = (ref_joueur_2, ref_joueur_1)
        try:
            if match_to_play1 and match_to_play2 in matchs_already_played:
                k += 1
                ref_joueur_2 = self.matchs_already_played_function(
                    ref_joueur_1=ref_joueur_1,
                    matchs_already_played=matchs_already_played,
                    instance_players_tried=instance_players_tried,
                    k=k
                )
        except:
            ref_joueur_2 = instance_players_tried[1]
        return ref_joueur_2

    # -----------------------------------------------------------------------------------------------------------------#

    def match(
            self,
            ref_joueur_1,
            ref_joueur_2,
            match_number,
            color_joueur_1,
            color_joueur_2,
            score_joueur_1=None,
            score_joueur_2=None,
            start_match_time=None,
            end_match_time=None
    ):

        if score_joueur_1 == None:
            score_joueur_1 = 0

        if score_joueur_2 == None:
            score_joueur_2 = 0

        if start_match_time == None:
            start_match_time = 0

        if score_joueur_2 == None:
            end_match_time = 0

        joueur_1 = [ref_joueur_1, score_joueur_1, color_joueur_1]
        joueur_2 = [ref_joueur_2, score_joueur_2, color_joueur_2]

        self.match_view(
            joueur_1=ref_joueur_1,
            joueur_2=ref_joueur_2,
            match_number=match_number,
            score_joueur_1=score_joueur_1,
            score_joueur_2=score_joueur_2,
            color_joueur_1=color_joueur_1,
            color_joueur_2=color_joueur_1,
            start_match_time=start_match_time,
            end_match_time=end_match_time
        )

        return joueur_1, joueur_2, start_match_time, end_match_time

    # -----------------------------------------------------------------------------------------------------------------#

    def rounds_matchs(self, Round, matchs_already_played, instance_players_tried):

        length = len(instance_players_tried)

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
                match_number=k,
                color_joueur_1=color_joueur_1,
                color_joueur_2=color_joueur_2
            )
            tour_list.append(match_player)
        return tour_list, matchs_already_played

    # -----------------------------------------------------------------------------------------------------------------#
