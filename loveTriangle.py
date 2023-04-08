from collections import defaultdict
def triangle(arr,size):
    flag = False
    for index in range(size):
        curr = arr[index]
        if arr[index] != index:
            val = arr[arr[index]-1]
            j = arr[index]-1
            count = 0
            while curr != val and count < 3:
                if val-1 != j:
                    j = val-1
                    val = arr[val-1]
                else:
                    break
                count += 1
        if val == curr and count == 2:
            flag = True
            break

    if flag:
        print("YES")
    else:
        print("NO")

size= int(input())
arr = list(map(int,input().split()))
triangle(arr,size)