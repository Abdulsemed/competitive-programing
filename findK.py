def findK(arr,size,k):
    sets = set(tuple(arr))
    flag = False
    for element in arr:
        if element + k in sets:
            flag = True
            break
    if flag:   
        print("YES")
    else:
        print("NO")
        
test = int(input())
for _ in range(test):
    size, k = map(int, input().split())
    lists = list(map(int,input().split()))
    findK(lists, size,k)
