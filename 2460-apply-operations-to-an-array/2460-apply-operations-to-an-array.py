class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        size = len(nums)
        answer = []
        while right < size:
            if nums[left] == nums[right] and nums[left] != 0:
                nums[left] *= 2
                answer.append(nums[left])
                nums[right] = 0
                left += 1
                right += 1
            elif nums[left] != 0:
                answer.append(nums[left])    
            right += 1
            left += 1
        if left < size:
            if nums[left] != 0:
                answer.append(nums[left])
        nums[:] = [0]*(size - len(answer))
        answer.extend(nums)
        return answer
            