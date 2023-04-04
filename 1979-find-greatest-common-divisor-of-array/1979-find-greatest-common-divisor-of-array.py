class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(min(nums), max(nums))
    def gcd(self,num1, num2):
        if num1 == 0:
            return num2
        return self.gcd(num2 % num1, num1)
    def findgcd(self, nums: List[int]) -> int:
        minim = min(nums)
        maxim = max(nums)
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
            
        