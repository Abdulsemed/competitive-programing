def shortest(arr, size):
    minLength = size+1
    left = 0
    right = 0
    sets = set()
    arrDict = {}
    set1 = {"1", "2", "3"}
    while right <= size:
        while sets == set1 and minLength != 3:
            minLength = min(minLength, right -left)
            arrDict[arr[left]] -= 1
            if arrDict[arr[left]] == 0:
                sets.remove(arr[left])
            left += 1
        if minLength == 3:
            break
        elif right == size:
            break
        elif arr[right] not in sets:
            sets.add(arr[right])
        arrDict[arr[right]] = 1 + arrDict.get(arr[right], 0)
        right += 1
    print(minLength if minLength != size+1 else 0)    
test = int(input())
for _ in range(test):
    lists = list(input())
    size = len(lists)
    shortest(lists, size)
