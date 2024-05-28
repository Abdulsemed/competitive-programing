class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = []
        for index in range(len(s)):
            arr.append(abs(ord(s[index]) - ord(t[index])))
        
        left = 0
        right = 1
        maxLength = 0
        curr = arr[0]
        while right < len(s):
            while  left < right and curr > maxCost:
                curr -= arr[left]
                left += 1
            maxLength = max(right-left, maxLength)
            curr += arr[right]
            right += 1
        if curr <= maxCost: 
            maxLength = max(right-left, maxLength)
        return maxLength