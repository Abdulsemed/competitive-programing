def button(arr):
    res = [arr[0]]
    sets = {arr[0]}
    size= len(arr)
    for index in range(1,size):
        if res and arr[index] == res[-1]:
            sets.remove(arr[index])
            res[-1] = " "
        elif arr[index] in sets:
            res.append(" ")
            continue
        else:
            res.append(arr[index])
            sets.add(arr[index])
    res[:] = []
    for element in sets:
        res.append(element)
    res.sort()
    print(''.join(res))
 
test = int(input())
for _ in range(test):
    lists = list(input())
    button(lists)
