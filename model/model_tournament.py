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
        # Init
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
    def save_tournament(self):
        # serialisation d'un tournoi
        serialized_tournament = {
            'nom': self.nom,
            'lieu': self.lieu,
            'date': self.date,
            'tour': self.tour,
            'Tournees': self.Tournees,
            'Joueurs': self.Joueurs,
            'controle_temps': self.controle_temps,
            'Description': self.Description
        }
        # Save tournoi
        self.database_game(select_table='tournois', serialized=serialized_tournament)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_delete_tournament(self, tournament_number):
        # Supprimer un tournoi
        self.database_game(select_table='tournois', tournament_number=tournament_number, delete_tournament=True)

    # -----------------------------------------------------------------------------------------------------------------#

    def delete_all_tournament(self):
        # Supprimer tous les tournois
        self.database_game(select_table='tournois', delete_all=True)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_tournament_value(self, tournament_number, key, value):
        # Mettre a jour un tournoi
        self.update_tournament_data_base(tournament_number=tournament_number, key=key, value=value)

    # -----------------------------------------------------------------------------------------------------------------#

    def search_tournament(self):
        # Chercher tous les tournois
        tournaments, table = self.database_game(select_table='tournois')
        return tournaments

    # ---------------------------------------------------------------------------------------------------------------------#
