class Solution:
def solve(self,n,dicts):
if n== 1:
return 1
if n == 0:
return 0
if n not in dicts:
dicts[n] = self.solve(n-1, dicts) + self.solve(n-2, dicts)
return dicts[n]
def fib(self, n: int) -> int:
dicts = {}
return self.solve(n,dicts)
class Solution:
def fib(self, n: int) -> int:
dp = [0,1]
for index in range(2,n+1):
dp.append(dp[index-1]+dp[index-2])
return dp[n]