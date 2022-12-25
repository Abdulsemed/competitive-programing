class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        sizeOfNums = len(nums)
        count = 0
        pointer = 0
        
        while pointer < sizeOfNums:
            if nums[pointer] is val:
                nums[pointer] = -1
                count += 1
                if pointer + 1 < sizeOfNums:
                    rightPointer = pointer + 1

                    while nums[rightPointer] != -1 :
                        (nums[rightPointer-1], nums[rightPointer]) = (nums[rightPointer], nums[rightPointer-1])
                        if rightPointer + 1 < sizeOfNums:
                            rightPointer += 1
            
            if nums[pointer] == -1:
                break
            elif nums[pointer] != val:
                pointer += 1
        print(nums)      
        return sizeOfNums - count 
        
        