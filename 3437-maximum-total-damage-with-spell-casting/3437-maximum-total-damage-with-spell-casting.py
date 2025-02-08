class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        def dfs(index):
            if index >= len(power):
                return 0

            if (power[index]) in memo:
                return memo[power[index]]

            if power[index] - power[index-1] > 2:
                val = memo[power[index-1]] + power[index] * dicts[power[index]]
            elif power[index] - power[index-2] > 2:
                val = memo[power[index-2]] + power[index] * dicts[power[index]]
            else:
                val = memo[power[index-3]] + power[index] * dicts[power[index]]

            memo[power[index]] = max(val,memo[power[index-1]])
            curr = dfs(index+1)
            return memo[power[index]]

        dicts = {}
        for element in power:
            dicts[element] = 1 + dicts.get(element, 0)
        
        power = [0,0,0] + sorted(list(dicts.keys()))
        memo = {0:0}
        dfs(3)
        return memo[power[-1]]