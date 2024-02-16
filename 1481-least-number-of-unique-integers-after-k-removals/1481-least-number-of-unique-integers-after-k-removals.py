class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dicts = {}
        for element in arr:
            dicts[element] = 1+ dicts.get(element,0)
           
        arr = sorted(dicts.items(), key = lambda x:(x[1],x[0]))
        for index in range(len(arr)):
            if k < arr[index][1]:
                return len(arr) - index
            k -= arr[index][1]
            
        return 0