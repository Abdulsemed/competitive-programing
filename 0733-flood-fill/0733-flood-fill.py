class Solution:
    def __init__(self):
        self.visited = set()
        self.directions = [(1,0),(0,1),(-1,0),(0,-1)]
        self.val = 0
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.val = grid[sr][sc]
        self.dfs(sr,sc, color, grid)
        grid[sr][sc] = color
        return grid
    def inBound(self,row,col, grid):
        return 0<= row < len(grid) and 0<= col < len(grid[0])
    def dfs(self, row,col, color, grid):
        self.visited.add((row,col))
        
        for row_change, col_change in self.directions:
            rows = row+row_change
            cols = col + col_change
            if (rows, cols) not in self. visited and self.inBound(rows,cols,grid) and grid[rows][cols] == self.val:
                self.dfs(rows,cols,color,grid)
                grid[rows][cols] = color
            