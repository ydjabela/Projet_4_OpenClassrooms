# -----------------------------------------------------------------------------------------------------------------#

def matchs_already_played_function(ref_joueur_1, matchs_already_played, instance_players_tried, k=1):

    ref_joueur_2 = instance_players_tried[k]
    match_to_play1 = ref_joueur_1, ref_joueur_2
    match_to_play2 = (ref_joueur_2, ref_joueur_1)
    print('====match_to_play', match_to_play1)
    if match_to_play1 and match_to_play2 in matchs_already_played:

        k += 1
        ref_joueur_2 = matchs_already_played_function(
            ref_joueur_1=ref_joueur_1,
            matchs_already_played=matchs_already_played,
            instance_players_tried=instance_players_tried,
            k=k
        )


    return ref_joueur_2

# -----------------------------------------------------------------------------------------------------------------#


def rounds_matchs(Round, matchs_already_played, instance_players_tried):

    length = len(instance_players_tried)

    # jumelé Le meilleur joueur de avec le deuxieme meilleur joueur
    tour_list = [Round]
    print('\n====Round:', round)
    for k in range(1, 4+1):
        print('====players:', instance_players_tried)

        ref_joueur_1 = instance_players_tried[0]

        print('====match:', k)

        ref_joueur_2 = matchs_already_played_function(
            ref_joueur_1=ref_joueur_1,
            matchs_already_played=matchs_already_played,
            instance_players_tried=instance_players_tried
        )
        match_to_play1 = (ref_joueur_1, ref_joueur_2)
        match_to_play2 = (ref_joueur_2, ref_joueur_1)

        matchs_already_played.append(match_to_play1)
        matchs_already_played.append(match_to_play2)
        print('====2', matchs_already_played)
        del instance_players_tried[instance_players_tried.index(ref_joueur_1)]
        del instance_players_tried[instance_players_tried.index(ref_joueur_2)]


matchs_already_played = [(0, 4), (4, 0), (1, 5), (5, 1), (2, 6), (6, 2), (3, 7), (7, 3)]

for round in range(2, 4+1):
    instance_players_tried = [0, 6, 1, 7, 2, 3, 4, 5]
    rounds_matchs(
        Round=round,
        matchs_already_played=matchs_already_played,
        instance_players_tried=instance_players_tried)
