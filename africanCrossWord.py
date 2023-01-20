from collections import Counter
def african(matrix, rows, cols):
    crossRow = []
    for row in range(rows):
        vals = Counter(matrix[row])
        lists = []
        for col in range(cols):
            if vals[matrix[row][col]] == 1:
                lists.append(matrix[row][col])
            else:
                lists.append(" ")
        crossRow.append(lists)
    crossCol = []
    for row in range(cols):
        lists = []
        rowDict = {}
        for col in range(rows):
            rowDict[matrix[col][row]] = 1 + rowDict.get(matrix[col][row], 0)
            lists.append(matrix[col][row])
        for col in range(rows):
            if rowDict[matrix[col][row]] > 1:
                lists[col] = " "
        crossCol.append(lists)
    lists = []
    for row in range(rows):
        for col in range(cols):
            if crossRow[row][col] == crossCol[col][row] and crossRow[row][col] != " ":
                lists.append(crossRow[row][col])
    print(''.join(lists))
    
            
    
row, col = map(int, input().split(" "))
matrix = []
for _ in range(row):
    matrix.append(list(input()))
african(matrix, row, col)
