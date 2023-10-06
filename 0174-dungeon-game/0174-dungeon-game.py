class Solution:
    def inbound(self, row,col,dungeon):
        return 0 <= row < len(dungeon) and 0<= col < len(dungeon[0])
        
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        directions = [(0,1),(1,0)]
        
        dp = [[-float("inf") for index in range(len(dungeon[0]))] for val in range(len(dungeon))]
        
        dp[-1][-1] = dungeon[-1][-1]
        for index in range(len(dungeon)-1,-1,-1):
            for val in range(len(dungeon[0])-1,-1,-1):
                if index == len(dungeon)-1 and val == len(dungeon[0])-1:
                    continue
                curr = dungeon[index][val]
                holder = - float("inf")
                for _r, _c in directions:
                    new_r = _r+ index
                    new_c = _c + val
                    if self.inbound(new_r,new_c,dungeon):
                        value = dungeon[index][val] + dungeon[new_r][new_c]
                        minim = min(dungeon[index][val], value)
                        if minim > holder:
                            holder = minim
                            curr = minim
                dungeon[index][val] = curr
                dp[index][val] = holder
        val = 1
        if dp[0][0] < 0:
            val += -(dp[0][0])
        return val
        