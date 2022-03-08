from model.database import Database

# ---------------------------------------------------------------------------------------------------------------------#


class Tournament(Database):

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
        self.database_game(select_table='tournois', serialized=serialized_tournament)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer un tournoi
    def ask_delete_tournament(self, tournament_number):
        self.database_game(select_table='tournois', tournament_number=tournament_number, delete_tournament=True)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer tous les tournois
    def delete_all_tournament(self):
        self.database_game(select_table='tournois', delete_all=True)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_tournament_value(self, tournament_number, key, value):
        self.update_tournament_data_base(tournament_number=tournament_number, key=key, value=value)

    # -----------------------------------------------------------------------------------------------------------------#

    def search_tournament(self):
        tournaments, table = self.database_game(select_table='tournois')
        return tournaments

    # ---------------------------------------------------------------------------------------------------------------------#
