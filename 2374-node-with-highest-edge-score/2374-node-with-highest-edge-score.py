class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        dicts = {}
        maxim  = 0
        ans = 0
        for index in range(len(edges)):
            dicts[edges[index]] = index + dicts.get(edges[index],0)
            if dicts[edges[index]] > maxim:
                maxim = dicts[edges[index]]
                ans = edges[index]
            if dicts[edges[index]] == maxim and edges[index] < ans:
                ans = edges[index]
                
        return ans
        