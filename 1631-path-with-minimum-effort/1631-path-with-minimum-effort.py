class Solution:
    def __init__(self):
        self.directions = [(0,-1),(-1,0),(0,1),(1,0)]
    def inbound(self,row,col,heights):
        return 0<= row < len(heights ) and 0 <= col < len(heights[0])
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dist = {}
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                dist[(i,j)] = float("inf")
                
        visited = set()
        dist[(0,0)] = 0
        
        queue = [(0,(0,0))]
        
        while queue:
            curr_dist, node = heappop(queue)
            
            if node in visited:
                continue
             
            visited.add(node)
            
            for row, col in self.directions:
                new_r = row + node[0]
                new_c = col + node[1]
                if self.inbound(new_r,new_c,heights):
                    distance =  max(curr_dist,  abs(heights[node[0]][node[1]] - heights[new_r][new_c]))
                    if distance < dist[(new_r, new_c)]:
                        dist[(new_r, new_c)] = distance
                        heappush(queue,(distance, (new_r,new_c)))
        # print(dist)                 
        return dist[( len(heights)-1, len(heights[0])-1 )]
        
                