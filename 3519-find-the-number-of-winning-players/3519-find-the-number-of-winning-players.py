class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        pick.sort()
        dicts = {}
        prev = pick[0][0]
        sets = set()
        for xi, yi in pick:
            if xi != prev:
                dicts = {}
                prev = xi
            dicts[yi] = 1 + dicts.get(yi,0)
            if dicts[yi] > xi and xi not in sets:
                sets.add(xi)
        
        return len(sets)