import copy
from bs4 import BeautifulSoup

with open('<< LOCAL DIRECTORY >>', 'r', encoding='utf-8', errors='ignore') as fp:
    soup = BeautifulSoup(fp, 'lxml')

def appendTo (name,temp):
    if name == 'Points':
        Points.append(temp)
    if name == 'Rebounds':
        Rebounds.append(temp)
    if name == 'Assists':
        Assists.append(temp)
    if name == '3 Point FG':
        ThreePoint.append(temp)
    if name == 'Double+Double':
        DoubleD.append(temp)
    if name == 'Blocks':
        Blocks.append(temp)
    if name == 'Turnovers':
        Turnovers.append(temp)
    if name == 'Pts+Rebs+Asts':
        PARs.append(temp)
    if name == 'Steals+Blocks':
        SBs.append(temp)

#Initialize Category Lists
Points = [] #1
Assists = [] #2
Rebounds = [] #3
Turnovers = [] #4
Blocks = [] #5
ThreePoint = [] #6
DoubleD = [] #7
PARs = [] #8
SBs = [] #9

playerNames = soup.find_all('div', class_= '<< TAG NAME >>')
cat_values = soup.find_all('span', class_= '<< TAG NAME >>')
odds = soup.find_all('span', class_= '<< TAG NAME >>')
tags = soup.find_all('div', class_= '<< TAG NAME >>')
dubs = soup.find_all('span', class_= '<< TAG NAME >>')

categoryLengths = []

for tag in tags:
    #print(tag.text)
    list_of_players = tag.find_all('div', class_= '<< TAG NAME >>')
    #print(list_of_players)
    num_of_players = len(list_of_players)
    categoryLengths.append(num_of_players)

first_six = 0
first_seven = 0
x = 0
i = 0

for i in range(9):
    if i == 6:
        first_six = x
    if i == 7:
        first_seven = x
    x = x + categoryLengths[i]

a = 0
counter = 0
counter2 = 0
dub_count = 0
tracker = 0
index = 1
temp_list = []

for player in playerNames:
    #print(player.text)
    if tracker >= first_six and tracker < first_seven :
        if index == 7:
            temp_list.append(player.text), temp_list.append('0.5'), temp_list.append(dubs[dub_count].text), temp_list.append(dubs[dub_count+categoryLengths[counter2]].text)
            DoubleD.append(temp_list)
        temp_list = []
        # print(player.text)
        # print(0.5, dubs[dub_count].text, dubs[dub_count+categoryLengths[counter2]].text)
        dub_count = dub_count + 1
        counter = counter + 1
        tracker = tracker + 1
        if counter == categoryLengths[counter2]:

            dub_count = dub_count + categoryLengths[counter2]
            counter = 0
            counter2 = counter2 + 1
            index = index + 1
    else:
        if index == 1:
            temp_list.append(player.text), temp_list.append(cat_values[a].text), temp_list.append(odds[a].text), temp_list.append(odds[a+categoryLengths[counter2]].text)
            Points.append(temp_list)
        elif index == 2:
            temp_list.append(player.text), temp_list.append(cat_values[a].text), temp_list.append(odds[a].text), temp_list.append(odds[a+categoryLengths[counter2]].text)
            Assists.append(temp_list)
        elif index == 3:
            temp_list.append(player.text), temp_list.append(cat_values[a].text), temp_list.append(odds[a].text), temp_list.append(odds[a+categoryLengths[counter2]].text)
            Rebounds.append(temp_list)
        elif index == 4:
            temp_list.append(player.text), temp_list.append(cat_values[a].text), temp_list.append(odds[a].text), temp_list.append(odds[a+categoryLengths[counter2]].text)
            Turnovers.append(temp_list)
        elif index == 5:
            temp_list.append(player.text), temp_list.append(cat_values[a].text), temp_list.append(odds[a].text), temp_list.append(odds[a+categoryLengths[counter2]].text)
            Blocks.append(temp_list)
        elif index == 6:
            temp_list.append(player.text), temp_list.append(cat_values[a].text), temp_list.append(odds[a].text), temp_list.append(odds[a+categoryLengths[counter2]].text)
            ThreePoint.append(temp_list)
        elif index == 8:
            temp_list.append(player.text), temp_list.append(cat_values[a].text), temp_list.append(odds[a].text), temp_list.append(odds[a+categoryLengths[counter2]].text)
            PARs.append(temp_list)
        elif index == 9:
            temp_list.append(player.text), temp_list.append(cat_values[a].text), temp_list.append(odds[a].text), temp_list.append(odds[a+categoryLengths[counter2]].text)
            SBs.append(temp_list)
        temp_list = []
        a = a + 1
        counter = counter + 1
        tracker = tracker + 1
        if counter == categoryLengths[counter2]:
            a = a + categoryLengths[counter2]
            counter = 0
            counter2 = counter2 + 1
            index = index + 1

master = [Points,Assists,Rebounds,Turnovers,Blocks,ThreePoint,DoubleD,PARs,SBs]
masterClone = copy.deepcopy(master)

def printData():
    print("-----------------------------------------------------------------------------------------------------------------")
    print(masterClone[0])
    print(masterClone[1])
    print(masterClone[2])
    print(masterClone[3])
    print(masterClone[4])
    print(masterClone[5])
    print(masterClone[6])
    print(masterClone[7])
    print(masterClone[8])
    print("-----------------------------------------------------------------------------------------------------------------")
