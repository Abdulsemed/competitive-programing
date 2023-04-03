class Solution:
    def findGCD(self, nums: List[int]) -> int:
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
            
        