class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dicts = {}
        
        def dfs(index,mask):
            if index >= len(arr):
                return 0
            if (index,mask) in dicts:
                return dicts[(index,mask)]
            bools = True
            before = mask
            for val in arr[index]:
                pos = 1 << (ord(val)-97)
                if pos & mask != 0:
                    bools = False
                    break
                mask += pos
            # print(flag,index,mask,bools)
            
            dicts[(index,before)] = max(dfs(index+1,mask)+ (len(arr[index]) if bools else 0),
                                        dfs(index+1,before))
            return dicts[(index,before)]
        
        return dfs(0,0)