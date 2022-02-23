peopleList = []
peopleMap = {}
peopleReverseMap = {}
sequenceNumber = int(97)
activities = []
allCheck = {}
sumCheck = {}
while(True):
    people = str(input("添加成员："))
    if(people == ''):
        break
    if(people in peopleList):
        print(str(people) + " 已存在，请重新输入。")
        continue
    else:
        peopleMap[chr(sequenceNumber)] = people
        peopleReverseMap[people] = chr(sequenceNumber)
        sequenceNumber+=1
        peopleList.append(people)
        
print("成员已添加完毕：")
print(peopleList)
print("\n")

while(True):
    exceptPeopleList = []
    people = str(input("活动的支付人："))
    if(people == ''):
        break
    if(people not in peopleList):
        print("支付人不在成员名单内，请重新输入。")
        continue
    while(True):
        exceptPeople = str(input("谁没参与："))
        if(exceptPeople == ''):
            break
        if(exceptPeople not in peopleList):
            print("支付人不在成员名单内，请重新输入。")
            continue
        else:
            exceptPeopleList.append(exceptPeople)
            print("本次活动 " + exceptPeople + " 已被剔除扣费。")
        
    costMoney = int(input("活动的支付金额："))
    if( costMoney < 1 ):
        print("输入的支付金额不合法，请重新输入。。")
        continue
    
    activities.append(str(people)+ "\t支付了:\t" + str(costMoney))

    for theOne in peopleList:
        if((theOne == people) or (theOne in exceptPeopleList)):
            continue
        if(str(peopleReverseMap[theOne]+peopleReverseMap[people]) in allCheck.keys()):
            allCheck[peopleReverseMap[theOne]+peopleReverseMap[people]] += costMoney / (len(peopleList)-len(exceptPeopleList))
        else:
            allCheck[peopleReverseMap[theOne]+peopleReverseMap[people]] = costMoney / (len(peopleList)-len(exceptPeopleList))
# print(allCheck)
for activity in activities:
    print(str(activity))

allCheckList = list(allCheck.items())

for check in allCheckList:
    flag = 0
    debt = check[0]
    reverseDebt = ''.join(reversed(debt))
    for tempCheck in allCheckList:
        tempDebt = tempCheck[0]
        if(str(reverseDebt) == str(tempDebt)):
            flag = 1
            allCheckList.remove(tempCheck)
            money = check[1]
            tempMoney = tempCheck[1]
            if(money > tempMoney):
                sumCheck[debt] = money - tempMoney
            elif(money < tempMoney):
                sumCheck[reverseDebt] = tempMoney - money
            break
    if(flag):
        pass
    else:
        sumCheck[check[0]] = check[1]
        
    
print("结账：")    
# print(sumCheck)
for people in peopleList:
    needPaySum = 0
    print(str(people)+": ")
    for key,money in sumCheck.items():
        if(str(peopleReverseMap[people]) == str(key[0])):
            needPaySum+=money
            print("--> "+str(peopleMap[key[1]])+" "+str(money))
    print("共需： "+str(needPaySum))