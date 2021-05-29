# Making an index to speed everything up

import json
import pandas as pd

def main():
    
    data = pd.read_csv('pos_player.csv', dtype=str)
    data['new_id'] = None
    id_num = 0
    index = {}
    original_id_tracker = []
    for i, r in data.iterrows():
        if r['id'] not in original_id_tracker:
            index[id_num] = r['player']
            original_id_tracker.append(r['id'])
            data.at[i, 'new_id'] = id_num
            id_num += 1            
        else:
            new_id = data.loc[data['id'] == r['id'], 'new_id'].values[0]
            data.at[i, 'new_id'] = new_id
        if i % 1000 == 0:
            print(str(i) + ' rows complete')
    with open('player_index.json', "w") as file: 
        json.dump(index, file)
    data.to_csv('pos_player.csv', index=False)

if __name__ == '__main__':
    main()