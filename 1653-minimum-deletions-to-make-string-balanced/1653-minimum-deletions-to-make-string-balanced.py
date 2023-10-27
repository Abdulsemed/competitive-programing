class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_total = s.count('a')
        a_sum = b_sum = 0
        ans = b_total
        for ch in s:
            a_sum += (ch == 'b')
            b_sum += (ch == 'a')
            ans = min(ans, a_sum + (b_total - b_sum))
        return min(ans, a_sum)