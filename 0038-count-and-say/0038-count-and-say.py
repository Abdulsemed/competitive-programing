class Solution:
    def countAndSay(self, n: int) -> str:
        def dfs(val):
            ans = []
            index = 1
            count = 0
            while index < len(val)+1:
                if index < len(val) and val[index] == val[index-1]:
                    count += 1
                else:
                    ans.append(str(count+1)+str(val[index-1]))
                    count = 0
                index += 1
            return "".join(ans)

        curr = "1"
        if n == 1:
            return curr
        for index in range(2,n+1):
            curr = dfs(curr)

        return curr

        




            
        