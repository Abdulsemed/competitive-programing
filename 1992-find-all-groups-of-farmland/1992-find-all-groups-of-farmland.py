class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def inbound(row,col):
            return 0<= row < len(land) and 0<= col < len(land[0])
        
        def dfs(row,col):
            nonlocal curr_max
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            
            for _r,_c in directions:
                new_r = _r + row
                new_c = _c + col
                if inbound(new_r,new_c)and(new_r,new_c) not in visited and land[new_r][new_c]:
                    curr_max = max(curr_max, (new_r,new_c))
                    visited.add((new_r,new_c))
                    dfs(new_r,new_c)
            
        ans = []
        visited = set()
        for index in range(len(land)):
            for val in range(len(land[0])):
                if land[index][val] and (index,val) not in visited:
                    curr_max = (index,val)
                    dfs(index, val)
                    ans.append([index,val,curr_max[0],curr_max[1]])
        
        return ans