from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy.base.control import Choice


class MatchView:
    @classmethod
    def view_current_matches(cls, matches, status):
        matches_choices = []
        for i, match in enumerate(matches):
            if match.score_1 == 0 and match.score_2 == 0:
                player_1 = match.player_1.get_full_name()
                player_2 = match.player_2.get_full_name()
                text = player_1 + " - " + player_2
                matches_choices.append(Choice(i, text))
        if len(matches_choices) != 0:
            answer = inquirer.select(
                message=status + "Sélectionnez un match pour entrer le score:",
                choices=matches_choices
            ).execute()
            selected_player_1 = matches[answer].player_1.get_full_name()
            selected_player_2 = matches[answer].player_2.get_full_name()
            answer_winner = cls.view_select_winner(selected_player_1, selected_player_2)
            # if answer_winner:
            return answer, answer_winner
            # else:
            #     return False
        else:
            return -1, None

    @classmethod
    def view_select_winner(cls, player_1, player_2):
        answer = inquirer.select(
            message="Résultat du match:",
            choices=[
                Choice("victory_1", player_1),
                Choice("victory_2", player_2),
                Choice("draw", "Égalitée"),
                Separator(),
                Choice(False, "Annuler")
            ]
        ).execute()
        return answer
