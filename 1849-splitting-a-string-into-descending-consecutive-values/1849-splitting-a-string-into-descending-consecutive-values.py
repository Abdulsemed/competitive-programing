class Solution:
    def splitString(self, s: str) -> bool:
        return self.splitter(0,s,[],len(s))
    def splitter(self,index,s,path,size):
        if index >= size:
            return len(path)>=2
        for j in range(index,size):
            val = int(s[index:j+1])
            if len(path) == 0 or val+1 == path[-1]:
                path.append(val)
                if self.splitter(j+1,s,path[:],size):
                    return True
                path.pop()
        return False
        
        