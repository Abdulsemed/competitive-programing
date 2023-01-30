def raisedSort(arr, size,k):
    count = 0
    val = 0
    for index in range(size-1):
        if arr[index] >= arr[index+1]*(2):
            if count >=k:
                val += count -k +1
            count = 0
        else:
            count += 1
    if count >= k:
        val += count -k + 1
    print(val)
tests = int(input())
for _ in range(tests):
    size, k  = map(int,input().split(" "))
    lists = list(map(int, input().split(" ")))
    raisedSort(lists, size, k)
