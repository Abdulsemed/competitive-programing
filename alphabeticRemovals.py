def polycarp(size, k, letters):
    lists = []
    for index in range(size):
        lists.append((letters[index], index))
        
    lists.sort()
    lists[:] = lists[k:]
    lists.sort(key= lambda lis: lis[1])
    print(''.join([char[0] for char in lists]))
 
size, k = map(int, input().split())
letters = input()
polycarp(size,k,letters)
