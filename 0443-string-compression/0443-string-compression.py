class Solution:
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        left = 0
        right = 0
        while right < size:
            while right < size and chars[left] == chars[right]:
                    right += 1
            if right-left > 1:
                val = str(right-left)
                char = chars[left]
                left += 1
                for element in val:
                    chars[left] =element
                    left += 1
                
                while left < size and chars[left] == char:
                    chars.pop(left)
                    size -= 1
                    right -= 1
            left = right
        
        print(chars)
        return len(chars)