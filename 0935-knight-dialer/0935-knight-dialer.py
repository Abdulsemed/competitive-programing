class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        dicts = {
            0:[6,4],
            1:[8,6],
            2:[7,9],
            3:[8,4],
            4:[0,9,3],
            6:[0,7,1],
            7:[2,6],
            8:[1,3],
            9:[2,4],
            
        }
        
        dp = {}
        def dfs(size,num):
            if size <=1:
                return 1
            
            if (size,num) in dp:
                return dp[(size,num)]
            
            ans = 0
            for key in dicts[num]:
                ans += dfs(size-1,key)
                
            dp[(size,num)]  = ans  
            return dp[(size,num)]
        count = 0
        for key in dicts:
            count += dfs(n,key)
            
        return count % 1000000007
                        