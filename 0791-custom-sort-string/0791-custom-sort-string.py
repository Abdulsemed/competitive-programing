class Solution:
    def customSortString(self, order: str, s: str) -> str:
        arr =[]
        sets = Counter(s)
        for element in order:
            while sets[element] > 0:
                arr.append(element)
                sets[element] -= 1
        
        for key in sets:
            while sets[key] > 0:
                arr.append(key)
                sets[key] -= 1
                
        return "".join(arr)
        