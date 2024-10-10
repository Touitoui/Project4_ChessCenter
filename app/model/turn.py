from datetime import datetime


class Turn:
    def __init__(self, name, matches):
        self.name = name
        self.start_time = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        self.end_time = None
        self.matches = matches

    def end_turn(self):
        self.end_time = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        for match in self.matches:
            for player, score in match:
                player.add_score(score)

    def end_of_match(self, match_number, result):
        match result:
            case "victory_1":
                self.matches[match_number][0][1] = 1
            case "victory_2":
                self.matches[match_number][1][1] = 1
            case _:
                self.matches[match_number][0][1] = 0.5
                self.matches[match_number][1][1] = 0.5

    def show_score(self, match_id):
        selected_match = self.matches[match_id]
        return (selected_match[0][0].get_full_name() + ":" + str(selected_match[0][1])
                + "\n" + selected_match[1][0].get_full_name() + ":" + str(selected_match[1][1]))
        # return self.matches[match_id].describe()
