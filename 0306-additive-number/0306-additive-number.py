class Solution:
    def __init__(self):
        self.size = 0
    def isAdditiveNumber(self, num: str) -> bool:
        self.size = len(num)
        return self.adder(0,num,[])
    def adder(self,index,num,path):
        if index >= self.size:
            return len(path)>=3
        
        for j in range(index,self.size):
            val = int(num[index:j+1])
            if str(val) == num[index:j+1]:
                if len(path) < 2 or path[-1]+path[-2] == val:
                    path.append(val)
                    if self.adder(j+1,num,path[:]):
                        return True
                    path.pop()
            
        return False
                
                
            