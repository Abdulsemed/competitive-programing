class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        size = n
        nums = [index for index in range(1,size+1)]
        while size > 1:
            index += k-1
            nums.pop(index% size)
            index = index % size
            size -= 1
         
        return nums[0]