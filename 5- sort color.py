 def sortColors(self, nums):  
  for elt in nums:
    for index in range(len(nums)-1):
        if nums[index] > nums[index+1]:
            holder = nums[index]
            nums[index] = nums[index+1]
            nums[index+1] = holder
  return nums
