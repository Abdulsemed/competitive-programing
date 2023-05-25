class Solution:
    def __init__(self):
        self.reps = {}
        self.size = []
    def find(self,node):
        if node != self.reps[node]:
            self.reps[node] = self.find(self.reps[node])
        return self.reps[node]
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return 
        elif self.size[rep1] > self.size[rep2]:
            self.size[rep1] += self.size[rep2]
            self.reps[rep2] = rep1
        else:
            self.size[rep2] += self.size[rep1]
            self.reps[rep1] = self.reps[rep2]
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ans = []
        self.size = [1] *(n)
        self.reps = {index:index for index in range(n)}
        for left, right in requests:
            flag= True
            leftRep = self.find(left)
            rightRep = self.find(right)
            for src, end in restrictions:
                rep1 = self.find(src)
                rep2 = self.find(end)
                if (leftRep == rep1 and rightRep == rep2) or (leftRep == rep2 and rightRep == rep1):
                    flag = False
                    break
            if flag:
                self.union(leftRep,rightRep)
                ans.append(True)
            else:
                ans.append(False)
        return ans