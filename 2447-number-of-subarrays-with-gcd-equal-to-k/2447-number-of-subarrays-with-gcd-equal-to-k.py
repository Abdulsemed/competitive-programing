class Solution:
    def gcd(self, num1, num2):
        maxim , minim = num2,num1
        if num1 > num2:
            maxim = num1
            minim = num2
        flag = True
        setsA = {minim}
        setsB = {maxim}
        currA = minim
        currB = maxim
        product = minim*maxim
        while True:
            if currA in setsB:
                break
            currA += minim
            currB += maxim
            setsA.add(currA)
            setsB.add(currB)
        return product//currA
    def gcd1(self,num1, num2):
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
                check = gcd(nums[index], nums[val])
                while check:
                    if check == k:
                        count += 1
                    if val+1 < size :
                        val += 1
                    else:
                        break
                    check = gcd(nums[val],check)
                    
            
        return count
            