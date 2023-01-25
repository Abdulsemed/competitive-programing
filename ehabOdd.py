def ehab(arr,size):
    if size > 1:
        oddCount = 0
        evenCount = 0
        for element in arr:
            if element %2 ==0:
                evenCount+=1
            elif element%2 != 0:
                oddCount += 1
            if oddCount > 0 and evenCount > 0:
                break
        if oddCount > 0 and evenCount > 0:
            arr.sort()
    print(*arr)
size = int(input())
lists = list(map(int, input().split(" ")))
ehab(lists,size)
