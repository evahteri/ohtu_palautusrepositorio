class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        
    
    def __str__(self):
        return f"{self.name}, Team: {self.team}, Goals: {self.goals}, Assists: {self.assists}"
