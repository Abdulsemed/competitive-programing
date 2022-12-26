class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sizeOfNums = len(nums)
        sortedNums = [0]*sizeOfNums
        left = 0
        right = sizeOfNums-1
        for element in nums:
            if element % 2 == 0:
                sortedNums[left] = element
                left += 1
            else:
                sortedNums[right] = element
                right -= 1

        return sortedNums