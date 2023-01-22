def removeSmall(arr, size):
    arr.sort()
    flag = True
    for index in range(size-1):
        if arr[index+1] - arr[index] >1:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
 
tests = int(input())
for _ in range(tests):
    size = int(input())
    lists = list(map(int, input().split(" ")))
    removeSmall(lists, size)
