def cardGame(arr,size):
    wube = 0
    heni  = 0
    left = 0
    right= size-1
    iterator = 0
    flag = True
    while left <= right:
        if flag:
            if arr[right] > arr[left]:
                wube += arr[right]
                right -= 1
            else:
                wube += arr[left]
                left += 1
        else:
            if arr[right] > arr[left]:
                heni += arr[right]
                right -= 1
            else:
                heni += arr[left]
                left += 1
        flag = not flag
 
    print(wube, heni)
 
size = int(input())
lists = list(map(int,input().split()))
cardGame(lists,size)
