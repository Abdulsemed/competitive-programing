from collections import defaultdict
def indexes(aList, bList):
    bSet = set(bList)
    indexDict = defaultdict(list)
    for index, elements in enumerate(aList):
        if elements in bSet:
            indexDict[elements].append(index+1)
    for elements in bList:
        for value in indexDict[elements]:
            print(value, end = " ")
        if not indexDict[elements]:
            print(-1)
        else:
            print()
    
    
aSize, bSize= map(int,input().split(" "))
left = 0
aList = []
bList = []
bSize += aSize
while left < bSize:
    if left < aSize:
        aList.append(input())
    else:
        bList.append(input())
    left += 1
        
indexes(aList, bList)
