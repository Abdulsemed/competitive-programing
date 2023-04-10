class Solution:
    def __init__(self):
        self.size = 0
        self.colSize = 0
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.visited = set()
        self.count = 0
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.size = len(grid)
        self.colSize = len(grid[0])
        for index in range(self.size):
            for val in range(self.colSize):
                if grid[index][val] == 1 and (index,val) not in self.visited:
                    self.dfs(index,val,grid)
        return self.count
    def outofBound(self,row,col):
        return 0<= row < self.size and 0<= col< self.colSize
    def dfs (self, row, col, grid):
        self.visited.add((row,col))
        
        for row_change, col_change in self.directions:
            new_row = row + row_change
            new_col = col + col_change
            if (new_row, new_col) not in self.visited and self.outofBound(new_row, new_col):
                if grid[row][col] == 1 and grid[new_row][new_col] == 0:
                    self.count += 1
                if grid[new_row][new_col] == 1:
                    self.dfs(new_row,new_col,grid)
            if grid[row][col] == 1 and not self.outofBound(new_row, new_col):
                self.count += 1
        