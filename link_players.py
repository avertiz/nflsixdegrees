import pandas as pd
import json

def main(data, json_filename):    

    players = data['new_id'].unique().tolist()

    players_dict = {}

    for player in players:

        teams = data[data['new_id'] == player][['team','year']].values.tolist()
        teams_and_teammates = []

        for team in teams:
            teams_and_teammates.append(data[(data['new_id'] != player) & 
                                (data['team'] == team[0]) &
                                (data['year'] == team[1])].values.tolist())

        player_dict = {}
        for team in teams_and_teammates:
            for teammate in team:
                if teammate[5] not in player_dict.keys():
                    player_dict[teammate[5]] = [[teammate[3], teammate[4]]]
        
        players_dict[player] = player_dict

    with open(json_filename, "w") as file: 
        json.dump(players_dict, file)    

if __name__ == '__main__':
    data = pd.read_csv('pos_player.csv')
    main(data = data, json_filename = 'players_and_teammates.json')        