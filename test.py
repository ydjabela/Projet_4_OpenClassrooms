from tinydb import TinyDB
import json

# ---------------------------------------------------------------------------------------------------------------------#


class Player:

    def __init__(self, familly_name, first_name, age, sex, classement):
        self.familly_name = familly_name
        self.first_name = first_name
        self.age = age
        self.sex = sex
        self.classement = classement

# ---------------------------------------------------------------------------------------------------------------------#


# convertir en dictionnaire$
def serialzation(player):
    serialized_player = {
        'familly_name': player.familly_name,
        'first_name': player.first_name,
        'age': player.age,
        'sex': player.sex,
        'classement': player.classement
    }
    return serialized_player

# ---------------------------------------------------------------------------------------------------------------------#


player1 = Player(familly_name='John', first_name='Cena', age=44, sex='M', classement=22)
serialized_players1 = serialzation(player=player1)
player2 = Player(familly_name='Jooooohn', first_name='Cenaaa', age=44, sex='M', classement=11)
serialized_players2 = serialzation(player=player2)


db = TinyDB('db.json')
players_table = db.table('players')
# clear the table first
players_table.truncate()
players = (serialized_players1, serialized_players2)
for player in players:
    players_table.insert(player)


print('==============================================================================================')

# ---------------------------------------------------------------------------------------------------------------------#


class Tournoi:

    def __init__(
            self,
            nom,
            lieu,
            date,
            tour,
            Tournees,
            Joueurs,
            controle_temps,
            Description
    ):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.tour = tour
        self.Tournees = Tournees
        self.Joueurs = Joueurs
        self.controle_temps = controle_temps
        self.Description = Description


# ---------------------------------------------------------------------------------------------------------------------#


# convertir en dictionnaire$
def serialzation_tournoi(tournoi):
    serialized_tournoi = {
        'nom': tournoi.nom,
        'lieu': tournoi.lieu,
        'date': tournoi.date,
        'tour': tournoi.tour,
        'Tournees': tournoi.Tournees,
        'Joueurs': tournoi.Joueurs,
        'controle_temps': tournoi.controle_temps,
        'Description': tournoi.Description
    }
    return serialized_tournoi

# ---------------------------------------------------------------------------------------------------------------------#


Tournoi1 = Tournoi(
    nom='tour 1',
    lieu='paris',
    date='4/11/2021',
    tour=4,
    Tournees=(1, 2),
    Joueurs=(1, 2),
    controle_temps=2,
    Description='ceci un test'
)
serialized_tournoi1 = serialzation_tournoi(tournoi=Tournoi1)
Tournoi2 = Tournoi(
    nom='tour 3',
    lieu='marseille',
    date='4/11/2021',
    tour=4,
    Tournees=(1, 2),
    Joueurs=(1, 2),
    controle_temps=2,
    Description='ceci un test'
)
serialized_tournoi2 = serialzation_tournoi(tournoi=Tournoi2)


db = TinyDB('db.json')
tournois_table = db.table('tournois')
# clear the table first
tournois_table.truncate()
tournois = (serialized_tournoi1, serialized_tournoi2)
for tournoi in tournois:
    tournois_table.insert(tournoi)
