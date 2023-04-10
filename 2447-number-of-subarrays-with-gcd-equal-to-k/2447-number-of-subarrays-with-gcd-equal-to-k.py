class Solution:
    def gcd(self,num1, num2):
        if num2 == 0:
            return num1
        return self.gcd(num2, num1 % num2)
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        size = len(nums)
        for index in range(size):
            if nums[index] == k:
                count += 1
            if index < size -1:
                val = index+1
                if nums[index] > nums[val]:
                    check = gcd(nums[index], nums[val])
                else:
                    check = gcd(nums[val], nums[index])
                while check:
                    if check == k:
                        count += 1
                    if val+1 < size :
                        val += 1
                    else:
                        break
                    check = gcd(nums[val],check)
            
        return count
            