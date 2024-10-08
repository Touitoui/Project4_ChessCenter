import random
import json
from app.controller.tournament_controller import TournamentController
from app.tools.utils import create_folder


folders = {
    "data": "data",
    "players": "data/players/",
    "tournaments": "data/tournaments/",
}


def main():
    for folder in folders:
        create_folder(folder)
    # TODO: cleanup tool, reports
    # TODO: Support de presentation
    controller = TournamentController()
    controller.main()


if __name__ == '__main__':
    main()
