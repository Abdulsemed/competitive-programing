class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dicts = {}
        keys = []
        sets = set()
        for w,l in matches:
            dicts[l] = 1 + dicts.get(l,0)
            if w not in sets:
                keys.append(w)
                sets.add(w)
                
            if l not in sets:
                keys.append(l)
                sets.add(l)
        keys.sort()
        ans =[[],[]]    
        for key in keys:
            if key not in dicts:
                ans[0].append(key)
            elif dicts[key] == 1:
                ans[1].append(key)
        
        return ans