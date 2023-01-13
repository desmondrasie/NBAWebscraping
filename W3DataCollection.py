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

#Global Data Lists
playerSlip = soup.find_all('div',class_='<< TAG NAME >>')
categoryValues = soup.find_all('span',class_='<< TAG NAME >>')
categoryValues = categoryValues[0::2]
odds = soup.find_all('span',class_='<< TAG NAME >>')
lock = soup.find_all('svg',class_='<< TAG NAME >>')

#class for locks
#market-btn style_button__34Zqv style_pill__1NXWo style_horizontal__10PLW style_disabled__2uBLz
#style_offline__3AUfP
tempList = []
counter = 0
for i in playerSlip:
    # print(i.text)
    if "Offline" in i.text:
        # print("|| Bet Slip Locked ||")
        continue
    splitTitle = i.text.split("(")
    categoryName = splitTitle[1]
    categoryName = categoryName[:-1]
    if categoryName not in ('Points','Rebounds','Assists','3 Point FG','Double+Double','Blocks','Turnovers','Pts+Rebs+Asts','Steals+Blocks'):
        # print("Category Filtered:",categoryName)
        counter = counter + 1
        continue
    # print("Counter is at:",counter)
    playerName = splitTitle[0]
    playerName = playerName.replace(".","")
    playerName = playerName[:-1]
    tempList.append(playerName)
    valueList = categoryValues[counter].text.split(" ")
    value = valueList[1]
    tempList.append(value)
    tempList.append(odds[counter*2].text)
    tempList.append(odds[counter*2+1].text)
    # print(tempList)
    appendTo(categoryName,tempList)
    tempList = []
    counter = counter + 1

masterNames = ["Points","Assists","Rebounds","Turnovers","Blocks","ThreePoint","Double+Double","P+A+R","S+B"]
master = [Points,Assists,Rebounds,Turnovers,Blocks,ThreePoint,DoubleD,PARs,SBs]
masterClone = copy.deepcopy(master)

def printData():
    print("-----------------------------------------------------------------------------------------------------------------")
    print("|| PIN Data ||")
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