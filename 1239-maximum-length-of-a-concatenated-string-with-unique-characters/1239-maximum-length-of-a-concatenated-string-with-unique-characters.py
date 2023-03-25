class Solution:
    def __init__(self):
        self.maxLen = 0
        self.size = 0
    def maxLength(self, arr: List[str]) -> int:
        self.size = len(arr)
        self.concat(0,arr,[])
        return self.maxLen
    def concat(self,index, arr, path):
        self.maxLen = max(self.maxLen, len(Counter(''.join(path))))
        if index >= self.size:
            return 
        for val in range(index, self.size):
            dicts = Counter(arr[val]) 
            maxim = max(dicts.values()) == 1
            if not path:
                if maxim:
                    path.append(arr[val])
                    self.concat(val+1,arr,path[:])
                    path.pop()
                else:
                    continue
            elif maxim:
                flag = True
                count = Counter(''.join(path))
                for element in arr[val]:
                    if element in count:
                        flag = False
                        break
                if flag:
                    path.append(arr[val])
                    self.concat(val+1,arr,path[:])
                    path.pop()