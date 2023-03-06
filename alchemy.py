def alchemy(arr,size):
    edw = 0
    alph = 0
    left =0 
    right = size - 1
    while left < right:
        if left < right and left == right-1:
             edw += 1
             alph += 1
             break
        elif left < right and right == left+1:
            alph += 1
            edw += 1
            break
        elif arr[left] == arr[right]:
            # chek the condition
            edw += 1
            left += 1
            alph += 1
            right -= 1
        elif arr[left] > arr[right]:
            arr[left] -= arr[right]
            right -= 1
            alph += 1
        else:
            arr[right] -= arr[left]
            left += 1
            edw += 1
    if left == right and arr[left] == arr[right]:
        edw += 1
    print(edw,alph)
 
 
size = int(input())
lists = list(map(int,input().split()))
alchemy(lists,size)
