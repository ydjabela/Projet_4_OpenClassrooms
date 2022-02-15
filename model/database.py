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


class Databaseplayers:

    # base de données  joueurs
    def database_players(
            self,
            serialized_player=None,
            player_number=None,
            delete_player=False,
            delete_all=False

    ):
        db = TinyDB('db.json')
        table = db.table('players')
        players = table.all()

        #ajout d'un  joueur
        if serialized_player:
            table.insert(serialized_player)

        # suprimer  un  joueur
        elif delete_player:
            player = Query()
            table.remove(
                player.familly_name == players[player_number]['familly_name']
                and
                player.first_name == players[player_number]['first_name']
            )
        # suprimer tous  les  joueurs
        elif delete_all:
            table.truncate()

        return players, table

    # ---------------------------------------------------------------------------------------------------------------------#

    def update_player_data_base(
            self,
            player_number,
            key,
            value
    ):
        players, table = self.database_players(player_number=player_number)
        player = Query()
        table.update({key: value}, player.familly_name == players[player_number]['familly_name'])
