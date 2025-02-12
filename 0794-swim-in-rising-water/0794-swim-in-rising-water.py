class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inBound(row,col):
            return 0<= row < len(grid) and 0<= col < len(grid[0])

        stack = [(0,0, grid[0][0])]
        ans = float("inf")
        visited = set()
        while stack:
            # print(stack)
            curr_r,curr_c,curr_w = heapq.heappop(stack)
            if (curr_r, curr_c) == (len(grid)-1, len(grid)-1):
                ans = min(ans, curr_w)
            if (curr_r,curr_c,curr_w) in visited:
                # print(curr_r,curr_c)
                continue
            visited.add((curr_r,curr_c,curr_w))
            for _r,_c in directions:
                new_r = curr_r + _r
                new_c = curr_c + _c
                if inBound(new_r,new_c):
                    weight = max(curr_w, grid[new_r][new_c])
                    heapq.heappush(stack,(new_r,new_c, weight))
        
        return ans                
                