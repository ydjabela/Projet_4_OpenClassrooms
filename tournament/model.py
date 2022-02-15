from tinydb import TinyDB, Query


# ---------------------------------------------------------------------------------------------------------------------#


class DatabaseTournaments:

    # base de données  joueurs
    def database_tournament(
            self,
            serialized_tournament=None,
            tournament_number=None,
            delete_tournament=False,
            delete_all=False

    ):
        db = TinyDB('db.json')
        table = db.table('tournois')
        tournaments = table.all()
        #ajout d'un  tournoi
        if serialized_tournament:
            table.insert(serialized_tournament)
        # suprimmer  un  tournoi
        elif delete_tournament:
            tournament = Query()
            table.remove(
                tournament.nom == tournaments[tournament_number]['nom']
                and
                tournament.lieu == tournaments[tournament_number]['lieu']
            )
        # suprimer tous  les  tournois
        elif delete_all:
            table.truncate()

        return tournaments, table

    # ---------------------------------------------------------------------------------------------------------------------#

    def update_tournament_data_base(
            self,
            tournament_number,
            key,
            value
    ):
        tournaments, table = self.database_tournament(tournament_number=tournament_number)
        tournament = Query()
        table.update({key: value}, tournament.nom == tournaments[tournament_number]['nom'])


# ---------------------------------------------------------------------------------------------------------------------#


class Tournament(DatabaseTournaments):

    def __init__(
            self,
            nom=None,
            lieu=None,
            date=None,
            tour=None,
            Tournees=None,
            Joueurs=None,
            controle_temps=None,
            Description=None
    ):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.tour = tour
        self.Tournees = Tournees
        self.Joueurs = Joueurs
        self.controle_temps = controle_temps
        self.Description = Description

    # -----------------------------------------------------------------------------------------------------------------#

    # Sauvegarder le tournois
    def save_tournament(self, serialized_tournament):
        self.database_tournament(serialized_tournament=serialized_tournament)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer un tournoi
    def ask_delete_tournament(self, tournament_number):
        self.database_tournament(tournament_number=tournament_number, delete_tournament=True)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer tous les tournois
    def delete_all_tournament(self):
        self.database_tournament(delete_all=True)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_tournament_value(self, tournament_number, key, value):
        self.update_tournament_data_base(tournament_number=tournament_number, key=key, value=value)

    # ---------------------------------------------------------------------------------------------------------------------#

    def search_tournament(self):
        tournaments, table = self.database_tournament()
        return tournaments

    # ---------------------------------------------------------------------------------------------------------------------#
