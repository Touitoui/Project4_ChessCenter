from datetime import datetime


class Turn:
    def __init__(self, name, matches):
        self.name = name
        self.start_time = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        self.end_time = None
        self.matches = matches

    def end_turn(self):
        self.end_time = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        # Apply scores for all matches in the turn
        for match in self.matches:
            match.apply_score()

    def end_of_match(self, match_number, result):
        match result:
            case "victory_1":
                self.matches[match_number].score_1 = 1
                self.matches[match_number].score_2 = 0
            case "victory_2":
                self.matches[match_number].score_1 = 0
                self.matches[match_number].score_2 = 1
            case _:  # Draw case
                self.matches[match_number].score_1 = 0.5
                self.matches[match_number].score_2 = 0.5

    def show_score(self, match_id):
        selected_match = self.matches[match_id]
        return (selected_match.player_1.get_full_name() + ":" + str(selected_match.score_1)
                + "\n" + selected_match.player_2.get_full_name() + ":" + str(selected_match.score_2))
        # return self.matches[match_id].describe()
