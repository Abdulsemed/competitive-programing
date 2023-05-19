class Solution:
    def __init__(self):
        self.reps = defaultdict(list)
        self.dicts = {}
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        
        if rep1 == rep2:
            return
        elif len(self.reps[rep1]) > len(self.reps[rep2]):
            for element in self.reps[rep2]:
                heapq.heappush(self.reps[rep1],element)
            self.dicts[rep2] = rep1
        else:
            for element in self.reps[rep1]:
                heapq.heappush(self.reps[rep2],element)
            self.dicts[rep1] = rep2
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        for index in range(len(s)):
            heapq.heappush(self.reps[index],s[index])
            self.dicts[index] = index
        for src,end in pairs:
            self.union(src,end)
        ans = []
        for i in range(len(s)):
            rep = self.find(i)
            ans.append(heapq.heappop(self.reps[rep]))
        return "".join(ans)