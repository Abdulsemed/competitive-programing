class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 1
        flag = True
        for val in range(len(nums)):
            count = 1
            last = nums[val]
            for index in range(val+1,len(nums)):
                if flag and nums[index] > last:
                    count += 1
                    flag = False
                elif not flag and nums[index] < last:
                    flag = True
                    count += 1
                last = nums[index]
            ans = max(ans,count)
        
        flag = True
        for val in range(len(nums)):
            count = 1
            last = nums[val]
            for index in range(val+1,len(nums)):
                if flag and nums[index] < last:
                    count += 1
                    flag = False
                elif not flag and nums[index] > last:
                    count += 1
                    flag = True
                last = nums[index]
            ans = max(ans, count)
        return ans