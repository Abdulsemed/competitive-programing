def rectangles(size,arr):
    arr.sort()
    area = arr[0] * arr[-1]
    left= 1
    right = (4*size)-2
    flag = True
    count = 1
    while left < right:
        if arr[left] * arr[right] != area:
            flag = False
            break
        elif count == 1 and (arr[left] != arr[left-1] or arr[right] != arr[right+1]):
            flag = False
            break
        elif count == 1:
            count = 0
        else:
            count = 1
        left += 1
        right -= 1
    if flag:
        print("YES")
    else:
        print("NO")

tests = int(input())
for _ in range(tests):
    size = int(input())
    arr= list(map(int,input().split()))
    rectangles(size,arr)
