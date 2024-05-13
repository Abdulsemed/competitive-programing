class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            arr = "".join(["1"]*(len(grid)))
            return int(arr,2)
        flag = True
        while flag:
            flag = False
            for val in range(len(grid[0])-1,-1,-1):
                zeroCount = 0
                for index in range(len(grid)):
                    if grid[index][val] == 0:
                        zeroCount += 1
                if zeroCount > len(grid) / 2:
                    flag= True
                    for index in range(len(grid)):
                        if grid[index][val] == 0:
                            grid[index][val] = 1
                        else:
                            grid[index][val] = 0

            for index in range(len(grid)):
                ones = 0
                zeros = 0
                for val in range(len(grid[0])):
                    if grid[index][val] == 1:
                        ones += 2**((len(grid[0])-val)-1)
                    else:
                        zeros += 2**((len(grid[0])-val)-1)
                        
                if zeros > ones:
                    flag = True
                    for val in range(len(grid[0])):
                        if grid[index][val] == 1:
                            grid[index][val] = 0
                        else:
                            grid[index][val] = 1
        
        currSum = 0
        for index in range(len(grid)):
            arr = []
            for val in range(len(grid[0])):
                arr.append(str(grid[index][val]))
                
            currSum += int("".join(arr),2)
        
        return currSum
            