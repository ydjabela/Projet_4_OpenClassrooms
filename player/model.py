from tinydb import TinyDB, Query
import settings

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

        db = TinyDB('db.json')
        players_table = db.table('players')
        players = players_table.all()
        if len(players) < nbr_player_max:
            players_table.insert(serialized_player)
        else:
            print('le nombre de joueurs à atteint le maximum')

    # -----------------------------------------------------------------------------------------------------------------#

    # Affichage des joueurs
    def search_player(self):
        db = TinyDB('db.json')
        table = db.table('players')
        players = table.all()
        try:
            if not len(players) == 0:
                i = 1
                print('les joueurs sont : ')
                print(
                    "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                        "N°", "Familly name", "First name", "Age", "Sex", "Classement"
                    )
                )
                for player in players:
                    familly_name = player['familly_name']
                    first_name = player['first_name']
                    age = player['age']
                    sex = player['sex']
                    classement = player['classement']
                    print(
                        "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                            i, familly_name, first_name, age, sex, classement
                        )
                    )
                    i += 1

        except Exception as e:
            print('Error', e)
        return players

    # -----------------------------------------------------------------------------------------------------------------#

    def stat_classement(self):
        """returns a classification by rank or alphabetical"""
        db = TinyDB('db.json')
        table = db.table('players')
        players = table.all()
        tri_rank = sorted(players, key=lambda k: k["classement"], reverse=False)
        print(players)
        tri_alphabet = sorted(players, key=lambda k: k["familly_name"], reverse=True)
        print(tri_alphabet)
        player_tri_ranking = []
        player_tri_alphabet = []
        for i in tri_rank:
            player_tri_ranking.append(i)
        for j in tri_alphabet:
            player_tri_alphabet.append(j)
        print(player_tri_alphabet)
        try:
            if not len(players) == 0:
                i = 1
                print('classement des  joueurs  par ordre de classement : ')
                print(
                    "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                        "N°", "Familly name", "First name", "Age", "Sex", "Classement"
                    )
                )
                for player in player_tri_ranking:
                    familly_name = player['familly_name']
                    first_name = player['first_name']
                    age = player['age']
                    sex = player['sex']
                    classement = player['classement']
                    print(
                        "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                            i, familly_name, first_name, age, sex, classement
                        )
                    )
                    i += 1
                print('classement des  joueurs  par ordre alphabetique : ')
                print(
                    "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                        "N°", "Familly name", "First name", "Age", "Sex", "Classement"
                    )
                )
                i = 0
                for player in player_tri_alphabet:
                    familly_name = player['familly_name']
                    print(familly_name, type(familly_name))
                    first_name = player['first_name']
                    age = player['age']
                    sex = player['sex']
                    classement = player['classement']
                    print(
                        "{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(
                            i, familly_name, first_name, age, sex, classement
                        )
                    )
                    i += 1

        except Exception as e:
            print('Error', e)

        return tri_rank, tri_alphabet

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
