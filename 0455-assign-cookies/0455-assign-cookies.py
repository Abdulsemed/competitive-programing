class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        right = 0
        left =0
        while left < len(g):
            while  right < len(s)and g[left] > s[right]:
                right += 1
            
            if right == len(s):
                break
            left += 1
            right += 1
        return left