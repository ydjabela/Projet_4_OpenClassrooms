from player.controller import PlayerMenu
from tournament.model import Tournament
from view import Choice

# ---------------------------------------------------------------------------------------------------------------------#


class MainMenu:

    def menu(self):
        choice = Choice()
        tournament = Tournament()
        player_menu = PlayerMenu()

        try:
            resultat = int(choice.main_choice())
        except:
            choice.print_error_enter_int()
            self.menu()

        if resultat == 1:
            player_menu.sub_menu()

        elif resultat == 2:
            tournament.add_tournament()

        elif int(resultat) == 4:
            tournament.search_tournament()

        elif resultat == 5:
            print('Merci pour  votre visite')
            exit()

        else:
            choice.print_error_enter_int()
        print('-------------------------------------------------------------------------------------------------------')
        self.menu()


# ---------------------------------------------------------------------------------------------------------------------#
