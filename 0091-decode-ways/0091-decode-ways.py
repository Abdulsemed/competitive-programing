class Solution:
    def __init__(self):
        self.dicts = {}
    def solve(self,index,size,s):
        if index >= len(s):
            return 1
        
        if (index) in self.dicts:
            return self.dicts[index]
        val1,val2 = 0,0
        if s[index:index+size][0] != "0":
            val1 = self.solve(index+1,size,s)
        else:
            return 0
        
        if index +1  < len(s) and int(s[index:index+1+size])  < 27:
            val2 = self.solve(index+size+1,size,s)
        self.dicts[index] = val1 + val2
        return self.dicts[index]
    def numDecodings(self, s: str) -> int:
        return self.solve(0,1, s)
        print(self.dicts)
        return 0
#     2,2,6,10,5,3,20,9
#     22,6,10,5,3,20,9
#     2,26,10,5,3,20,9

