class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        val = []
        num1Size = len(num1)
        num2Size = len(num2)
        left = num1Size-1
        right = num2Size -1
        holder = 0
        while left > - 1 or right > -1 or holder:
            val1 = int(num1[left]) if left > -1 else 0
            val2 = int(num2[right]) if right > -1 else 0
            ans = str(val1+ val2 + holder)
            if len(ans) > 1:
                holder = int(ans[0])
                val.append(ans[1])
            else:
                holder = 0
                val.append(ans[0])
            left -= 1
            right -= 1
        return ''.join(val[::-1])