class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = sum(weights)
        size = len(weights)
        val = 0
        maxim = max(weights)
        ans =[]
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
                    l = index
                    currSum = weights[l]
                index += 1
            if currSum <= mid:
                count += 1
            if count <= days:
                if mid >= maxim:
                    right = mid -1
                else:
                    left = mid +1
            elif count > days:
                left = mid+1
        return left