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
                return
            if target_player in self.data[node].keys():
                path.append(target_player)
                self.path = path
                return
            for adjacent in self.data.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    def pretty_return(self, path):
        pretty_list = []
        for player in range(len(path)):
            if path[player] == path[-1]:
                self.pretty_list = pretty_list
                return
            else:
                pretty_list.append(
                    [path[player],
                     self.data[path[player]][path[player + 1]][0],
                     path[player + 1]]
                )
                

data = Bfs(json_filepath = 'players_and_teammates.json')

return_object = data.bfs(start_player='Mitchell Trubisky', target_player='Alshon Jeffery')

pretty_list = data.pretty_return(path = path)

print(test.bfs(start_player='Mitchell Trubisky', target_player='Alshon Jeffery'))

# Walter Payton
# Patrick Mahomes


# def bfs(self, start_player, target_player):

file = open('players_and_teammates.json')
data = json.load(file)
file.close()

start_player = 'Mitchell Trubisky'
target_player = 'Alshon Jefferey'

queue = []        
queue.append([start_player])
# while queue:            
path = queue.pop(0)            
node = path[-1]            
if node == target_player:
    print('Found')
    # return path  
if target_player in data[node].keys():
    print('Found')

for adjacent in data.get(node, []):
    new_path = list(path)
    new_path.append(adjacent)
    queue.append(new_path)