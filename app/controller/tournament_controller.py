import os
from os.path import isfile, join
from app.view.menu_view import MenuView

from app.model.tournoi import Tournament
from app.model.joueur import Player

from app.controller.player_controller import PlayerController

tournament_folder = 'data/tournaments/'


class TournamentController:
    def __init__(self):
        self.view = MenuView()
        self.tournament = Tournament()

    def main(self):
        quit_ = False
        while not quit_:
            if self.tournament and self.tournament.in_progress:
                self.tournament.save_tournament()
                self.show_ongoing_matches()
            else:
                quit_ = self.show_main_menu()

        exit()

    def show_ongoing_matches(self):
        turn, result = self.view.match.view_current_matches(self.tournament.turns[-1].matches, self.status_message())
        if turn != -1:
            self.tournament.turns[-1].end_of_match(turn, result)
        else:
            self.tournament.new_turn()

    def show_main_menu(self):
        answer = self.view.main_menu()
        match answer:
            case "new":
                self.create_new_tournament()
            case "load":
                self.load_tournament()
            case "show_players":
                PlayerController.show_player_menu()
            case "create_player":
                PlayerController.create_player()
            case False:
                return self.view.tools.ask_confirmation("Do you want to exit?")

    # def show_player_menu(self):
    #     answer = True
    #     text = ""
    #     while answer:
    #         answer = self.view.player.select_player_for_info(text)
    #         if answer:
    #             text = Player.describe(answer)

    # def add_players(self):
    #     players = []
    #     player_files, player_text = Player.list_existing_players()
    #     answer = self.view.player.add_player(player_files, player_text)
    #     for id_ in answer:
    #         players.append(Player.players[id_])
    #     return players

    def create_new_tournament(self):
        # TODO: RECUPERATION DES DONNEES A FAIRE DANS LA VUE / fix PlayerController
        players = PlayerController.add_players()
        for player in players:
            player.score = 0
        data = self.view.tournament.new_tournament(players)  # player_files, player_text)

        # player_files, player_text = Player.list_existing_players()
        # data = self.view.new_tournament(player_files, player_text)

        self.tournament.new_tournament(data)
        self.tournament.save_tournament()

    def load_tournament(self):
        list_file = Tournament.list_existing_tournaments()
        answer = self.view.tournament.reload_existing_tournament(list_file)
        self.tournament.load_tournament(answer)
        # if self.tournament.current turn < self.tournament.max_turn
        #   go there
        #   state = during turn

    def status_message(self):
        text = self.tournament.turns[-1].name + '\n'
        for player in self.tournament.players:
            text += player.last_name + " " + player.first_name + ": " + str(player.score) + '\n'
        text += "----------------\n"
        return text


