class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        for key,value in freq.items():
            if value > (len(nums)//2):
                return key
            
        