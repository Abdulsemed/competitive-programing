def array(lists, size):
    posetive = [1]
    negative = [1]
    times = 1
    zeroes = [1]
    for index in range(size):
        if lists[index] > 0:
            posetive.append(lists[index])
        elif lists[index] < 0:
            negative.append(lists[index])
        else:
            zeroes.append(lists[index])
            
    if len(negative) % 2 != 0:
        negative[0] = len(negative)-2
        zeroes.append(negative.pop())
    if len(posetive) == 1:
        posetive[0] = 2
        negative[0] = len(negative) -3
        for _ in range(2):
            posetive.append(negative.pop())
    else:
        posetive[0] = len(posetive) -1
        negative[0] = len(negative) -1
    zeroes[0] = len(zeroes)-1
    for val in negative:
        print(val , end =" ")
    print(end ="\n")
    for val in posetive:
        print(val, end =" ")
    print(end ="\n")
    for val in zeroes:
        print(val, end =" ")
        
    
    
size = int(input())
lists = list(map(int, input().split(" ")))
array(lists,size)
