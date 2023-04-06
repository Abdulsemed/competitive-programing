class Solution:
    def __init__(self):
        self.count = 0
        self.bools = 0
    def countArrangement(self, n: int) -> int:
        n+=1
        self.counter(n,[])
        return self.count
    def counter(self, n,path):
        if len(path) >= n-1:
            self.count += 1
            return 
        
        for index in range(1,n):
            if self.bools & 1<<index == 0:
                if (len(path)+1) % index == 0 or (index % (len(path)+1) == 0):
                    self.bools += 2**index
                    path.append(index)
                    self.counter(n,path[:])
                    path.pop()
                    self.bools -= 2**index
                