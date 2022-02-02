from player.model import Player
from tournament.model import Tournament
from view import Choice

# ---------------------------------------------------------------------------------------------------------------------#


class MainMenu:

    def menu(self):
        choice = Choice()
        tournament = Tournament()
        player = Player()

        try:
            resultat = int(choice.main_choice())
        except:
            choice.print_error_enter_int()
            self.menu()

        if resultat == 1:
            player.add_players()
            self.menu()

        elif resultat == 2:
            tournament.add_tournament()
            self.menu()

        elif resultat == 3:
            exit()

        else:
            choice.print_error_enter_int()
            self.menu()

# ---------------------------------------------------------------------------------------------------------------------#
