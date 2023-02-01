def shortest(arr, rows, cols):
    for col in range(cols):
        bottom= rows-1
        for row in range(rows-1,-1,-1):
            if arr[row][col]  == "*":
                arr[row][col] = "."
                arr[bottom][col] = "*"
                bottom -= 1
            elif arr[row][col] == "o":
                bottom = row-1
    for row in range(rows):
        for col in range(cols):
            print(arr[row][col], end="")
        print(end="\n")
        
test = int(input())
for _ in range(test):
    rows, cols = map(int,input().split(" "))
    lists = []
    for row in range(rows):
        lists.append(list(input()))
    shortest(lists, rows, cols)
