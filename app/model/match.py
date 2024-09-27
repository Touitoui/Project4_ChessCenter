class Match:
    def __init__(self, player_1, player_2):
        # self.pair = ([player_1, 0], [player_2, 0])
        # self.id =
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_score = 0
        self.player_2_score = 0

    def describe(self):
        return (self.player_1.get_full_name() + ":" + str(self.player_1_score)
                + "\n" + self.player_2.get_full_name() + ":" + str(self.player_2_score))
