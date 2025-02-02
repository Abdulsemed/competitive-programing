class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        maxim = max(weights)
        right = max(sum(weights),maxim)
        size = len(weights)
        val = 0
        while left <= right:
            mid= left + (right-left)//2
            currSum = 0
            count =0
            index = 0
            l = 0
            while index < size:
                currSum += weights[index]
                if currSum > mid:
                    count += 1
                    currSum = weights[index]
                    if currSum > mid:
                        count = days + 1
                        break
                index += 1
           
            if currSum <= mid:
                count += 1
            if count <= days:
                right = mid - 1
            elif count > days:
                left = mid+1
        return left