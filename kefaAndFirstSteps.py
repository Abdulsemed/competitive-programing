def kefa(arr,size):
    maxLen = 0
    left = 0
    right = 1
    while right < size:
        if arr[right-1] > arr[right]:
            left = right
        maxLen = max(maxLen, right - left +1)
        right += 1
    if size == 1:
        maxLen = 1   
    print(maxLen)
 
size = int(input())
lists = list(map(int,input().split()))
kefa(lists,size)
