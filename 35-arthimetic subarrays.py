def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = []
        for j in range(len(r)):
            temp = sorted(nums[l[j]:r[j] + 1])
            d = temp[1] - temp[0]
            for index in range(1,len(temp)):
                if d != (temp[index] - temp[index-1]):
                    result.append(False)
                    break
                if index == len(temp)-1 and d == temp[index]-temp[index-1]:
                    result.append(True)
                
        return result
