import json
import pandas as pd

class Bfs:
    def __init__(self, tree_filepath, player_index_filepath, team_index_filepath):
        file1 = open(tree_filepath)
        self.data = json.load(file1)
        file1.close()
        file2 = open(player_index_filepath)
        self.player_index = json.load(file2)
        file2.close()
        file3 = open(team_index_filepath)
        self.team_index = json.load(file3)
        file3.close()
        self.path = []
        self.output_table = pd.DataFrame()
        self.start_player = ''
        self.start_player_id = ''
        self.target_player = ''
        self.target_player_id = ''

    def get_full_player_name(self, player_id):
        player_key_list = list(self.player_index.keys())
        player_val_list = list(self.player_index.values())

        player_id_position = player_key_list.index(player_id)
        full_player_name = player_val_list[player_id_position]
        return(full_player_name)

    def get_full_team_name(self, team_abbreviation):
        team_key_list = list(self.team_index.keys())
        team_val_list = list(self.team_index.values())

        team_abbreviation_position = team_key_list.index(team_abbreviation)
        full_team_name = team_val_list[team_abbreviation_position]
        return(full_team_name)

    def player_to_index(self):
        player_key_list = list(self.player_index.keys())
        player_val_list = list(self.player_index.values())

        start_player_position = player_val_list.index(self.start_player)
        target_player_position = player_val_list.index(self.target_player)

        self.start_player_id = player_key_list[start_player_position]
        self.target_player_id = player_key_list[target_player_position]
        return(self)

    def bfs(self):  
        queue = []    
        queue.append([self.start_player_id])
        while queue:
            path = queue.pop(0)
            node = path[-1]            
            if node == self.target_player_id:
                self.path = path
                return(self)
            if self.target_player_id in self.data[node].keys():
                path.append(self.target_player_id)
                self.path = path
                return(self)
            for adjacent in self.data.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    def pretty_return(self, start_player, target_player):
        self.start_player = start_player
        self.target_player = target_player
        self.path = []
        self.player_to_index()
        self.bfs()
        table = pd.DataFrame(columns = ['player', 'team', 'teammate'])
        for player in range(len(self.path)):
            if self.path[player] == self.path[-1]:
                self.output_table = table
                return(self)
            else:
                player_name = self.get_full_player_name( self.path[player] )
                team = str( self.data[self.path[player]][self.path[player + 1]][0][1] ) +' '+ str( self.get_full_team_name( self.data[self.path[player]][self.path[player + 1]][0][0] ) )
                teammate = self.get_full_player_name( self.path[player + 1] )

                table = table.append({'player': player_name, 'team': team, 'teammate':teammate}, ignore_index = True)