class Solution:
    def ini(self,a):
        if a not in self.reps:
            self.reps[a] = a
        if a not in self.size:
            self.size[a] = 1
    def find(self,node):
        if self.reps[node] != node:
            self.reps[node] = self.find(self.reps[node])
        return self.reps[node]
    
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        
        if rep1 == rep2:
            return
        
        if self.size[rep1] > self.size[rep2]:
            self.reps[rep2] = rep1
            self.size[rep1] += self.size[rep2]
        else:
            self.reps[rep1] = rep2
            self.size[rep2] += self.size[rep1]
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        arr = []
        visited = set()
        holder = []
        for element in nums:
            j = 2
            arr.append([])
            sets = set()
            while j*j <= element:
                while element % j == 0:
                    if j not in sets:
                        arr[-1].append(j)
                        sets.add(j)
                    if arr[-1][-1] not in visited:
                        holder.append(arr[-1][-1])
                        visited.add(arr[-1][-1])
                    element //= j
                j += 1
                
            if element > 1:
                arr[-1].append(element)
                if arr[-1][-1] not in visited:
                    holder.append(arr[-1][-1])
                    visited.add(arr[-1][-1])
        self.reps = {}
        self.size = {}
        for a in arr:
            for index in range(len(a)-1):
                self.ini(a[index])
                self.ini(a[index+1])
                self.union(a[index],a[index+1])
            if not a: 
                return False
            self.ini(a[0])
            
        for index in range(len(holder)-1):
            if self.find(holder[index]) != self.find(holder[index+1]):
                return False
            
        return True     