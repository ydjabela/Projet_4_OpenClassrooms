from model.database import Databaseplayers
from operator import itemgetter


# ---------------------------------------------------------------------------------------------------------------------#


class Player(Databaseplayers):

    def __init__(self, familly_name=None, first_name=None, age=None, sex=None, classement=None):
        self.familly_name = familly_name
        self.first_name = first_name
        self.age = age
        self.sex = sex
        self.classement = classement

    # -----------------------------------------------------------------------------------------------------------------#

    # Sauvegarder le joueur
    def save_player(self, serialized_player):
        self.database_players(serialized_player=serialized_player)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer un joueur
    def ask_delete_player(self, player_number):
        self.database_players(player_number=player_number, delete_player=True,)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer tous les joueurs
    def delete_all_player(self):
        self.database_players(delete_all=True)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_value(self, player_number, key, value):
        self.update_player_data_base(player_number=player_number, key=key, value=value)

    # -----------------------------------------------------------------------------------------------------------------#

    # Affichage des joueurs
    def search_player(self):
        players, table = self.database_players()
        return players

# ---------------------------------------------------------------------------------------------------------------------#


class Player_Stat(Databaseplayers):
    # -----------------------------------------------------------------------------------------------------------------#

    def stat_classement(self):
        """returns a classification by rank or alphabetical"""

        players, table = self.database_players()
        tri_rank = sorted(players, key=lambda k: k["classement"], reverse=False)
        tri_alphabet = sorted(players, key=itemgetter('familly_name'), reverse=False)

        return tri_rank, tri_alphabet
