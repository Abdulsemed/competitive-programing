def rotate(matrix, length):
    counter = 0
    size = length //2
    for values in range(size):
        for index in range(values,length-values-1):
            numZero = 0
            numOne = 0
            col = index
            row = values
            for val in range(4):
                if matrix[row][col] == 1:
                    numOne += 1
                else:
                    numZero += 1
                temp = col
                col = row
                row = length- temp -1
            counter += min(numZero, numOne)
    
    print(counter)
    
size = int(input())
for _ in range(size):
    length = int(input())
    matrix = []
    for _ in range(length):
        matrix.append(list(map(int,list(input()))))
    rotate(matrix, length)
