def minimum(arr):
    arr.sort()
    print(arr[1])
    
size = int(input())  
for _ in range(size):
    lists = list(map(int, input().split(" ")))
    minimum(lists)
