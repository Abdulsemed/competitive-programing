class Solution:
    def __init__(self):
        self.dicts = {}
        self.size = []
        self.reps = {}
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    def united(self,rep1,rep2):
        self.dicts[rep2] = rep1
        self.size[rep1] += self.size[rep2] 
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return 
        if self.size[rep1] > self.size[rep2]:
            self.united(rep1,rep2)
        else:
            self.united(rep2,rep1)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.size = [1] *(len(accounts))
        for index in range(len(accounts)):
            self.dicts[index] = index
        for index in range(len(accounts)):
            for val in accounts[index][1:]:
                if val in self.reps:
                    self.union(index,self.reps[val])
                else:
                    self.reps[val] = index
        ans = defaultdict(list)
        for key in self.reps:
            rep = self.find(self.reps[key])
            ans[rep].append(key)
        self.dicts = []
        for key in ans:
            self.dicts.append([accounts[key][0]]+ sorted(ans[key]))
        return self.dicts