from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from app.tools.InquirerTools import InquirerTools


class PlayerView:
    @classmethod
    def create_player(cls):
        # players = self.add_player(player_files, player_text)
        data = {
            "last_name": InquirerTools.prompt_text("Nom de famille:"),
            "first_name": InquirerTools.prompt_text("Prénom:"),
            "birthdate": InquirerTools.prompt_text("Date de naissance:"),  # GERER VALIDATION
            "club_id": InquirerTools.prompt_text("Numéro de club:"),  # GERER VALIDATION
        }
        return data

    @classmethod  # TODO : replace by show_player_list - don't do anything when selecting, show all info in list
    def select_player_for_info(cls, player_list, player_text, text=""):
        player_choice = []
        for i, player in enumerate(player_list):
            player_choice.append(Choice(player, player_text[i]))
        InquirerTools.sort_choices(player_choice)
        player_choice.append(Choice(False, "Retour"))
        answer = inquirer.select(
            message=text + "Liste des joueurs:",
            choices=player_choice,
        ).execute()
        return answer

    @classmethod
    def add_player(cls, player_list, player_text):
        player_choice = []
        for i, player in enumerate(player_list):
            player_choice.append(Choice(player, player_text[i]))
        InquirerTools.sort_choices(player_choice)
        answer = inquirer.checkbox(
            message="Quel joueur ajouter: ([Espace] pour selectionner, [Entrer] pour valider)",
            choices=player_choice,
            transformer=lambda result: "%s choices%s selectionnés"
                                       % (len(result), "s" if len(result) > 1 else ""),
            validate=lambda result: len(result) > 1,
            invalid_message="Selectionnez au moins deux joueurs.",
        ).execute()
        return answer


