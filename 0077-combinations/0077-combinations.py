class Solution:
    def __init__(self):
        self.comb = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinator(1,n,k,[])
        return self.comb
    def combinator(self,index,n,k,path):
        if index > n:
            if len(path) == k:
                self.comb.append(path)
            return
        self.combinator(index+1,n,k,path+[index])
        self.combinator(index+1,n,k,path)
        