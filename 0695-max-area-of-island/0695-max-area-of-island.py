class Solution:
    def __init__(self):
        self.directions = [(1,0),(0,1),(0,-1),(-1,0)]
        self.size = 0
        self.colSize = 0
        self.visited = set()
        self.count = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        self.size = len(grid)
        self.colSize = len(grid[0])
        for index in range(self.size):
            for val in range(self.colSize):
                self.count = 1
                if grid[index][val] == 1 and (index,val) not in self.visited:
                    self.dfs(index,val, grid)
                    count = max(count, self.count)
        return count
    
    def inBound(self,row,col):
        return 0<= row < self.size and 0<= col < self.colSize
    
    def dfs(self,row,col,grid):
        self.visited.add((row,col))
        for row_change, col_change in self.directions:
            new_row = row_change+ row
            new_col = col_change + col
            if self.inBound(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in self.visited:
                self.count += 1
                self.dfs(new_row, new_col,grid)      
        