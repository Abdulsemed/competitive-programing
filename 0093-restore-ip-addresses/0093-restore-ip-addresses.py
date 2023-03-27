class Solution:
    def __init__(self):
        self.valid =  []
        self.size = 0
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.size = len(s)
        self.validate(0,s,[])
        return self.valid
    
    def validate(self, index,s,path):
        if index >= self.size:
            if len(path) == 4:
                self.valid.append('.'.join(path))
        elif len(path) > 4: return
        
        for idx in range(index, self.size):
            val = s[index:idx+1]
            if str(int(val)) == val and idx - index < 3 and int(val) <= 255:
                path.append(val)
                self.validate(idx+1,s,path[:])
                path.pop()
            elif idx - index >= 3:
                return