class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 1
        flag = True
        count = 1
        last = nums[0]
        for index in range(1,len(nums)):
            if flag and nums[index] > last:
                count += 1
                flag = False
            elif not flag and nums[index] < last:
                flag = True
                count += 1
            last = nums[index]
        ans = max(ans,count)
        flag = True
        last = nums[0]
        count = 1
        for index in range(1,len(nums)):
            if flag and nums[index] < last:
                count += 1
                flag = False
            elif not flag and nums[index] > last:
                count += 1
                flag = True
            last = nums[index]
        return max(ans, count)