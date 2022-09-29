def insertionSort1(n, arr):
    # Write your code here
    i = n - 1
    for index in range(len(arr) - 1):
        if arr[i - index] < arr[(i - 1) - index]:
            holder = arr[i - index]
            arr[i - index] = arr[(i - 1) - index]
            print(*arr)
            arr[(i - 1) - index] = holder

    print(*arr)
