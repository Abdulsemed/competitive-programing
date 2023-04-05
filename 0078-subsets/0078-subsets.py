class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = 2**len(nums)
        lists = []
        for index in range(size):
            curr = []
            idx = 0
            while index:
                if index & 1 == 1:
                    curr.append(nums[idx])
                idx += 1
                index >>= 1
            lists.append(curr)
        return lists
                    