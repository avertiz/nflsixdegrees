from bs4 import BeautifulSoup
import requests
import csv

def main(YEARS_START, YEARS_END):

    TEAMS = ['arz' , 'atl', 'bal', 'buf', 'car', 'chi', 'cin', 'cle', 'dal', 'den', 'det', 'gb', 'hou', 'ind', 'jac', 'kc', 'lac', 'lam', 'mia', 'min', 'ne', 'no', 'nyg', 'nyj', 'oak', 'phi', 'pit', 'sf', 'sea', 'tb', 'ten', 'was',
    'stl', 'bos', 'pho']

    id = []
    positions = []
    players = []
    team_list_placeholder = []
    year_list_placeholder = []

    for year in range(YEARS_START, YEARS_END+1):

        for team in TEAMS:

            print(team, year)
            url = "http://www.jt-sw.com/football/pro/rosters.nsf/Annual/%s-%s" % (year, team)
            page = requests.get(url).text

            try:
                soup = BeautifulSoup(page, 'lxml')
                table = soup.find('table', attrs={'cellpadding':'4'})
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    if cols:
                        id.append(cols[3].find_all('a')[0]['href'][-8:])
                        positions.append(cols[0].string)
                        players.append(cols[3].string)
                        team_list_placeholder.append(team)
                        year_list_placeholder.append(year)
            except:
                print("Unable to get ", team, year)

    data = [id, players, positions, team_list_placeholder, year_list_placeholder]
    file = open("pos_player.csv","w+", newline='')
    with file:
        write = csv.writer(file)
        write.writerow(['id', 'player', 'pos', 'team', 'year'])
        for row in range(len(data[0])):
            text_ = [data[0][row], data[1][row], data[2][row], data[3][row], data[4][row]]
            write.writerow(text_)

if __name__ == '__main__':
    main(YEARS_START = 1970, YEARS_END = 2019)