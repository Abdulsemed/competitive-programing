class Solution:
    def longestArithSeqLength(self, arr: List[int]) -> int:
        
        sets  = set()
        for index in range(len(arr)):
            for val in range(index+1, len(arr)):
                sets.add(arr[val]-arr[index])
        maxim = 1
        for key in sets:
            dicts = defaultdict(int)
            for element in arr:
                dicts[element] = 1 + dicts[element-key]
            maxim = max(maxim, max(dicts.values()))
            
        return maxim