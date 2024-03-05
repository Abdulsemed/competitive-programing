class Solution:
    def minimumLength(self, s: str) -> int:
        maxim = len(s)
        left = 0
        right = len(s)-1
        leftArr = [0,0,0]
        rightArr = [0,0,0]
        while left< right:
            pos = ord(s[left])-97
            leftArr[pos] = 1
            while right > left and pos == ord(s[left])-97:
                left += 1
            pos = ord(s[right])-97
            rightArr[pos] = 1
            while left < right and pos == ord(s[right]) -97:
                right -= 1
                
            if leftArr[0]==rightArr[0] and leftArr[1]==rightArr[1] and leftArr[2]==rightArr[2]:
                maxim = min(maxim, (right-left)+1)
            else:
                break
            leftArr = [0,0,0]
            rightArr = [0,0,0]
        if right > 0 and s[left] == s[right-1] and maxim == 1:
            return 0
        return maxim