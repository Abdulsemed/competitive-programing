class Solution:
    def __init__(self):
        self.count = 0
        self.directions = [(1,0),(0,1),(-1,0),(0,-1)]
        self.visited = set()
        self.bools = True
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        for index in range(len(grid1)):
            for val in range(len(grid1[0])):
                self.bools = True
                if (index,val) not in self.visited and grid2[index][val]:
                    self.dfs(index,val,grid1,grid2)
                    if grid1[index][val] and self.bools:
                        self.count += 1
                
        return self.count
    def inbound(self,row,col,grid):
        return 0<= row < len(grid) and 0<= col < len(grid[0])
    def dfs(self,row,col,grid1,grid2):
        self.visited.add((row,col))
        
        for row_change, col_change in self.directions:
            new_row  = row + row_change
            new_col = col + col_change
            if self.inbound(new_row,new_col,grid1) and (new_row,new_col) not in self.visited:
                if grid2[new_row][new_col]:
                    if self.bools and grid1[new_row][new_col]:
                        self.bools = True
                    else:
                        self.bools = False
                    self.dfs(new_row,new_col,grid1,grid2)
                
        