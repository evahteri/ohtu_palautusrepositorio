class TennisGame:
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

    def tie(self):
        tie_table = {0:"Love-All", 1: "Fifteen-All", 2: "Thirty-All", 3: "Forty-All"}

        if self.player1_score not in [0,1,2,3]:
            return "Deuce"
    
        return tie_table[self.player1_score]
    

    def advantage(self):
        point_difference = self.player1_score - self.player2_score

        if point_difference == 1:
            return "Advantage player1"
        if point_difference == -1:
            return "Advantage player2"
        if point_difference >= 2:
            return "Win for player1"
        if point_difference <= -2:
            return "Win for player2"
        

    def get_score(self):
        score = ""
        score_table = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

        if self.player1_score == self.player2_score:
            score = self.tie()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.advantage()

        else:
            score = f"{score_table[self.player1_score]}-{score_table[self.player2_score]}"

        return score
