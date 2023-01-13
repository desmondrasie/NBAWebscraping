import time
import copy
import W1DataCollection
import W2DataCollection
import W3DataCollection

### GLOBAL VARIABLES ###
Y = 0
X = 1000
P = 0
percent = 0
counter = 0
final = []

### FUNCTIONS ###

def isArbitrage(odds1,odds2):
    odds1 = int(odds1)
    odds2 = int(odds2)
    if (odds1 + odds2) > 0:
        return False
    else:
        return True

def calcArbitrage(odds1,odds2):
    temp = []
    odds1 = int(odds1)
    odds2 = int(odds2)
    tempList = []
    if odds1 > 0:
        odds_x = (odds1/100)
    else:
        odds_x = (100/odds1)*(-1)
    if odds2 > 0:
        odds_y = (odds2/100)
    else:
        odds_y = (100/odds2)*(-1)
    Y = (X + (X*odds_x))/(1 + odds_y)
    P = (X*odds_x) - Y
    percent = (P/(X+Y))*100
    percent = round(percent,4)
    return percent

def arbData(percent,slip1,slip2,flag,counter,index):
    temp = []
    temp.append(percent)
    temp.append(slip1[0])
    temp.append(W2DataCollection.masterNames[counter])
    temp.append(slip1[1])
    if flag == "Over|Under":
        if index == 1:
            temp.append("DK over")
            temp.append(slip1[2])
            temp.append("PIN under")
            temp.append(slip2[3])
        if index == 2:
            temp.append("BET over")
            temp.append(slip1[2])
            temp.append("PIN under")
            temp.append(slip2[3])
        if index == 3:
            temp.append("DK over")
            temp.append(slip1[2])
            temp.append("BET under")
            temp.append(slip2[3])

    elif flag == "Under|Over":
        if index == 1:
            temp.append("PIN over")
            temp.append(slip2[2])
            temp.append("DK under")
            temp.append(slip1[3])
        if index == 2:
            temp.append("PIN over")
            temp.append(slip2[2])
            temp.append("BET under")
            temp.append(slip1[3])
        if index == 3:
            temp.append("BET over")
            temp.append(slip2[2])
            temp.append("DK under")
            temp.append(slip1[3])
    final.append(temp)

def sortList(final):
    final.sort(key = lambda x: x[0],reverse=True)
    return final

def isAMatch(list1,list3,counter,index):
    list2 = copy.deepcopy(list3)
    for slip1 in list1:
        print("SLIP 1",slip1)
        for slip2 in list2: #include break statement at the end for efficiency
            print("SLIP 2",slip2)
            if ((slip1[0] == slip2[0]) and (slip1[1] == slip2[1])):
                if isArbitrage(slip1[2],slip2[3]):
                    flag = "Over|Under"
                    arbData(calcArbitrage(slip1[2],slip2[3]),slip1,slip2,flag,counter,index)
                elif isArbitrage(slip1[3],slip2[2]):
                    flag = "Under|Over"
                    arbData(calcArbitrage(slip1[3],slip2[2]),slip1,slip2,flag,counter,index)
                list2.remove(slip2)
                #print("BREAK")
                break

#### MAIN FOR LOOP ####

#FIX OVER AND UNDER DEPENDING ON THE SPORTSBOOKS BEING COMPARED --> currently only Dk and Pin

def mainComparison(list1,list2,list3):
    counter = 0
    index = 1
    for category in list1.master:
        #print(category)
        isAMatch(category,list2.master[counter],counter,index)
        counter = counter + 1
    counter = 0
    index = 2
    for category in list3.master:
        isAMatch(category,list2.master[counter],counter,index)
        counter = counter + 1
    counter = 0
    index = 3
    for category in list1.master:
        isAMatch(category,list3.master[counter],counter,index)
        counter = counter + 1
    counter = 0

#### OUTPUT ####

mainComparison(W2DataCollection,W3DataCollection,W1DataCollection)

W2DataCollection.printData()
W3DataCollection.printData()
print("-----------------------------------------------------------------------------------------------------------------")
print()
if final == []:
    print("\t\t\t\t*** [No Profitable Bets Available] ***")
else:
    print("\t\t\t\t*** [Success!",len(final),"Profitable Bets Available] ***")
print()

(sortList(final)) #sort based on highest profit %
for betSlip in final:
    betSlip[0] = ""+str(betSlip[0])+" % |"
    betSlip[1] = "|"+betSlip[1]+" | "+betSlip[2]
    del betSlip[2]
    betSlip[1] = betSlip[1]+" | "+betSlip[2]+"|"
    del betSlip[2]
    betSlip[2] = "|"+betSlip[2]+" "+betSlip[3]+"|"
    del betSlip[3]
    betSlip[3] = "|"+betSlip[3]+" "+betSlip[4]+"|"
    del betSlip[4]
    print(betSlip)
    print()
