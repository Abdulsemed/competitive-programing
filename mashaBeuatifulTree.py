def beautyTree(arr,size,count):
    if size == 1:
        return arr,count
    mid = size//2
    leftArr,leftCount = beautyTree(arr[:mid],mid,count)
    rightArr,rightCount = beautyTree(arr[mid:],size-mid,count)

    if leftArr[0] > rightArr[0]:
        leftCount += 1
        rightArr.extend(leftArr)
    else:
        leftArr.extend(rightArr)
        rightArr = leftArr
    return rightArr, leftCount+rightCount


tests = int(input())
for _ in range(tests):
    size = int(input())
    arr = list(map(int,input().split()))
    arr,count= beautyTree(arr,size,0)
    if arr == sorted(arr):
        print(count)
    else:
        print(-1)
