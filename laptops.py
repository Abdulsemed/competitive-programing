def alex(arr, size):
    flag = False
    arr.sort()
    for index in range(size-1):
        if arr[index][0] < arr[index+1][0] and arr[index+1][1] < arr[index][1]:
            flag = True
            break
        elif arr[index][0] > arr[index+1][0] and arr[index+1][1] > arr[index][1]:
            flag = True
            break
    if flag:
        print("Happy Alex")
    else:
        print("Poor Alex")
    
size = int(input())
lists = []
for _ in range(size):
    lists.append(list(map(int, input().split(" "))))
alex(lists, size)
