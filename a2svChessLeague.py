def chessLeague(arr,_left, _right,k):
    if _left ==_right-1 :
        return [arr[_left]]
    _mid = (_left+_right)//2
    leftArr= chessLeague(arr,_left,_mid,k)
    rightArr= chessLeague(arr,_mid,_right,k)
    lists = []
    minimLeft = leftArr[0]
    minimRight = rightArr[0]
    left ,right = 0,0
    leftSize, rightSize = len(leftArr), len(rightArr)
    while left < leftSize or right < rightSize:
        val1 = leftArr[left] if left < leftSize else (rightArr[right][0]+1, 0)
        val2 = rightArr[right] if right < rightSize else (leftArr[left][0]+1, 0)
        if val1[0] > val2[0]:
            if minimLeft[0] - rightArr[right][0] <= k:
                lists.append(rightArr[right])
            right += 1
        
        else:
            if minimRight[0] - leftArr[left][0] <= k:
                lists.append(leftArr[left])
            left += 1
    return lists
 
round, k = map(int,input().split())
arr = list(map(int,input().split()))
arr = [(value,index+1) for index,value in enumerate(arr) ]
arr = sorted(chessLeague(arr,0,2**round,k), key= lambda item: item[1])
print(*[value[1] for value in arr])
