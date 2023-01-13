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
    if name == 'Threes':
        ThreePoint.append(temp)
    if name == 'Double-Double':
        DoubleD.append(temp)
    if name == 'Blocks':
        Blocks.append(temp)
    if name == 'Turnovers':
        Turnovers.append(temp)
    if name == 'Pts, Reb & Ast':
        PARs.append(temp)
    if name == 'Steals + Blocks':
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

#Initialize Variables
tempList = []
subList = []
counter = 0
categoryBlocks = soup.find_all('div',class_='<< TAG NAME >>')
for i in categoryBlocks:
    subList = []
    categoryName = i.find_all('a',class_= '<< TAG NAME >>')
    if categoryName[0].text not in ('Points','Rebounds','Assists','Threes','Double-Double','Blocks','Turnovers','Pts, Reb & Ast','Steals + Blocks'):
        continue
    playerNames = i.find_all('span',class_='<< TAG NAME >>')
    if categoryName[0].text == "Double-Double":
        categoryValues = i.find_all('span',class_= '<< TAG NAME >>')
    else:
        categoryValues = i.find_all('span',class_= '<< TAG NAME >>')
    categoryValues = categoryValues[0::2]
    odds = i.find_all('span',class_= '<< TAG NAME >>')

#####Dealing With Empty Values in Double-Double##### START
    temporary = i.find_all(True, {'class':['<< TAG NAME >>','<< TAG NAME >>']})
    for a in temporary:
        if ('' == a.text):
            subList.append(a.text)
        elif "Yes" in a.text:
            subList.append(a.text)
        elif "No" in a.text:
            subList.append(a.text)
    while '' in subList:
        x = subList.index('')
        subList[x] = '-100000'
        del subList[x+1]
        del subList[x+1]
    alpha = 0
    for i in subList:
        x = i.replace('Yes',"")
        x = x.replace('No','')
        subList[alpha] = x
        alpha = alpha + 1
    #print(subList)
#####Dealing With Empty Values in Double-Double##### END
    for slip in categoryValues:
        name = playerNames[counter].text
        name = name.replace(".","")
        tempList.append(name)
        if categoryName[0].text != "Double-Double":
            tempList.append(slip.text)
            odds1 = odds[counter*2].text
            odds2 = odds[counter*2+1].text
        else:
            tempList.append('0.5')
            odds1 = subList[counter*2]
            odds2 = subList[counter*2+1]

        odds1 = odds1.replace("−","-")
        tempList.append(odds1)
        odds2 = odds2.replace("−","-")
        tempList.append(odds2)
        appendTo(categoryName[0].text,tempList)
        tempList = []
        counter = counter + 1
    counter = 0
masterNames = ["Points","Assists","Rebounds","Turnovers","Blocks","ThreePoint","Double+Double","P+A+R","S+B"]
master = [Points,Assists,Rebounds,Turnovers,Blocks,ThreePoint,DoubleD,PARs,SBs]
masterClone = copy.deepcopy(master)

def printData():
    print("-----------------------------------------------------------------------------------------------------------------")
    print("|| DK Data ||")
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
#printData()

