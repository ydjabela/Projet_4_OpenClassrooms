from tinydb import TinyDB, Query

# ---------------------------------------------------------------------------------------------------------------------#


class Database:
    def database_game(
            self,
            select_table,
            tournament_number=None,
            player_number=None,
            delete_tournament=False,
            delete_player=False,
            delete_all=False,
            serialized=None
    ):
        db = TinyDB('db.json')
        table = db.table(select_table)
        select_table = table.all()

        # ajout d'un  tournoi ou de joueur
        if serialized:
            table.insert(serialized)

        # suprimer tout la table
        if delete_all:
            table.truncate()

        # suprimmer un tournois
        elif delete_tournament:
            tournament = Query()
            table.remove(
                tournament.nom == select_table[tournament_number]['nom']
                and
                tournament.lieu == select_table[tournament_number]['lieu']
            )

        # suprimer un joueur
        elif delete_player:
            player = Query()
            table.remove(
                player.familly_name == select_table[player_number]['familly_name']
                and
                player.first_name == select_table[player_number]['first_name']
            )

        return select_table, table

    # ---------------------------------------------------------------------------------------------------------------------#

    def update_tournament_data_base(
            self,
            tournament_number,
            key,
            value
    ):
        tournaments, table = self.database_game(select_table='tournois', tournament_number=tournament_number)
        tournament = Query()
        table.update({key: value}, tournament.nom == tournaments[tournament_number]['nom'])

    # ---------------------------------------------------------------------------------------------------------------------#

    def update_player_data_base(
            self,
            player_number,
            key,
            value
    ):
        players, table = self.database_game(select_table='players', player_number=player_number)
        player = Query()
        table.update({key: value}, player.familly_name == players[player_number]['familly_name'])

# ---------------------------------------------------------------------------------------------------------------------#
