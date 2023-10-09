class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        size = len(heaters)
        maxim = 0
        for index in houses:
            left = 0
            right = size-1
            while left <= right:
                mid = left + (right-left)//2
                if heaters[mid] > index:
                    right = mid -1
                elif heaters[mid] < index:
                    left = mid + 1
                else:
                    right = mid
                    break
            leftSide = rightSide = float("inf")
            if left < size:
                leftSide = abs(heaters[left] - index)
            if right > -1:
                rightSide = abs(heaters[right] - index)
            minim = min( leftSide, rightSide)
            maxim = max(maxim, minim)
            
        return maxim