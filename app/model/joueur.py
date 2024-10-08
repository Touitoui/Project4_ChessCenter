import json
import jsonpickle
import os
from os.path import isfile, join

player_folder = 'data/players/'

# from datetime import date
#
#
# def calculate_age(born):
#     today = date.today()
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class Player:
    players = {}
    next_id = 0

    def __init__(self):  # , file_name):  # last_name, first_name, birthdate, club_id=0):
        self.id = 0
        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.club_id = None
        self.score = 0
        # self._load_player(file_name)

    def new_player(self, data):
        self.id = self.next_id
        self.next_id += 1
        self.last_name = data["last_name"]
        self.first_name = data["first_name"]
        self.birthdate = data["birthdate"]
        self.club_id = data["club_id"]

        self.players[self.id] = self
        self.save_player()

    def add_score(self, score):
        self.score += score

    def load_player(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.id = data["id"]
            self.last_name = data["last_name"]
            self.first_name = data["first_name"]
            self.birthdate = data["birthdate"]
            self.club_id = data["club_id"]

    def save_player(self):
        data = {"id": self.id,
                "last_name": self.last_name,
                "first_name": self.first_name,
                "birthdate": self.birthdate,
                "club_id": self.club_id}
        path = os.path.join(player_folder, str(self.id) + ".json")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_details(self):
        return [value for attr, value in vars(self).items() if not callable(value) and not attr.startswith("__")]

    def get_full_name(self):
        return self.last_name + " " + self.first_name

    @classmethod
    def describe(cls, id_):
        player = cls.players[id_]
        text = "ID: " + str(id_) + '\n'
        text += "Nom: " + player.last_name + '\n'
        text += "Prénom: " + player.first_name + '\n'
        text += "Age: " + "" + " (" + player.birthdate + ")\n"  # TODO: Age
        text += "ID Club: " + player.club_id + '\n'
        return text

    @classmethod
    def get_loaded_players(cls):
        return cls.players

    @classmethod
    def list_existing_players(cls):
        # player_files = [f for f in os.listdir(player_folder) if isfile(join(player_folder, f))]
        player_id = list(cls.players.keys())
        player_text = []
        for id_ in player_id:
            player_text.append(cls.players[id_].last_name + " " + cls.players[id_].first_name)
        return player_id, player_text

    @classmethod
    def load_all_players(cls):
        player_files = [f for f in os.listdir(player_folder) if isfile(join(player_folder, f))]
        player_text = []
        for player in player_files:
            player_id = int(player.replace('.json', ''))
            if player_id >= cls.next_id:
                cls.next_id = player_id + 1
            file_path = os.path.join(player_folder, player)
            cls.players[player_id] = Player()
            cls.players[player_id].load_player(file_path)

    @classmethod
    def use_next_id(cls):
        id_ = cls.next_id
        cls.next_id += 1
        return id_


Player.load_all_players()
