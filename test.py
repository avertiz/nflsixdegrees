import time
import json
from player_search import Bfs

# startTime = time.time()

data = Bfs(tree_filepath='players_and_teammates.json',
    player_index_filepath = 'player_index.json',
    team_index_filepath = 'team_index.json')        

data.pretty_return(start_player="Dick Butkus", target_player="Tom Brady")
# executionTime = (time.time() - startTime)
# print(str(executionTime) + ' seconds')

print(data.output_table)
print(data.loops)

import json

file1 = open('players_and_teammates.json')
data = json.load(file1)
file1.close()
file2 = open('player_index.json')
player_index = json.load(file2)
file2.close()
file3 = open('team_index.json')
team_index = json.load(file3)
file3.close()

# "145": "Dick Butkus"
# "288": "Mike Ditka"
# "16949": "Mitchell Trubisky"
# "4159": "Jim McMahon"
# "14895": "Alshon Jeffery"
# "10672": "Tom Brady"

start_player="4159"
target_player="10672"

loop = 0
queue = []        
queue.append([start_player])
# while queue:


path = queue.pop(0)
node = path[-1]            
if node == target_player:
    print(path)
if target_player in data[node].keys():
    path.append(target_player)
    print(path)
loop += 1
print(loop)
for adjacent in data.get(node, []):
    new_path = list(path)
    new_path.append(adjacent)
    queue.append(new_path)
    # if loop < 50:
    #     queue.append(new_path)
    # else:
    #     queue.insert(0, new_path)

