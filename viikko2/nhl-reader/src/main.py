from player import Player
import requests

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = [Player(d) for d in response]


    fin_players = list(filter(lambda pl: pl.nationality == 'FIN', players))

    fin_sorted = sorted(fin_players, key=lambda pl: pl.goals + pl.assists, reverse=True)

    print("Players from FIN\n")

    for p in fin_sorted:
        points = p.goals + p.assists
        print(f"{p.name:<20} {p.team:<15} {p.goals:>2} + {p.assists:>2} = {points}")

if __name__ == "__main__":
    main()
