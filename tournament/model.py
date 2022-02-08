from tinydb import TinyDB, Query
import json
import settings

# ---------------------------------------------------------------------------------------------------------------------#


class Tournament:

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

        db = TinyDB('db.json')
        tournaments_table = db.table('tournois')
        tournaments = tournaments_table.all()
        tournaments_table.insert(serialized_tournament)

    # ---------------------------------------------------------------------------------------------------------------------#

    # convertir en dictionnaire
    def serialzation_tournament(self, tournoi):
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

    def add_tournament(self):
        nom = str(input('Nom du tournoi: '))
        lieu = str(input('lieu: '))
        date = str(input('date: '))
        tour = int(input('tour: '))
        Tournees = int(input('Tournees: '))
        Joueurs = int(input('Joueurs: '))
        controle_temps = int(input('controle_temps: '))
        Description = str(input('Description: '))
        tournoi = Tournament(
            nom=nom,
            lieu=lieu,
            date=date,
            tour=tour,
            Tournees=Tournees,
            Joueurs=Joueurs,
            controle_temps=controle_temps,
            Description=Description
        )
        serialized_tournoi = self.serialzation_tournament(tournoi=tournoi)

        db = TinyDB('db.json')
        tournoi_table = db.table('tournois')
        # clear the table first
        tournoi_table.truncate()
        tournoi_table.insert(serialized_tournoi)

    # ---------------------------------------------------------------------------------------------------------------------#

    def search_tournament(self):
        try:
            print('le tournois est : ')
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            i = 1
            print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20} {:<15}".format("N°", "Nom", "Lieu", "Date", "Tour", "Tournees", "Joueurs", "Controle temps", "Description"))
            for tournament in tournaments:
                nom = tournament['nom']
                lieu = tournament['lieu']
                date = tournament['date']
                tour = tournament['tour']
                Tournees = tournament['Tournees']
                Joueurs = tournament['Joueurs']
                controle_temps = tournament['controle_temps']
                Description = tournament['Description']

                print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20} {:<15}".format(
                    i, nom, lieu, date, tour, str(Tournees), str(Joueurs), controle_temps, Description))
                i += 1

        except Exception as e:
            print('Error', e)
        return  tournaments

    # ---------------------------------------------------------------------------------------------------------------------#

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer un tournoi
    def ask_delete_tournament(self, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.remove(tournament.nom == tournaments[tournament_number]['nom'])

        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    # Supprimer tous les tournois
    def delete_all_tournament(self):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            table.truncate()

        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_name(self, name, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.update({'nom': name}, tournament.nom == tournaments[tournament_number]['nom'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_lieu(self, lieu, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.update({'lieu': lieu}, tournament.nom == tournaments[tournament_number]['nom'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_date(self, date, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.update({'date': date}, tournament.nom == tournaments[tournament_number]['nom'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_tour(self, tour, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.update({'tour': tour}, tournament.nom == tournaments[tournament_number]['nom'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_Tournees(self, Tournees, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.update({'Tournees': Tournees}, tournament.nom == tournaments[tournament_number]['nom'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_Joueurs(self, Joueurs, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.update({'Joueurs': Joueurs}, tournament.nom == tournaments[tournament_number]['nom'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_controle_temps(self, controle_temps, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.update({'controle_temps': controle_temps}, tournament.nom == tournaments[tournament_number]['nom'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#

    def ask_change_Description(self, Description, tournament_number):
        try:
            db = TinyDB('db.json')
            table = db.table('tournois')
            tournaments = table.all()
            tournament = Query()
            table.update({'Description': Description}, tournament.nom == tournaments[tournament_number]['nom'])
        except Exception as e:
            print('Error', e)

    # -----------------------------------------------------------------------------------------------------------------#
