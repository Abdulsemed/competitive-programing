class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        maxim = max(nums)
        maxCount = 0
        subCount = 0
        size = len(nums)
        maxArr = deque([])
        while right < size:
            if nums[right] == maxim:
                if maxCount == k:
                    curr = maxArr.popleft()
                    temp = curr
                    if maxArr: temp = maxArr.pop()
                    val = (right-temp)
                    if not val: 
                        val = 1
                    subCount += (curr+1) * val
                    maxCount -= 1
                    if temp != curr: maxArr.append(temp)
                maxArr.append(right)
                maxCount += 1
                
            right += 1
        if maxCount == k:
            curr = maxArr.popleft()
            temp = curr
            if maxArr: temp = maxArr.pop()
            val = (right-temp)
            if not val: 
                val = 1
            subCount += (curr+1) * val     
        
        return subCount
                