def xsum(grid,rows, cols):
    sumDict ={}
    diffDict = {}
    maxSum = 0
    for row in range(rows):
        for col in range(cols):
            sumDict[row+col] = grid[row][col] + sumDict.get(row+col, 0)
            diffDict[row-col] = grid[row][col] + diffDict.get(row-col, 0)
            
    for row in range(rows):
        for col in range(cols):
            count = sumDict[row+col] + diffDict[row-col] - grid[row][col]
            maxSum = max(maxSum, count)
            
    print(maxSum)

size = int(input())
for _ in range(size):
    grid = []
    row, col = map(int,input().split(" "))
    for _ in range(row):
        lists = list(map(int, input().split(" ")))
        grid.append(lists)
    xsum(grid,row,col)
