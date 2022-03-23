import random

# ---------------------------------------------------------------------------------------------------------------------#


class Match:
    @staticmethod
    def player_color():
        # Choix de couleur
        colors = ['Noir', 'Blanche']
        # Couleur du joueur 1
        color_joueur_1 = random.choice(colors)
        color_joueur_2 = [color for color in colors if color != color_joueur_1][0]

        return color_joueur_1, color_joueur_2

    # -----------------------------------------------------------------------------------------------------------------#
    @staticmethod
    def players_points(ref_joueur, dict_points, points):
        # Ajouter les points pour le joueur
        dict_points[ref_joueur] += points
        return dict_points

    # -----------------------------------------------------------------------------------------------------------------#

    def matchs_already_played_function(self, ref_joueur_1, matchs_already_played, instance_players_tried, k=1):
        # Init
        ref_joueur_2 = instance_players_tried[k]
        match_to_play1 = ref_joueur_1, ref_joueur_2
        match_to_play2 = (ref_joueur_2, ref_joueur_1)

        try:
            # Voir si le match a ete deja jouer
            if match_to_play1 and match_to_play2 in matchs_already_played:
                k += 1
                ref_joueur_2 = self.matchs_already_played_function(
                    ref_joueur_1=ref_joueur_1,
                    matchs_already_played=matchs_already_played,
                    instance_players_tried=instance_players_tried,
                    k=k
                )
        except (ValueError, IndexError):
            ref_joueur_2 = instance_players_tried[1]
        return ref_joueur_2

    # -----------------------------------------------------------------------------------------------------------------#
    @staticmethod
    def match(
            ref_joueur_1,
            ref_joueur_2,
            color_joueur_1,
            color_joueur_2,
            score_joueur_1=None,
            score_joueur_2=None,
            start_match_time=None,
            end_match_time=None
    ):
        # init
        if score_joueur_1 is None:
            score_joueur_1 = 0

        if score_joueur_2 is None:
            score_joueur_2 = 0

        if start_match_time is None:
            start_match_time = 0

        if score_joueur_2 is None:
            end_match_time = 0
        # tuple joueur
        joueur_1 = [ref_joueur_1, score_joueur_1, color_joueur_1]
        joueur_2 = [ref_joueur_2, score_joueur_2, color_joueur_2]

        return joueur_1, joueur_2, start_match_time, end_match_time

    # -----------------------------------------------------------------------------------------------------------------#
