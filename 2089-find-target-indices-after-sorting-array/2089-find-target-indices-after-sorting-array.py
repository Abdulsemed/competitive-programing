class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        counts = Counter(nums)
        equalvals = counts[target]
        lessval = 0
        for key in counts:
            if key < target:
                lessval += counts[key]
        equalvals += lessval
        lists = []
        for index in range(lessval, equalvals):
            lists.append(index)
        return lists