class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    DEUCE_THRESHOLD = 4
    ADVANTAGE_DIFFERENCE = 1

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.is_tied_score():
            return self.get_tied_score_text()
        elif self.is_endgame():
            return self.get_endgame_score_text()
        else:
            return self.get_regular_score_text()

    def is_tied_score(self):
        return self.player1_score == self.player2_score

    def is_endgame(self):
        return self.player1_score >= self.DEUCE_THRESHOLD or self.player2_score >= self.DEUCE_THRESHOLD

    def get_tied_score_text(self):
        tied_scores = {
            self.LOVE: "Love-All",
            self.FIFTEEN: "Fifteen-All",
            self.THIRTY: "Thirty-All"
        }
        return tied_scores.get(self.player1_score, "Deuce")

    def get_endgame_score_text(self):
        score_difference = self.get_score_difference()

        if self.has_advantage():
            return self.get_advantage_text(score_difference)
        else:
            return self.get_winner_text(score_difference)

    def get_score_difference(self):
        return self.player1_score - self.player2_score

    def has_advantage(self):
        score_difference = abs(self.get_score_difference())
        return score_difference == self.ADVANTAGE_DIFFERENCE

    def get_advantage_text(self, score_difference):
        if score_difference > 0:
            return "Advantage player1"
        else:
            return "Advantage player2"

    def get_winner_text(self, score_difference):
        if score_difference > 0:
            return "Win for player1"
        else:
            return "Win for player2"

    def get_regular_score_text(self):
        player1_text = self.convert_score_to_text(self.player1_score)
        player2_text = self.convert_score_to_text(self.player2_score)
        return f"{player1_text}-{player2_text}"

    def convert_score_to_text(self, score):
        score_names = {
            self.LOVE: "Love",
            self.FIFTEEN: "Fifteen",
            self.THIRTY: "Thirty",
            self.FORTY: "Forty"
        }
        return score_names.get(score, "")
