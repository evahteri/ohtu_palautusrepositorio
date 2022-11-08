import requests
from player import Player

class PlayerReader():
    def __init__(self, url):
        self.players = []
        self.json =requests.get(url).json()
    
    def get_players(self):

        for player_dict in self.json:
            if player_dict["nationality"] == "FIN":
                player = Player(
                    name=player_dict['name'],
                    team=player_dict["team"],
                    goals=player_dict["goals"],
                    assists=player_dict["assists"]
                    )

                self.players.append(player)

        return self.players