class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        newArr = []
        directions = [(0,1),(1,0),(-1,0),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
        for index in range(len(grid)-2):
            newArr.append([])
            for val in range(len(grid[index])-2):
                row = index+1
                col = val +1
                currMax = grid[row][col]
                for _r,_c in directions:
                    new_r = row+_r
                    new_c = col +_c
                    currMax = max(currMax, grid[new_r][new_c])
                newArr[-1].append(currMax)
                
        return newArr