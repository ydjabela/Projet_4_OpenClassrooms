from tinydb import TinyDB
import json
import settings

# ---------------------------------------------------------------------------------------------------------------------#


class Player:

    def __init__(self, familly_name=None, first_name=None, age=None, sex=None, classement=None):
        self.familly_name = familly_name
        self.first_name = first_name
        self.age = age
        self.sex = sex
        self.classement = classement

    # convertir en dictionnaire$
    def serialzation(self, player):
        serialized_player = {
            'familly_name': player.familly_name,
            'first_name': player.first_name,
            'age': player.age,
            'sex': player.sex,
            'classement': player.classement
        }
        return serialized_player

    def add_player(self):

        familly_name = str(input('familly_name : '))
        first_name = str(input('first_name: '))
        age = int(input('age: '))
        sex = str(input('sex: '))
        classement = int(input('classement: '))
        player = Player(familly_name=familly_name, first_name=first_name, age=age, sex=sex, classement=classement)
        serialized_players = self.serialzation(player=player)
        return serialized_players

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

    def search_player(self):
        try:
            print('les joueurs sont : ')
            db = TinyDB('db.json')
            table = db.table('players')
            players = table.all()
            i = 1
            print("{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format("N°", "Familly name", "First name", "Age", "Sex", "Classement"))
            for player in players:
                familly_name = player['familly_name']
                first_name = player['first_name']
                age = player['age']
                sex = player['sex']
                classement = player['classement']
                print("{:<5} {:<25} {:<25} {:<15} {:<15} {:<15}".format(i, familly_name, first_name, age, sex, classement))
                i += 1

        except Exception as e:
            print('Error', e)
