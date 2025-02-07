class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        def dfs(index,before):
            if index >= len(power):
                return 0

            if index == before+6:
                return power[index] * dicts[power[index]]

            if (index, before) in memo:
                return memo[(index, before)]

            val1 = 0
            if power[index] > power[before]+2:
                val1 = dfs(index+1, index) + (power[index] * dicts[power[index]])
            val2 = dfs(index+1,before)

            memo[(index, before)] = max(val1, val2)
            return memo[(index, before)]

        dicts = {}
        for element in power:
            dicts[element] = 1 + dicts.get(element, 0)
        
        power = [-2] + sorted(list(dicts.keys()))
        memo = {}
        return dfs(1,0)