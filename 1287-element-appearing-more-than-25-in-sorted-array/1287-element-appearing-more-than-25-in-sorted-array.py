class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dicts = Counter(arr)
        for key in dicts:
            if dicts[key] > len(arr)/4:
                return key
            