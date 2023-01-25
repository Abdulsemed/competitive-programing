def findSmall(size1, size2,arr1, arr2):
    left = 0
    right =0
    while right< size2:
        while left < size and arr2[right] > arr1[left]:
            left += 1
        right += 1
        print(left, end=" ")
size, size2 = map(int, input().split(" "))
lists = list(map(int, input().split(" ")))
lists2 =list(map(int, input().split(" ")))
findSmall(size, size2,lists, lists2)
