from view.principal_view import Choice
from controller.controller_tournament import TournamentMenu
from controller.controller_player import PlayerMenu

# ---------------------------------------------------------------------------------------------------------------------#


class MainMenu(Choice, TournamentMenu, PlayerMenu):

    def menu(self):
        resultat = 0
        try:
            resultat = int(self.main_choice())
        except:
            self.print_error_enter_int()
            self.menu()

        if resultat == 1:
            self.sub_menu_player_1()

        elif resultat == 2:
            self.sub_menu_tournament_1()

        elif resultat == 3:
            selected_players = self.select_and_add_players()
            tournament_number, tournaments = self.start_playing_tournament(players=selected_players)

        elif resultat == 5:
            self.message_visit()
            exit()

        else:
            self.print_error_enter_int()
        self.menu()

#   -------------------------------------------------------------------------------------------------------------------#

