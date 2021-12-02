from tinydb import TinyDB
import json

class Player:

    def __init__(self, familly_name, first_name, age, sex):
        print('=====>1', familly_name, first_name, age, sex)
        self.familly_name = familly_name
        self.first_name = first_name
        self.age = age
        self.sex = sex

    def to_JSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))





# ---------------------------------------------------------------------------------------------------------------------#

# convertir en dictionnaire$


def serialzation(player):
    serialized_player = {
        'familly_name': player.familly_name,
        'first_name': player.first_name,
        'age': player.age,
        'sex': player.sex
    }
    print('===========>2', serialized_player)
    familly_name = serialized_player['familly_name']
    first_name = serialized_player['first_name']
    sex = serialized_player['sex']
    age = serialized_player['age']
    player_serialized = Player(familly_name=familly_name, first_name=first_name, age=age, sex=sex)
    return serialized_player


player1 = Player(familly_name='John', first_name='Cena', age=44, sex='M')
serialized_players1 = serialzation(player=player1)
player2 = Player(familly_name='Jooooohn', first_name='Cenaaa', age=44, sex='M')
serialized_players2 = serialzation(player=player2)


db = TinyDB('db.json')
players_table = db.table('players')
# clear the table first
players_table.truncate()
players = (serialized_players1, serialized_players2)
for player in players:
    players_table.insert(player)
