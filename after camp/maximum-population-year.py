class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        curr = []
        for b,d in logs:
            curr.append((b,1))
            curr.append((d,-1))
        curr.sort()
        maxP = 0
        idx = -1
        val = 0
        for date in curr:
            val += date[1]
            if val > maxP:
                maxP = val
                idx = date[0]
        return idx