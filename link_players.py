import pandas as pd
import json

def main(data, json_filename):    

    players = data['player'].unique().tolist()

    players_dict = {}

    for player in players:

        teams = data[data['player'] == player][['team','year']].values.tolist()
        teams_and_teammates = []

        for team in teams:
            teams_and_teammates.append(data[(data['player'] != player) & 
                                (data['team'] == team[0]) &
                                (data['year'] == team[1])].values.tolist())

        player_dict = {}
        for team in teams_and_teammates:
            for teammate in team:
                if teammate[0] not in player_dict.keys():
                    player_dict[teammate[0]] = [[teammate[2], teammate[3]]]
                else:
                    player_dict[teammate[0]].append([teammate[2], teammate[3]])
        
        players_dict[player] = player_dict

    with open(json_filename, "w") as file: 
        json.dump(players_dict, file)    

if __name__ == '__main__':
    data = pd.read_csv('pos_player.csv')
    main(data = data, json_filename = 'players_and_teammates.json')        