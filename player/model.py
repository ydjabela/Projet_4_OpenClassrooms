from tinydb import TinyDB, Query
import settings
from operator import itemgetter

# ---------------------------------------------------------------------------------------------------------------------#


class Databaseplayers:

    # Affichage des joueurs
    def database_players(
            self,
            serialized_player=None,
            player_number=None,
            delete_all=False

    ):
        db = TinyDB('db.json')
        table = db.table('players')
        players = table.all()
        if serialized_player:
            table.insert(serialized_player)

        elif player_number:
            player = Query()
            table.remove(
                player.familly_name == players[player_number]['familly_name']
                and
                player.first_name == players[player_number]['first_name']
            )

        elif delete_all:
            table.truncate()

        return players, table

    def save_date(self):
        players, table = self.search_player()


# ---------------------------------------------------------------------------------------------------------------------#


class Player:

    def __init__(self, familly_name=None, first_name=None, age=None, sex=None, classement=None):
        self.familly_name = familly_name
        self.first_name = first_name
        self.age = age
        self.sex = sex
        self.classement = classement

    # -----------------------------------------------------------------------------------------------------------------#

    # Sauvegarder le joueur
    def save_player(self, serialized_player):
        nbr_player_max = settings.nbr_player_max
        Databasegame = Databaseplayer()
        Databasegame.database_players(serialized_player=serialized_player)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer un joueur
    def ask_delete_player(self, player_number):
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            player = Query()
            table.remove(player.familly_name == players[player_number]['familly_name'])

        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer tous les joueurs
    def delete_all_player(self):
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            table.truncate()

        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_name(self, name, player_number):
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            player = Query()
            table.update({'familly_name': name}, player.familly_name == players[player_number]['familly_name'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_first_name(self, prenom, player_number):
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            player = Query()
            table.update({'first_name': prenom}, player.familly_name == players[player_number]['familly_name'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_age(self, age, player_number):
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()

            player = Query()
            table.update({'age': age}, player.familly_name == players[player_number]['familly_name'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_sex(self, sex, player_number):
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            player = Query()
            table.update({'sex': sex}, player.familly_name == players[player_number]['familly_name'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_classement(self, classement, player_number):
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            player = Query()
            table.update({'classement': classement}, player.familly_name == players[player_number]['familly_name'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------------------------#


class Player_Stat:
    # -----------------------------------------------------------------------------------------------------------------#

    def stat_classement(self):
        """returns a classification by rank or alphabetical"""
        db = TinyDB('db.json')
        table = db.table('players')
        players = table.all()
        tri_rank = sorted(players, key=lambda k: k["classement"], reverse=False)
        tri_alphabet = sorted(players, key=itemgetter('familly_name'), reverse=False)

        return tri_rank, tri_alphabet
