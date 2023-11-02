class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dead = {}
        live = {}
        minim = float("inf")
        maxim = -float("inf")
        for b,d in logs:
            maxim = max(maxim, d)
            minim = min(minim, b)
            dead[d] = 1 + dead.get(d,0)
            live[b] = 1 + live.get(b,0)
       
        maxP = 0
        idx = -1
        val = 0
        for date in range(minim,maxim+1):
            
            if date in live:
                val += live[date]
            if date in dead:
                val -= dead[date]
            if val > maxP:
                maxP = val
                idx = date
        return idx