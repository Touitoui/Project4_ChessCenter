# TODO: refacto usage
class Match:
    def __init__(self, player_1, player_2):
        # self.pair = ([player_1, 0], [player_2, 0])
        # self.id =
        self.player_1 = player_1
        self.player_2 = player_2
        self.id_1 = self.player_1.id
        self.id_2 = self.player_2.id
        self.score_1 = 0
        self.score_2 = 0

    def apply_score(self):
        self.player_1.score += self.score_1
        self.player_2.score += self.score_2

    def describe(self):
        return (self.player_1.get_full_name() + ":" + str(self.score_1)
                + "\n" + self.player_2.get_full_name() + ":" + str(self.score_2))
