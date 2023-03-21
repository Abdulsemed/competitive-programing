class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed  = sorted([(pos,speed) for pos, speed in zip(position, speed)],reverse = True)
        minStack = []
        for pos, speed in posSpeed:
            minStack.append((target-pos)/speed)
            if len(minStack) > 1 and minStack[-1] <= minStack[-2]:
                minStack.pop()
        return len(minStack)