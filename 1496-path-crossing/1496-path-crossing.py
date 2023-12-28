class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = [0,0]
        dicts = {"N":(1,0), "S":(-1,0), "E":(0,1), "W":(0,-1)}
        sets = {(0,0)}
        for element in path:
            curr[0] += dicts[element][0]
            curr[1] += dicts[element][1]
            val = (curr[0],curr[1])
            if val in sets:
                return True
            sets.add(val)
        return False