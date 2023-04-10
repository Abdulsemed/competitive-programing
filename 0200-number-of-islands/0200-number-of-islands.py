class Solution:
    def __init__(self):
        self.visited = set()
        self.count = 0
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        for index in range(len(grid)):
            for val in range(len(grid[0])):
                if grid[index][val] == "1" and (index, val) not in self.visited:
                    self.dfs(index,val,grid)
                    self.count += 1

        return self.count
    def outofBound(self,row,col, grid):
        return 0<= row < len(grid) and 0<= col< len(grid[0])
        
    def dfs(self, row,col, grid):
        self.visited.add((row,col))
        
        for row_change, col_change in self.directions:
            new_row = row + row_change
            new_col = col + col_change
            
            if (new_row, new_col) not in self.visited and self.outofBound(new_row, new_col, grid):
                if grid[new_row][new_col] == "1":
                    self.dfs(new_row, new_col, grid)
            