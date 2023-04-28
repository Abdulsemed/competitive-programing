class Solution:
    def __init__(self):
        self.directions = [(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[len(grid)-1][len(grid)-1]:
            return -1
        return self.bfs(0,0,grid)
    def inbound(self,row,col,size):
        return 0<= row < size and 0<= col < size
    def bfs(self,row,col,grid):
        queue = deque([[0,0]])
        visited = {(0,0)}
        size = len(grid)
        count = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row,col= queue.popleft()
                if row == col == size-1:
                    queue = []
                    break
                for row_c, col_c in self.directions:
                    new_r = row+row_c
                    new_c = col + col_c
                    if self.inbound(new_r,new_c,size):
                        if grid[new_r][new_c] == 0 and (new_r,new_c) not in visited:
                            queue.append([new_r,new_c])
                            visited.add((new_r,new_c))
            count += 1
        if row == col == size-1:
            return count
        return -1
        