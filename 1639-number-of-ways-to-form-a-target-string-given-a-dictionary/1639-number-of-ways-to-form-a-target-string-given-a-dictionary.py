class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dicts = defaultdict(int)
        def dfs(idx,i):
            if idx == len(words[0]):
                return 1 if i == len(target) else 0
            if(i, idx) in dicts:
                return dicts[(i,idx)]
            
            
            dicts[(i,idx)] = dfs(idx+1,i)
            if i < len(target):
                pos = ord(target[i]) -97
                dicts[(i,idx)] += dfs(idx+1,i+1)*arr[pos][idx]
                    
            return dicts[(i,idx)] % (10**9 + 7)
        
        arr = [[0]*len(words[0]) for _ in range(26)]
        for j in range(len(words[0])):
            for val in range(len(words)):
                pos  = ord(words[val][j]) - 97
                arr[pos][j] += 1       
        return dfs(0,0)