class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")
        
        for element in nums:
            if element <= first:
                first = element
            elif element <= second:
                second = element
            else:
                return True
        return False
                