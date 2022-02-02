from tinydb import TinyDB
import json
import settings


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

# ---------------------------------------------------------------------------------------------------------------------#
