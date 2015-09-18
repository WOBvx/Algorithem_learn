def Queue(LoadList):
    newList = list(LoadList) # 可以将元组Tuple eg.(1,2,4,1) 转换成列表list [1,2,4,1]
    length = len(newList)
    ResList = []
    head = 0 #创建头函数和尾函数
    tail = length-1

    while(head<tail):
        ResList.append(newList[head])
        head+=1
        newList.append(newList[head])
        tail+=1
        head+=1

    ResList.append(newList[head]) #最后补一位
    return ResList

# 测试数据：t=[6,3,1,7,5,8,9,2,4]
# 结果：6,1,5,9,4,7,2,8,3
