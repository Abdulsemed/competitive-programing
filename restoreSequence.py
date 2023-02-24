def whiteboard(arr,size):
    left = 0
    right = size-1
    newArr = [0]*(size)
    pointer = 0
    flag = True
    while left <= right:
        if flag:
            newArr[pointer] = arr[left]
            left += 1
        else:
            newArr[pointer] = arr[right]
            right -= 1
        pointer += 1
        flag = not flag
    print(*newArr)
tests = int(input())
for _ in range(tests):
    size = int(input())
    lists = list(input().split(" "))
    whiteboard(lists,size)
