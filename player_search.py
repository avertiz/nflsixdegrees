import json

class Bfs:
    def __init__(self, json_filepath):
        file = open(json_filepath)
        self.data = json.load(file)
        file.close()

    def bfs(self, start_player, target_player):        
        queue = []        
        queue.append([start_player])
        while queue:            
            path = queue.pop(0)            
            node = path[-1]            
            if node == target_player:
                return path            
            for adjacent in self.data.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                

test = Bfs(json_filepath = 'players_and_teammates.json')
print(test.bfs(start_player='Mitchell Trubisky', target_player='Walter Payton'))