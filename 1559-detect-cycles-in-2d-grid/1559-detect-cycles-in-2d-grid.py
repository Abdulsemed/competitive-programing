class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(row,col):
            return 0<= row < len(grid) and 0<= col < len(grid[0])
        def dfs(row,col,parent):
            visited.add((row,col))
            for _r,_c in directions:
                new_r = _r + row
                new_c = _c + col
                if inbound(new_r,new_c) and (new_r,new_c) != parent and grid[new_r][new_c] == grid[parent[0]][parent[1]]:
                    if (new_r,new_c) in visited:
                        return True
                    else:
                        
                        if dfs(new_r,new_c,(row,col)):
                            return True

        for index in range(len(grid)):
            for val in range(len(grid[0])):
                if (index,val) not in visited and dfs(index,val,(index,val)):
                    return True
            
        