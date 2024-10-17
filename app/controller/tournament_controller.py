from app.view.menu_view import MenuView
from app.view.tournament_view import TournamentView
from app.view.match_view import MatchView
from app.tools.inquirer_tools import InquirerTools
from app.model.tournament import Tournament
from app.controller.player_controller import PlayerController

tournament_folder = 'data/tournaments/'


class TournamentController:
    def __init__(self):
        self.tournament = Tournament()
        self.text = ""

    def main(self):
        quit_ = False
        while not quit_:
            if self.tournament and self.tournament.in_progress:
                self.tournament.save_tournament()
                self.show_ongoing_matches()
            else:
                text = ""
                if self.tournament.name:
                    text = self.describe_ended_tournament()
                    self.tournament.name = None
                quit_ = self.show_main_menu(text)

        exit()

    def show_ongoing_matches(self):
        turn, result = MatchView.view_current_matches(self.tournament.turns[-1].matches, self.status_message())
        if result and turn != -1:
            self.tournament.turns[-1].end_of_match(turn, result)
        elif turn == -1:
            self.tournament.new_turn()

    def show_main_menu(self, text=""):
        answer = MenuView.main_menu(text)
        match answer:
            case "new":
                self.create_new_tournament()
            case "load":  # TODO : show final score if ended
                self.load_tournament()
            case "show_players":
                PlayerController.show_player_menu()
            case "create_player":
                PlayerController.create_player()
            case False:
                return InquirerTools.ask_confirmation("Do you want to exit?")

    def create_new_tournament(self):
        # TODO: RECUPERATION DES DONNEES A FAIRE DANS LA VUE / fix PlayerController
        players = PlayerController.add_players()
        for player in players:
            player.score = 0
        data = TournamentView.new_tournament(players)
        self.tournament.new_tournament(data)
        self.tournament.save_tournament()

    def load_tournament(self):
        list_file = Tournament.list_existing_tournaments()
        answer = TournamentView.reload_existing_tournament(list_file)
        self.tournament.load_tournament(answer)

    def describe_ended_tournament(self):
        text = self.tournament.describe()
        text += self.status_message()

        return text

    def status_message(self):   # TODO : refacto matches
        text = self.tournament.turns[-1].name + '\n'
        status = {}
        for match in self.tournament.turns[-1].matches:
            player_1 = match[0][0].id
            score_1 = match[0][1]
            player_2 = match[1][0].id
            score_2 = match[1][1]
            if not self.tournament.is_over():
                if score_1 == 0 and score_2 == 0:
                    status[player_1] = " (Match en cours)"
                    status[player_2] = " (Match en cours)"
                elif score_1 == 1:
                    status[player_1] = " (Victoire)"
                    status[player_2] = " (Défaite)"
                elif score_2 == 1:
                    status[player_1] = " (Défaite)"
                    status[player_2] = " (Victoire)"
                else:
                    status[player_1] = " (Egalité)"
                    status[player_2] = " (Egalité)"
            else:
                status[player_1] = ""
                status[player_2] = ""

        for player in self.tournament.players:
            text += player.last_name + " " + player.first_name + ": " + str(player.score) + status[player.id] + '\n'
        text += "----------------\n"
        return text
