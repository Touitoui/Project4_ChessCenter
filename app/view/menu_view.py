from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy.base.control import Choice
from app.tools.inquirer_tools import InquirerTools
from app.view.tournament_view import TournamentView
from app.view.player_view import PlayerView
from app.view.match_view import MatchView


class MenuView:
    def __init__(self):
        self.tournament = TournamentView
        # self.player = PlayerView
        # self.match = MatchView
        # self.tools = InquirerTools

    @classmethod
    def main_menu(cls):
        answer = inquirer.select(
            message="Bienvenue:",
            choices=[
                Choice("new", "Nouveau tournoi"),
                Choice("load", "Charger tournoi"),
                Separator(),
                Choice("show_players", "Afficher les joueurs"),
                Choice("create_player", "Créer joueur"),
                Separator(),
                Choice(False, "Quitter")
            ]
        ).execute()
        return answer
