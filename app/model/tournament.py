import random
import json
import jsonpickle
from app.model.turn import Turn
from app.model.match import Match
from app.model.player import Player
import os
from datetime import datetime
from os.path import isfile, join

tournament_folder = 'data/tournaments/'


class Tournament:
    def __init__(self):
        self.name = None
        self.location = None
        self.start = None
        self.end = None
        self.players = {}
        self.description = None
        self.current_turn = None
        self.number_of_turns = None
        self.all_matches = []
        self.previous_matches = []
        self.turns = None
        self.file = None
        self.in_progress = False

    def new_tournament(self, data):
        self.name = data["name"]
        self.location = data["location"]
        self.start = data["start"]
        self.end = data["end"]
        self.players = data["players"]
        self.description = data["description"]
        self.current_turn = data["current_turn"]
        self.number_of_turns = int(data["number_of_turns"])
        self.all_matches = []
        matches = self.next_turn(self.players, random_order=True)
        self.turns = [Turn("Round 1", matches)]
        self.file = os.path.join(tournament_folder, self.name + "_"
                                 + datetime.today().strftime('%H-%M_%d-%m-%Y') + ".json")
        self.in_progress = True

    def new_turn(self):
        if self.current_turn < self.number_of_turns:
            self.turns[self.current_turn-1].end_turn()
            self.current_turn += 1
            matches = self.next_turn(self.players)
            self.turns.append(Turn("Round " + str(self.current_turn), matches))
        else:
            self.current_turn += 1
            self.in_progress = False

    def next_turn(self, players, random_order=False):
        list_matches = []
        new_pairs = []
        if random_order:
            random.shuffle(players)
            for i in range(0, len(players), 2):
                match = Match(players[i], players[i + 1])
                new_pairs.append((players[i].id, players[i+1].id))
                list_matches.append(match)
        else:
            players = sorted(players, key=lambda x: x.score, reverse=True)
            new_pairs = self.randomize_per_score(players)
            for paired in new_pairs:
                player_1 = Player.get_loaded_players()[paired[0]]
                player_2 = Player.get_loaded_players()[paired[1]]
                match = Match(player_1, player_2)
                list_matches.append(match)
        self.all_matches.append(new_pairs)
        self.previous_matches.append(list_matches)
        return list_matches

    def randomize_per_score(self, players):
        new_pairs = []
        removed_player = []

        # Will pair player with player2 if they never had a fight
        for player in players:
            if player.id not in removed_player:
                for player2 in players:
                    if player.id == player2.id:
                        continue
                    if not self.had_a_fight(player.id, player2.id) and player2.id not in removed_player:
                        new_pairs.append((player.id, player2.id))
                        removed_player.append(player.id)
                        removed_player.append(player2.id)
                        break

        # If previous pairing left some players (because they had already been paired before), pair them anyway
        if len(removed_player) < len(players):
            for player in players:
                if player.id not in removed_player:
                    for player2 in players:
                        if player.id == player2.id:
                            continue
                        if player2.id not in removed_player:
                            new_pairs.append((player.id, player2.id))
                            removed_player.append(player.id)
                            removed_player.append(player2.id)
                            break
        return new_pairs

    def had_a_fight(self, player_1, player_2):
        for previous_match in self.all_matches:
            if (player_1, player_2) in previous_match or (player_2, player_1) in previous_match:
                return True
        return False

    def save_tournament(self):
        with open(self.file, 'w', encoding='utf-8') as f:
            frozen = jsonpickle.encode(self)  #
            json.dump(frozen, f, ensure_ascii=False, indent=4)

    def load_tournament(self, tournament_file):
        file_path = os.path.join(tournament_folder, tournament_file)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            thawed = jsonpickle.decode(data)
            self.name = thawed.name
            self.location = thawed.location
            self.start = thawed.start
            self.end = thawed.end
            self.players = thawed.players
            self.description = thawed.description
            self.current_turn = thawed.current_turn
            self.number_of_turns = thawed.number_of_turns
            self.all_matches = thawed.all_matches
            self.previous_matches = thawed.previous_matches
            self.turns = thawed.turns
            self.file = thawed.file
            self.in_progress = thawed.in_progress

    def get_details(self):
        return [value for attr, value in vars(self).items() if not callable(value) and not attr.startswith("__")]

    def is_over(self):
        if self.current_turn > self.number_of_turns:
            return True
        else:
            return False

    def describe_status(self):
        text = ""
        if self.name:
            text = self.name + '\n'
            if self.current_turn > self.number_of_turns:
                text += "--Match terminé--" + '\n'
            else:
                text += "--Tour " + str(self.current_turn) + "/" + str(self.number_of_turns) + "--"

        return text

    def describe(self):
        text = ""
        text += "Nom: " + self.name + '\n'
        text += "Lieu: " + self.location + '\n'
        text += "Début-Fin: " + self.start + '-' + self.end + '\n'
        text += "Description: " + self.description + '\n'
        text += "Tour actuel: " + str(self.current_turn) + '/' + str(self.number_of_turns) + '\n'
        return text

    def describe_players(self):
        text = ""
        for player in self.players:
            text += Player.describe(player.id) + '\n'
        return text

    def describe_matches(self):
        text = ""
        for i, rounds in enumerate(self.previous_matches):
            text += "--Round " + str(i + 1) + "--\n"
            for match in rounds:
                text += match.describe()
        return text

    @classmethod
    def list_existing_tournaments(cls):
        only_files = [f for f in os.listdir(tournament_folder) if isfile(join(tournament_folder, f))]

        names = []
        for file in only_files:
            names.append(file.split('_')[0])
        return only_files, names
