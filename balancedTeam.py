def balanced(arr,size):
    arr.sort()
    left =0
    right = 1
    maxLen = 0
    while  right < size:
        if arr[right] - arr[left] > 5:
            left += 1
            
        maxLen = max(maxLen, right -left+1)
        right += 1
    if size == 1:
        maxLen = 1
    print(maxLen)
size= int(input())
lists = list(map(int,input().split()))
balanced(lists,size)
