from tinydb import TinyDB
import json
import settings
from player.view import Error_enter

# ---------------------------------------------------------------------------------------------------------------------#


class Player:

    def __init__(self, familly_name=None, first_name=None, age=None, sex=None, classement=None):
        self.familly_name = familly_name
        self.first_name = first_name
        self.age = age
        self.sex = sex
        self.classement = classement

    # -----------------------------------------------------------------------------------------------------------------#

    # convertir en dictionnaire
    def serialzation(self, player):
        serialized_player = {
            'familly_name': player.familly_name,
            'first_name': player.first_name,
            'age': player.age,
            'sex': player.sex,
            'classement': player.classement
        }
        return serialized_player

    # -----------------------------------------------------------------------------------------------------------------#

    # Ajouter un joueur
    def add_player(self):
        error_enter = Error_enter()
        familly_name = str(input('familly_name : '))
        first_name = str(input('first_name: '))

        def add_age():
            try:
                age = int(input('age: '))
            except:
                error_enter.print_error_enter_int_age()
                add_age()
            return age

        age = add_age()
        sex = str(input('sex: '))
        classement = int(input('classement: '))
        player = Player(familly_name=familly_name, first_name=first_name, age=age, sex=sex, classement=classement)
        serialized_player = self.serialzation(player=player)
        return serialized_player

    # -----------------------------------------------------------------------------------------------------------------#

    # Sauvegarder le joueur
    def save_player(self):
        nbr_player_max = settings.nbr_player_max

        db = TinyDB('db.json')
        players_table = db.table('players')
        players = players_table.all()
        if len(players) < nbr_player_max:
            players_table.insert(self.add_player())
        else:
            print('le nombre de joueurs à atteint le maximum')

    # -----------------------------------------------------------------------------------------------------------------#

    # Ajouter et sauvegarder  plusieurs joueurs
    def add_players(self):
        players = list()
        nbr_player = settings.nbr_player
        for i in range(1, nbr_player+1):
            print('add player number : ', i)
            serialized_players = self.add_player()
            players.append(serialized_players)

        db = TinyDB('db.json')
        players_table = db.table('players')
        # clear the table first
        players_table.truncate()
        for player in players:
            players_table.insert(player)

    # -----------------------------------------------------------------------------------------------------------------#

    # Affichage des joueurs
    def search_player(self):
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            if len(players) == 0:
                print('la liste des joueurs est vide')
                return
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

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer un joueur
    def delete_player(self):
        self.search_player()
        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            print(players)
            table.remove(1)

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
    def modif_element_player(self, player):
        # manages the requests between the view and the modify player function

        self.ask_change_name(player)
        self.ask_change_first_name(player)
        self.ask_change_birth_date(player)
        self.ask_change_sex(player)
        self.ask_change_rank(player)
        return player

    # modifier un joueur.
    def modify_a_player(self, player_number=None):
        self.search_player()

        try:
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            if len(players) == 0:
                print('la liste des joueurs est vide')
                return
            elif len(players) == 1:
                self.modif_element_player(player=players)
                return

            else:
                if player_number is not None:
                    print('=======>', players[player_number])
                    self.modif_element_player(player=players[player_number])
                    '''
                    for player in players:
                        if player.get("pk") == modif.get("pk"):
                            player_doc_id = player.doc_id
                            db.upsert(Document(modif, doc_id=player_doc_id))
                    '''
                else:
                    return

        except Exception as e:
            print('Error', e)

# ---------------------------------------------------------------------------------------------------------------------#
