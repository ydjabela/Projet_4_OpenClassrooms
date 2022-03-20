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

        # ajout d'un tournoi ou de joueur
        if serialized:
            table.insert(serialized)

        # supprimer toute la table
        if delete_all:
            table.truncate()

        # supprimer un tournoi
        elif delete_tournament:
            tournament = Query()
            tournament_nom_selected = select_table[tournament_number]['nom']
            tournament_lieu_selected = select_table[tournament_number]['lieu']
            table.remove(tournament.nom == tournament_nom_selected and tournament.lieu == tournament_lieu_selected)

        # supprimer un joueur
        elif delete_player:
            player = Query()
            player_name_selected = select_table[player_number]['familly_name']
            player_first_name_selected = select_table[player_number]['first_name']
            table.remove(
                player.familly_name == player_name_selected and player.first_name == player_first_name_selected
            )

        return select_table, table

    # ---------------------------------------------------------------------------------------------------------------------#

    def update_tournament_data_base(
            self,
            tournament_number,
            key,
            value
    ):
        # mettre a jour un element d'un tournoi
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
        # mettre a jour un element d'un joueur
        players, table = self.database_game(select_table='players', player_number=player_number)
        player = Query()
        table.update({key: value}, player.familly_name == players[player_number]['familly_name'])

# ---------------------------------------------------------------------------------------------------------------------#
