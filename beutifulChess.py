def chess(lists):
    hashTag= []
    for index in range(8):
        if lists[0][index] == "#":
            hashTag.append([0,index])
        if lists[7][index] == "#":
            hashTag.append([7,index])
    
    for index in range(1,7):
        if lists[index][0] == "#":
            hashTag.append([index, 0])
        if lists[index][7] == "#":
            hashTag.append([index,7])
 
    for index in range(1,4):
        if hashTag[0][0] - hashTag[0][1] == hashTag[index][0] - hashTag[index][1]:
            hashTag.pop(index)
            xIndex = (hashTag[0][0] - hashTag[0][1] + hashTag[1][0] + hashTag[1][1])//2
            yIndex = abs((hashTag[0][0] - hashTag[0][1]) - xIndex)
            break
        elif hashTag[0][0] + hashTag[0][1] == hashTag[index][0] + hashTag[index][1]:
            hashTag.pop(index)
            xIndex = (hashTag[0][0] + hashTag[0][1] + hashTag[1][0] - hashTag[1][1])//2
            yIndex = abs((hashTag[0][0] + hashTag[0][1]) - xIndex)
            break
    print(xIndex+1, yIndex+1)
size = int(input())
 
for _ in range(size):
    lists = []
    empty = input()
    for index in range(8):
        lists.append(input())
    chess(lists)
