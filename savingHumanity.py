def humanity(arr1,size,m):
    m = min(m,size)
    for _ in range(m):
        left = 0
        right = 1
        arr = arr1.copy()
        while right < size:
            if arr1[left] == "1":
                if right +1 < size:
                    if arr1[right+1] == "0":
                        arr[right] = "1"
                else:
                    arr[right] = "1"
            else:
                if left > 0 and arr1[right] =="1":
                    if arr1[left-1] == "0":
                        arr[left] = "1"
                elif left == 0 and arr1[right] == "1":
                        arr[left] = "1"
            right += 1
            left += 1
        arr1 = arr.copy()
    print("".join(arr1))
 
tests = int(input())
for _ in range(tests):
    size, m = map(int, input().split())
    lists = list(input())
    humanity(lists,size,m)
