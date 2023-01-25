def lessOrEqual(arr,size,k):
    arr.sort()
    if k ==0 :
        val =arr[k] -1
        return val if val >0 else "-1"
    elif k == size:
        return arr[k-1]
    else:
        value1 =arr[k]
        value2 = arr[k-1]
        if value1 == value2:
            return "-1"
        return value2
    
size, k = map(int, input().split(" "))
lists = list(map(int, input().split(" ")))
print(lessOrEqual(lists,size,k))
