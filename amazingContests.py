def amazing(lists):
    maxim = lists[0]
    minm = lists[0]
    count = 0
    for index in range(1, size):
        if lists[index] < minm:
            minm = lists[index]
            count += 1
        elif lists[index] > maxim:
            maxim = lists[index]
            count += 1
    
    print(count)
 
size = int(input())
lines = list(map(int,input().split(" ")))
amazing(lines)
