import os
from os.path import isfile, join
from app.view.menu_view import MenuView
from app.model.tournoi import Tournament
from app.model.joueur import Player

tournament_folder = 'data/tournaments/'


class TournamentController:
    def __init__(self):
        self.view = MenuView()
        self.tournament = Tournament()
        # self.state = "main_menu"

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
        turn, result = self.view.view_current_matches(self.tournament.turns[-1].matches, self.status_message())
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
            case "exit":
                return self.view.ask_confirmation("Do you want to exit?")

    def add_players(self):
        players = []
        player_files, player_text = Player.list_existing_players()
        answer = self.view.add_player(player_files, player_text)
        for id_ in answer:
            players.append(Player.players[id_])
        return players

    def create_new_tournament(self):
        # RECUPERATION DES DONNEES A FAIRE DANS LA VUE
        players = self.add_players()
        data = self.view.new_tournament(players)  # player_files, player_text)

        # player_files, player_text = Player.list_existing_players()
        # data = self.view.new_tournament(player_files, player_text)

        self.tournament.new_tournament(data)
        self.tournament.save_tournament()

    def load_tournament(self):
        list_file = Tournament.list_existing_tournaments()
        answer = self.view.reload_existing_tournament(list_file)
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


