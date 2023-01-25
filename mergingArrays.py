def mergingArrays(arr1,arr2,size1,size2):
    left1 = 0
    left2 = 0
    result = []
    while left1 < size1 and left2 < size2:
        if arr1[left1] < arr2[left2]:
            result.append(arr1[left1])
            left1 += 1
        else:
            result.append(arr2[left2])
            left2 += 1
    result.extend(arr1[left1:])
    result.extend(arr2[left2:])
    print(*result)
           
size1, size2 = map(int,input().split(" "))
lists = list(map(int, input().split(" ")))
lists2 = list(map(int, input().split(" ")))
mergingArrays(lists,lists2,size1,size2)
