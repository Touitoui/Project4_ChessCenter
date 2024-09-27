from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy.base.control import Choice


class MenuView:
    def ask_confirmation(self, question):
        answer = inquirer.confirm(
            message=question,
        ).execute()
        return answer

    def prompt_text(self, question):
        answer = inquirer.text(
            message=question,
            validate=lambda result: len(result) > 0,
            invalid_message="Input cannot be empty.",
        ).execute()
        return answer

    # GESTION CHIFFRE InquirerPy à vérifier
    def prompt_int(self, question, default_number):
        answer = inquirer.text(
            message=question,
            validate=lambda result: len(result) > 0,
            invalid_message="Input cannot be empty.",
        ).execute()
        return answer

    def add_player(self, player_list, player_text):  # TODO: tried par ordre alphabetique
        player_choice = []
        for i, player in enumerate(player_list):
            player_choice.append(Choice(player, player_text[i]))
        answer = inquirer.checkbox(
            message="Quel joueur ajouter: ([Espace] pour selectionner, [Entrer] pour valider)",
            choices=player_choice,
            transformer=lambda result: "%s choices%s selectionnés"
                                       % (len(result), "s" if len(result) > 1 else ""),
            validate=lambda result: len(result) > 1,
            invalid_message="Selectionnez au moins deux joueurs.",
        ).execute()
        return answer

    def reload_existing_tournament(self, tournament_list):
        tournament_list.append(Choice("return", "Retour"))
        answer = inquirer.select(
                message="Quel tournoi charger?:",
                choices=tournament_list
            ).execute()
        return answer

    # def new_tournament(self, player_files, player_text):
    def new_tournament(self, players):
        # players = self.add_player(player_files, player_text)
        data = {
            "players": players,
            "name": self.prompt_text("Nom du tournoi:"),
            "location": self.prompt_text("Adresse:"),
            "start": self.prompt_text("Debut:"),  # GERER VALIDATION
            "end": self.prompt_text("Fin:"),   # GERER VALIDATION
            "description": self.prompt_text("Description du tounoi:"),
            "current_turn": 1,
            "number_of_turns": self.prompt_int("Nombre de tours:", 4)
        }
        return data

    def view_current_matches(self, matches, status):
        matches_choices = []
        for i, match in enumerate(matches):
            if match[0][1] == 0 and match[1][1] == 0:
                player_1 = match[0][0].get_full_name()
                player_2 = match[1][0].get_full_name()
                text = player_1 + " - " + player_2
                matches_choices.append(Choice(i, text))
        if len(matches_choices) != 0:
            answer = inquirer.select(
                message=status + "Sélectionnez un match pour entrer le score:",
                choices=matches_choices
            ).execute()
            selected_player_1 = matches[answer][0][0].get_full_name()
            selected_player_2 = matches[answer][1][0].get_full_name()
            return answer, self.view_select_winner(selected_player_1, selected_player_2)
        else:
            return -1, None

    def view_select_winner(self, player_1, player_2):
        answer = inquirer.select(
            message="Résultat du match:",
            choices=[
                Choice("victory_1", player_1),
                Choice("victory_2", player_2),
                Choice("draw", "Égalitée"),
                Separator(),
                Choice("cancel", "Annuler")
            ]
        ).execute()
        return answer

    def main_menu(self):
        answer = inquirer.select(
            message="Bienvenue:",
            choices=[
                Choice("new", "Nouveau tournoi"),
                Choice("load", "Charger tournoi"),
                Separator(),
                Choice("show_players", "Afficher les joueurs"),  # TODO: Ajouter menu
                Choice("create_player", "Créer joueur"),  # TODO: Ajouter menu
                Separator(),
                Choice("exit", "Quitter")
            ]
        ).execute()
        return answer
