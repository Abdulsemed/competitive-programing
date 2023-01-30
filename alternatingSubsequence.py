def kDominant(arr, size):
    result = [arr[0]]
    flag = arr[0] > 0
    for index in range(1,size):
        if (arr[index] > 0 and flag) or (arr[index] < 0 and not flag):
            result[-1] = max(result[-1], arr[index])
        elif (arr[index] > 0 and not flag) or (arr[index] < 0 and flag):
            result.append(arr[index])
            flag = not flag
    print(sum(result))
tests = int(input())
for _ in range(tests):
    size = int(input())
    lists = list(map(int,input().split()))
    kDominant(lists,size)
