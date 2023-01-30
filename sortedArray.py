def sortArray(arr, size):
    arr2 = sorted(arr)
    flag = True
    index = 0
    left = 0
    if arr2[0] == arr[0]:
        while index < size-1 and arr[index] < arr[index+1]:
            index += 1
        left = index
    while index < size-1 and arr[index] > arr[index+1]:
        index += 1
    right = index+1
    arr1 = arr[:left]
    arr1.extend(arr[left:right][::-1])
    arr1.extend(arr[right:])
    if arr1 == arr2:
        print("yes")
        print(left+1, right)
    else:
        print("no")
 
size = int(input())
lists = list(map(int, input().split(" ")))
sortArray(lists, size)
