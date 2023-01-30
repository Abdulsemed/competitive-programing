class Solution:
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        left = 0
        right = 0
        result = []
        while right < size:
            while right < size and chars[left] == chars[right]:
                    right += 1
            result.append(chars[left])
            if right-left > 1:
                val = str(right-left)
                for element in val:
                    result.append(element)
            left = right
        print(result)
        chars[:] = result
        return len(result)