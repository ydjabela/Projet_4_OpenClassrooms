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

        elif resultat == 2:
            tournament.add_tournament()

        elif int(resultat) == 3:
            player.search_player()

        elif int(resultat) == 4:
            tournament.search_tournament()

        elif resultat == 5:
            exit()

        else:
            choice.print_error_enter_int()
        print('-------------------------------------------------------------------------------------------------------')
        self.menu()


# ---------------------------------------------------------------------------------------------------------------------#
