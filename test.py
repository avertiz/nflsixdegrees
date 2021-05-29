import time
import json
from player_search import Bfs

startTime = time.time()

data = Bfs(tree_filepath='players_and_teammates_new.json',
    player_index_filepath = 'player_index.json',
    team_index_filepath = 'team_index.json')

# data.bfs(start_player="16949", target_player="10672")

executionTime = (time.time() - startTime)
print(str(executionTime) + ' seconds')


# file1 = open('players_and_teammates_new.json', 'r')
# data = json.load(file1)
# file1.close()
# file2 = open('player_index.json', 'r')
# player_index = json.load(file2)
# file2.close()
# file3 = open('team_index.json', 'r')
# team_index = json.load(file3)
# file3.close()