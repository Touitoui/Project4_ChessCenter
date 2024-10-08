from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy.base.control import Choice
from app.tools.InquirerTools import InquirerTools


class TournamentView:
    @classmethod
    def reload_existing_tournament(cls, tournament_list):
        tournament_list.append(Choice("return", "Retour"))
        answer = inquirer.select(
            message="Quel tournoi charger?:",
            choices=tournament_list
        ).execute()
        return answer

    @classmethod
    # def new_tournament(self, player_files, player_text):
    def new_tournament(cls, players):
        # players = self.add_player(player_files, player_text)
        data = {
            "players": players,
            "name": InquirerTools.prompt_text("Nom du tournoi:"),
            "location": InquirerTools.prompt_text("Adresse:"),
            "start": InquirerTools.prompt_text("Debut:"),  # GERER VALIDATION
            "end": InquirerTools.prompt_text("Fin:"),  # GERER VALIDATION
            "description": InquirerTools.prompt_text("Description du tounoi:"),
            "current_turn": 1,
            "number_of_turns": InquirerTools.prompt_int("Nombre de tours:", 4)
        }
        return data