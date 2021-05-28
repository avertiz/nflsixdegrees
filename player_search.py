import json

class Bfs:
    def __init__(self, json_filepath):
        file = open(json_filepath)
        self.data = json.load(file)
        file.close()
        self.path = []
        self.pretty_list = []

    def bfs(self, start_player, target_player):        
        queue = []        
        queue.append([start_player])
        while queue:            
            path = queue.pop(0)            
            node = path[-1]            
            if node == target_player:
                self.path = path
                return(self)
            if target_player in self.data[node].keys():
                path.append(target_player)
                self.path = path
                return(self)
            for adjacent in self.data.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    def pretty_return(self):
        pretty_list = []
        for player in range(len(self.path)):
            if self.path[player] == self.path[-1]:
                self.pretty_list = pretty_list
                return(self)
            else:
                pretty_list.append(
                    [self.path[player],
                     self.data[self.path[player]][self.path[player + 1]][0],
                     self.path[player + 1]]
                )