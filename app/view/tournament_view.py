from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from app.tools.inquirer_tools import InquirerTools


class TournamentView:
    @classmethod
    def reload_existing_tournament(cls, tournaments_files, tournaments_names):
        tournament_choice = []
        for i, file in enumerate(tournaments_files):
            tournament_choice.append(Choice(file, tournaments_names[i]))
        tournament_choice.append(Choice(False, "Retour"))
        answer = inquirer.select(
            message="Quel tournoi charger?:",
            choices=tournament_choice
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

    @classmethod
    def show_tournament_results(cls, tournament):
        # Print header
        print("=" * 50)
        print(f"RÉSULTATS DU TOURNOI: {tournament.name}")
        print(f"Lieu: {tournament.location}")
        print(f"Date: {tournament.start} - {tournament.end}")
        print("=" * 50)
        print()

        # Print final standings
        print("Score final:")
        print("-" * 20)
        sorted_players = sorted(tournament.players, key=lambda x: x.score, reverse=True)
        for i, player in enumerate(sorted_players):
            print(f"{i + 1}. {player.get_full_name()}: {player.score} points")
        print()

        # Print round summaries
        print("Résumé des rounds:")
        print("-" * 20)
        for turn in tournament.turns:
            print(f"\n{turn.name}")
            for match in turn.matches:
                if match.score_1 == 1:
                    result = "a gagné contre"
                elif match.score_2 == 1:
                    result = "a perdu contre"
                else:
                    result = "égalité avec"
                print(f"{match.player_1.get_full_name()} {result} {match.player_2.get_full_name()}")

        print("\n" + "=" * 50)

        # Wait for user input before continuing
        input("\nPressez entrer pour revenir au menu...")

    # Reports
    @classmethod
    def select_tournament_for_info(cls, tournaments_files, tournaments_names, text=""):
        tournament_choice = []
        for i, file in enumerate(tournaments_files):
            tournament_choice.append(Choice(file, tournaments_names[i]))
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

