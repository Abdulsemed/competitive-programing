class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dicts = {}
        for element in arr:
            dicts[element] = 1 + dicts.get(element,0)
        sets = set()
        for key in dicts:
            if dicts[key] in sets:
                return False
            sets.add(dicts[key])
            
        return True