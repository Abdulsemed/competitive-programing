class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        equalvals = 0
        lessval = 0
        for element in nums:
            if element < target:
                lessval += 1
            elif element == target:
                equalvals += 1
        equalvals += lessval
        lists = []
        for index in range(lessval, equalvals):
            lists.append(index)
        return lists