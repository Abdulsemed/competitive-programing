class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        left = 0
        right =  size - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                break
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]
                