class Solution:
    def __init__(self):
        self.size = 0
        self.min = float("inf")
        self.k = 0
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        fair = [0]*k
        self.size = len(cookies)
        self.k = k
        if k == self.size:
            return max(cookies)
        self.distribute(0,0,cookies,fair)
        return self.min
    def distribute(self,left,index,cookies,fair):
        if index >= self.size:
            self.min = min(self.min, max(fair))
            return
        if max(fair) >= self.min:
            return
        for j in range(left,self.k):
            fair[j] += cookies[index]
            self.distribute(left,index+1,cookies,fair[:])
            fair[j] -= cookies[index]