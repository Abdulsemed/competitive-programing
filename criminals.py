def criminal(arr,size):
    values = 0
    for index in range(size-1):
        if values != 0 and arr[index] == 0:
            values += 1
        elif arr[index] != 0:
            values += arr[index]
    print(values)
tests = int(input())
for _ in range(tests):
    size= int(input())
    lists = list(map(int,input().split()))
    criminal(lists,size)
