class Solution:
    def __init__(self):
        self.reps = defaultdict(set)
        self.dicts = {}
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    def united(self,rep1,rep2):
        for element in self.reps[rep2]:
            if element in self.reps[rep1]:
                self.reps[rep1] = self.reps[rep1].union(self.reps[rep2])
                self.dicts[rep2] = rep1
                break
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return 
        if len(self.reps[rep1]) > len(self.reps[rep2]):
            self.united(rep1,rep2)
        else:
            self.united(rep2,rep1)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for index in range(len(accounts)):
            self.dicts[index] = index
            self.reps[index] = set(accounts[index][1:])
        for index in range(len(accounts)):
            for val in range(index+1,len(accounts)):
                if accounts[index][0] == accounts[val][0]:
                    self.union(index,val)
        ans = []
        for key in self.dicts:
            if key == self.dicts[key]:
                ans.append([accounts[key][0]])
                ans[-1].extend(sorted(list(self.reps[key])))
        return ans