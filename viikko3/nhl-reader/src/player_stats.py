from player import Player

class PlayerStats():

    def __init__(self, reader):
        self.players = reader

    
    def _get_points(self, player):
        return player.goals + player.assists

    def top_scorers_by_nationality(self, nationality):
        player_by_nationality = []

        for player_dict in self.players:

            if player_dict["nationality"] == nationality:
                player = Player(
                    name=player_dict['name'],
                    team=player_dict["team"],
                    goals=player_dict["goals"],
                    assists=player_dict["assists"]
                    )

                player_by_nationality.append(player)
        result = sorted(player_by_nationality, key=self._get_points ,reverse=True)
        return result