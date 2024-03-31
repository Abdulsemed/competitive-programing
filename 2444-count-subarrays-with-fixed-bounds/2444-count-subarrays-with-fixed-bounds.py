class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        right = 0
        left = 0
        dicts = {-1:[0,0]}
        size = len(nums)
        minR = 0
        maxR = 0
        queue = deque([])
        count = 0
        while right < size:
            dicts[right] = dicts[right-1].copy()
            if nums[right] < minK or nums[right] > maxK:
                #print(queue, left)
                while left < right and queue:
                    flag= True
                    for index, curr in queue:
                        #print(left,index,curr, minR, maxR)
                        if curr[0] - minR > 0 and curr[1] - maxR > 0:
                            #print(right-index)
                            count += (right-index)
                            flag = False
                        if not flag: break
                    if nums[left] == minK:
                        minR += 1
                    if nums[left] == maxK:
                        maxR += 1
                    while queue and queue[0][0] <= left:
                        queue.popleft()
                    left += 1
                while left < right:
                    if nums[left] == minK:
                        minR += 1
                    if nums[left] == maxK:
                        maxR += 1
                    while queue and queue[0][0] <= left:
                        queue.popleft()
                    left += 1
                right += 1
                left = right
                continue
                    
            if nums[right] == minK:
                dicts[right][0] += 1
                
            if nums[right] == maxK:
                dicts[right][1] += 1  
            if dicts[right][0] > 0 and dicts[right][1] > 0:
                queue.append([right,dicts[right]])
            right += 1
            
        while left < right and queue:
            #print(queue, left)
            flag= True
            for index, curr in queue:
                #print(left,index,curr, minR, maxR)
                if curr[0] - minR > 0 and curr[1] - maxR > 0:
                    #print(right-index)
                    count += (right-index)
                    flag = False
                if not flag: break
            if nums[left] == minK:
                minR += 1
            if nums[left] == maxK:
                maxR += 1
            while queue and queue[0][0] <= left:
                queue.popleft()
            left += 1
        return count 
        
    
            