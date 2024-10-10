from app.model.player import Player
from app.view.player_view import PlayerView


class PlayerController:
    @classmethod
    def add_players(cls):
        players = []
        player_files, player_text = Player.list_existing_players()
        answer = PlayerView.add_player(player_files, player_text)
        for id_ in answer:
            players.append(Player.players[id_])
        return players

    @classmethod
    def show_player_menu(cls):
        answer = True
        player_files, player_text = Player.list_existing_players()
        text = ""
        while answer:
            answer = PlayerView.select_player_for_info(player_files, player_text, text)

    @classmethod
    def create_player(cls):
        answer = PlayerView.create_player()
        player = Player()
        player.new_player(answer)
