from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy.base.control import Choice
from app.view.tournament_view import TournamentView


class MenuView:
    def __init__(self):
        self.tournament = TournamentView

    @classmethod
    def main_menu(cls, text=""):
        answer = inquirer.select(
            message=text + "Bienvenue:",
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
