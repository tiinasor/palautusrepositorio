from player import Player
import requests

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = [Player(d) for d in response]

    print("Players from FIN:\n")
    for p in players:
        if p.nationality == 'FIN':
            print(p)

if __name__ == "__main__":
    main()
