class Match:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.id_1 = self.player_1.id
        self.id_2 = self.player_2.id
        self.score_1 = None
        self.score_2 = None

    def apply_score(self):
        self.player_1.score += self.score_1
        self.player_2.score += self.score_2

    def describe(self):
        if not self.score_1:
            status_1 = " (Match en cours)"
            status_2 = " (Match en cours)"
        elif self.score_1 == 1:
            status_1 = " (Victoire)"
            status_2 = " (Défaite)"
        elif self.score_1 == 0:
            status_1 = " (Défaite)"
            status_2 = " (Victoire)"
        else:
            status_1 = " (Égalité)"
            status_2 = " (Égalité)"
        text = (self.player_1.get_full_name() + status_1
                + " - " + self.player_2.get_full_name() + status_2 + '\n')
        return text
