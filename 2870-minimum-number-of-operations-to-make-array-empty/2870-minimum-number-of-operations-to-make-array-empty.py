class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dicts = {}
        for element in nums:
            dicts[element] = 1 + dicts.get(element, 0)
        count = 0
        for key in dicts:
            if dicts[key] % 3 ==0:
                count += dicts[key]//3
            else:
                val = (dicts[key]-2) % 3
                if dicts[key] > 2 and (val+2) % 2 == 0:
                    count += ((dicts[key]-2)//3 + (val+2)//2)
                elif dicts[key] % 2 == 0:
                    count += (dicts[key]//2)
                else:
                    return -1
        return count