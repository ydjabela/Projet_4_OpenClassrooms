from model.database import Database
from operator import itemgetter


# ---------------------------------------------------------------------------------------------------------------------#


class Player(Database):

    def __init__(self, familly_name=None, first_name=None, age=None, sex=None, classement=None):
        self.familly_name = familly_name
        self.first_name = first_name
        self.age = age
        self.sex = sex
        self.classement = classement

    # -----------------------------------------------------------------------------------------------------------------#

    def save_player(self):
        # Serilaisation d'un joueur
        serialized_player = {
            'familly_name': self.familly_name,
            'first_name': self.first_name,
            'age': self.age,
            'sex': self.sex,
            'classement': self.classement
        }
        # Sauvegarder le joueur
        self.database_game(select_table='players', serialized=serialized_player)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_delete_player(self, player_number):
        # Supprimer un joueur
        self.database_game(select_table='players', player_number=player_number, delete_player=True)

    # -----------------------------------------------------------------------------------------------------------------#

    def delete_all_player(self):
        # Supprimer tous les joueurs
        self.database_game(select_table='players', delete_all=True)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_value(self, player_number, key, value):
        # mettre a jour un joueur
        self.update_player_data_base(player_number=player_number, key=key, value=value)

    # -----------------------------------------------------------------------------------------------------------------#

    def search_player(self):
        # Chercher tous les joueurs
        players, table = self.database_game(select_table='players')
        return players

# ---------------------------------------------------------------------------------------------------------------------#


class Player_Stat(Database):

    def stat_classement(self):
        """returns a classification by rank or alphabetical"""
        # Chercher tous les joueurs
        players, table = self.database_game(select_table='players')
        # Triage par classement
        tri_rank = sorted(players, key=lambda k: k["classement"], reverse=False)
        # Triage par ordre alphabetique
        tri_alphabet = sorted(players, key=itemgetter('familly_name'), reverse=False)

        return tri_rank, tri_alphabet

    # -----------------------------------------------------------------------------------------------------------------#
    @staticmethod
    def tri_rank_selected_player(players, selected_players):
        # filtré les joueurs parmi la selection
        selected_players_list = list()
        for selected_player in selected_players:
            selected_players_list.append(players[selected_player])
        # Triage par classement
        players_tried = sorted(selected_players_list, key=lambda k: k["classement"], reverse=False)
        return players_tried

    # -----------------------------------------------------------------------------------------------------------------#
