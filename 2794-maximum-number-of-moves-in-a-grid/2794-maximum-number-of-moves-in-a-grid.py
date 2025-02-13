class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0<= row < len(grid) and 0<= col < len(grid[0])
        directions = [(-1,1),(0,1),(1,1)]
        moves = 0
        visited = set()
        for index in range(len(grid)):
            
            queue = [(index,0,0)]
            while queue:
                row,col,count = heapq.heappop(queue)
                moves = max(moves, count)
                if (row,col) in visited:
                    continue
                visited.add((row,col))
                for _r,_c in directions:
                    new_r = _r + row
                    new_c = _c + col
                    if inbound(new_r,new_c) and (new_r,new_c) not in visited:
                        if grid[new_r][new_c] > grid[row][col]:
                            heapq.heappush(queue,(new_r,new_c, count+1))

        return moves

        