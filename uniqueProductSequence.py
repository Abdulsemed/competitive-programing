def uniproduct(arr, size):
    count = 0
    neg = 0
    zeros = 0
    pos = 0
    arr.sort()
    for element in arr:
        if element > 0:
            count += element - 1
            pos += 1
        elif element < 0:
            count += abs(element)-1
            neg += 1
        else:
            count += 1
            zeros += 1
    if neg % 2 != 0 and zeros == 0:
        count += 2
    print(count)
 
size = int(input())
lists = list(map(int,input().split()))
uniproduct(lists, size)
