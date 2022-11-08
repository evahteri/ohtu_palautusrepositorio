import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            player = Player(
                name=player_dict['name'],
                team=player_dict["team"],
                goals=player_dict["goals"],
                assists=player_dict["assists"]
                )

            players.append(player)
    
    players.sort(key=get_points ,reverse=True)

    print("Oliot:")

    for player in players:
        print(player)

def get_points(player):
    return player.goals + player.assists

if __name__ == "__main__":
    main()