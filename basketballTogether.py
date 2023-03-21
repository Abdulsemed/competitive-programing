def basketball(arr,enemy,size):
    arr.sort()
    left = 0
    right = size-1
    currSum = 0
    count = 0
    while left < right:
        if arr[right] > enemy:
            count += 1
            right -= 1
        else:
            currSum = arr[right]
            while left < right and currSum <= enemy:
                left += 1
                currSum += arr[right]
            if currSum > enemy:
                count += 1
                right -= 1
    if left == right and arr[right] > enemy:
        count += 1
                
    print(count)

size,enemy = map(int,input().split(" "))
arr = list(map(int,input().split()))
basketball(arr,enemy,size)
