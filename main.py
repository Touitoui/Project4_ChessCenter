from app.controller.tournament_controller import TournamentController
from app.tools.utils import create_folder


folders = {
    "data": "data",
    "players": "data/players/",
    "tournaments": "data/tournaments/",
}

# TODO: Support de presentation
# TODO: reports (save to file, tournament info)
# TODO: match refacto
# TODO: end match (+ show score when reload ended match)
# TODO: README


def main():
    for x in folders:
        create_folder(folders[x])
    controller = TournamentController()
    controller.main()


if __name__ == '__main__':
    main()
