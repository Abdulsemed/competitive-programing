class Solution:
    def __init__(self):
        self.directions = [(1,0),(0,1),(0,-1),(-1,0)]
    def shortestBridge(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col]:
                    queue = deque([(row,col)])
                    ones = {(row,col)}
                    path = [(row,col)]
                    while queue:
                        row,col = queue.popleft()
                        for row_c,col_c in self.directions:
                            new_r = row+row_c
                            new_c = col + col_c
                            if self.inbound(new_r,new_c,grid) and (new_r,new_c) not in ones:
                                if grid[new_r][new_c]:
                                    queue.append((new_r,new_c))
                                    ones.add((new_r,new_c))
                    return self.bfs(grid,ones)            
    def inbound(self,row,col,grid):
        return 0<= row< len(grid) and 0<= col < len(grid)
    def bfs(self,grid,ones):
        queue = deque(ones)
        counter = 0
        while queue:
            length  = len(queue)
            for _ in range(length):
                row,col = queue.popleft()
                for row_c,col_c in self.directions:
                    new_r = row+row_c
                    new_c = col + col_c
                    if self.inbound(new_r,new_c,grid) and (new_r,new_c) not in ones:
                        if grid[new_r][new_c]:
                            return counter
                        queue.append((new_r,new_c))
                        ones.add((new_r,new_c))
            counter += 1
        return counter