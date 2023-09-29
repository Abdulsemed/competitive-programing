class Solution:
    def __init__(self):
        self.dp = []
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = []
        self.dp = [[-1 for _ in range(len(scores))] for _ in range(len(scores))]
        for index in range(len(scores)):
            scores[index] = [ages[index], scores[index]]
        scores.sort(key = lambda x:(x[0],x[1]), reverse = True)
        return self.dfs(-1,0,scores)
    def dfs(self,curr,index,arr):
        if index >= len(arr):
            return 0
        if self.dp[curr][index] != -1:
            return self.dp[curr][index]
        val1=val2= 0  
        val = 0
        minim = curr
        if curr == -1 or arr[curr][1] >= arr[index][1]:
            val += arr[index][1]
            minim = index
        val1 = self.dfs(minim,index+1,arr) + val
        val2 = self.dfs(curr,index+1,arr)
        self.dp[curr][index] = max(val1,val2)
        return self.dp[curr][index]
            