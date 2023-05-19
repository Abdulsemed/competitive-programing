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
            self.reps[rep1].extend(self.reps[rep2])
            self.dicts[rep2] = rep1
        else:
            self.reps[rep2].extend(self.reps[rep1])
            self.dicts[rep1] = rep2
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        for index in range(len(s)):
            self.reps[index].append(s[index])
            self.dicts[index] = index
        for src,end in pairs:
            self.union(src,end)
        ans = []
        for key in self.reps:
            if key == self.dicts[key]:
                self.reps[key] = sorted(self.reps[key], reverse = True)
        for i in range(len(s)):
            rep = self.find(i)
            ans.append(self.reps[rep].pop())
        return "".join(ans)