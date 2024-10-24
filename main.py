from app.controller.tournament_controller import TournamentController
from app.tools.utils import create_folder


folders = {
    "data": "data",
    "players": "data/players/",
    "tournaments": "data/tournaments/",
}

# TODO: Support de presentation
# TODO: README


def main():
    for x in folders:
        create_folder(folders[x])
    controller = TournamentController()
    controller.main()


if __name__ == '__main__':
    main()
