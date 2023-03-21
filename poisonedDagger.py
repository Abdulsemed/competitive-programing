def checker(arr,damage,mid,size):
    count = 0
    for index in range(size):
        if index != size-1:
            maxVal = min(arr[index+1] - arr[index], mid)
        else:
            maxVal = mid
        count += maxVal
    return count>= damage
def posioned(arr,size,damage):
    left = 1
    right = damage
    while left <= right:
        mid = left + (right-left)//2
        if checker(arr,damage,mid,size):
            right = mid - 1
        else:
            left = mid + 1
    print(left)

tests = int(input())
for _ in range(tests):
    size, damage = map(int, input().split())
    arr= list(map(int, input().split()))
    posioned(arr,size,damage)
