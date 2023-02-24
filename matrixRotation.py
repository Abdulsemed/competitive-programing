def rotate(arr1,arr2):
    flag =False
    for index in range(4):
        if arr1[0] < arr1[1] and arr2[0] < arr2[1] and arr1[0] < arr2[0] and arr1[1] < arr2[1]:
            flag = True
            break
        temp = arr1[0]
        arr1[0] = arr2[0]
        arr2[0] = arr2[1]
        arr2[1] = arr1[1]
        arr1[1] = arr1[0]
        arr1[1] = temp
    if flag:
        print("YES")
    else:
        print("NO")
 
test = int(input())
for _ in range(test):
    matrix1 = list(map(int,input().split()))
    matrix2 = list(map(int,input().split()))
    rotate(matrix1,matrix2)
