from player.model import Player
from player.view import Sub_Choice
import sys

# ---------------------------------------------------------------------------------------------------------------------#


class PlayerMenu:

    def sub_menu(self):
        sub_choice = Sub_Choice()
        player = Player()

        try:
            resultat = int(sub_choice.sub_main_choice())
        except:
            sub_choice.print_error_enter_int()
            self.sub_menu()

        # Ajouter un joueur.
        if resultat == 1:
            player.save_player()

        # modifier un joueur.
        elif resultat == 2:
            player.add_tournament()

        # Supprimmer un joueur.
        elif resultat == 3:
            player.delete_player()

        # Affichage des joueurs.
        elif int(resultat) == 4:
            player.search_player()

        # Supprimmer tous les joueurs.
        elif int(resultat) == 5:
            player.delete_all_player()

        # Retour au menu principal
        elif resultat == 6:
            print('Retour au menu principal')
            return

        # sortir du logiciel
        elif resultat == 7:
            print('Merci pour  votre visite')
            exit()

        else:
            sub_choice.print_error_enter_int()
        print('-------------------------------------------------------------------------------------------------------')
        self.sub_menu()
