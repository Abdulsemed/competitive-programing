class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        val = list(map(str,s.split()))
        return len(val[-1])