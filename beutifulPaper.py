def square(row1,col1, row2, col2):
    if row1 > col1:
        val1 = row1
        val2 = col1
    else:
        val1 = col1
        val2 = row1
    if row2> col2:
        val3 = row2
        val4 = col2
    else:
        val3 = col2
        val4 = row2
    if val1 == val3:
        if val2 + val4 == val1:
            print("yes")
        else:
            print("no")
    else:
        print("no")
    
    
size = int(input())
for _ in range(size):
    row1, col1 = map(int, input().split(" "))
    row2, col2 = map(int, input().split(" "))
    square(row1,col1,row2,col2)
