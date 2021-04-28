import pandas as pd
import requests
from bs4 import BeautifulSoup
# all data are extracted from https://2kmtcentral.com

# open a list and a dataframe for storage
playernames = []
playerlist = pd.DataFrame(columns=['Name', 'OVR', 'POS', 'INS', 'OUT', 'PLY', 'ATH', 'DEF', 'REB',
       'Height', 'Unnamed: 10', 'Unnamed: 11', 'PS4'])

num = 0
while True:
    website = 'https://2kmtcentral.com/21/players/page/' + str(num)
    # read player data using pandas
    df = pd.read_html(website)
    df = df[0]
    playerlist = playerlist.append(df, ignore_index=True)

    # set the end of the loop
    if len(df) == 0:
        break

    # extract player names by using beautiful soup
    web = requests.get(website)
    soup = BeautifulSoup(web.content, 'lxml')
    for link in soup.find_all("a", class_="name box-link"):
        # modfify the format of the name
        name = list(link)
        name = str(name[0]) + name[1]
        name = name.replace('<strong>', '')
        name = name.replace('</strong>', '')
        name = name.rstrip()
        playernames.append(name)

    print(playerlist)
    num +=1

# delete the unrelated columns
playerlist = playerlist.drop(['Height', 'Unnamed: 10', 'Unnamed: 11', 'PS4'], axis=1)

# change the names
playerlist["Name"] = playernames

# modify the position
playerlist["POS"] = playerlist["POS"].apply(lambda x: x[:2] if ' ' in x else x)

print(playerlist)

# export the data to a csv file
playerlist.to_csv(r'playerdata.csv', index = False)
