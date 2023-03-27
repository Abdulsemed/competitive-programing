class Solution:
    def __init__(self):
        self.count = 0
        self.size = 0
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        path = [0]*(n)
        self.size = len(requests)
        self.transfers(0,path,requests, 1)
        return self.count
    def transfers(self,index,path,requests,length):
        if index >= self.size:
            return
        if self.count == self.size: #prunning case
            return
        for val in range(index,self.size):
            path[requests[val][0]] -= 1
            path[requests[val][1]] += 1
            if max(path) == 0:
                self.count = max(self.count,length)
            self.transfers(val+1, path[:],requests,length+1)
            path[requests[val][0]] += 1
            path[requests[val][1]] -= 1