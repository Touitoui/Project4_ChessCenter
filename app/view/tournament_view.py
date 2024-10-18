from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from app.tools.inquirer_tools import InquirerTools


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
    def new_tournament(cls, players):
        data = {
            "players": players,
            "name": InquirerTools.prompt_text("Nom du tournoi:"),
            "location": InquirerTools.prompt_text("Adresse:"),

            "start": InquirerTools.prompt_date("Debut (HH:MM JJ/MM/AAAA):", "datetime"),
            "end": InquirerTools.prompt_date("Fin (HH:MM JJ/MM/AAAA):", "datetime"),
            "description": InquirerTools.prompt_text("Description du tounoi:"),
            "current_turn": 1,
            "number_of_turns": InquirerTools.prompt_int("Nombre de tours (Défaut: 4):", 4)
        }
        return data

    # Reports
    @classmethod
    def select_tournament_for_info(cls, tournaments_files, text=""):
        tournament_choice = []
        for file in tournaments_files:
            tournament_choice.append(Choice(file, file))
        # tournament_choice = []
        # for i, tournament in enumerate(tournaments_list):
        #     tournament_choice.append(Choice(tournament, tournaments_text[i]))
        InquirerTools.sort_choices(tournament_choice)
        tournament_choice.append(Choice(False, "Retour"))
        answer = inquirer.select(
            message=text + "Liste des tournois:",
            choices=tournament_choice,
        ).execute()
        return answer

    @classmethod
    def choose_option_info(cls, text=""):
        answer = inquirer.select(
            message=text + "Bienvenue:",
            choices=[
                Choice("name_date", "Info du tournoi"),
                Choice("list_players", "Liste des joueurs"),
                Choice("match_recap", "Résumé du match"),
                Choice(False, "Quitter")
            ]
        ).execute()
        return answer

