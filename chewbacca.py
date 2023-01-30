def chew(nums):
    minimum = 10
    result = ""
    flag = False
    for index in range(len(nums)):
        if index == 0 and nums[index] == 9:
            nums[index] = 9
        elif 9-nums[index] < nums[index]:
            nums[index] = 9- nums[index]
            
    print(''.join([str(char) for char in nums]))
nums = list(input())
num = list(map(int,nums))
chew(num)
