def circle(arr, size):
    arr2 =[0]*size
    left = 0
    right = size -1
    flag = False
    for index in range(size):
        if flag:
            val = right
            right -= 1
        else:
            val = left 
            left += 1
        arr2[val] = arr.pop()
        flag = not flag
    flag = True
    if arr2[0] >= arr2[1] + arr2[size-1]:
        flag = False
    else:
        for index in range(1,size-1):
            if arr2[index] >= arr2[index-1] + arr2[index+1]:
                flag = False
                break
    if flag:
        print("YES")
        for element in arr2:
            print(element, end=" ")
        print(end="\n")
    else:
        print("NO")
    
size = int(input())
lists = list(map(int, input().split(" ")))
circle(sorted(lists), size)
