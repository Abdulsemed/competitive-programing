def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = [0]*len(s)
        result = 0
        for index in range(len(s)):
            if s[index] in vowels:
                count[index] = 1

        beg = 0
        end = k
        window = sum(count[beg:end])
        while end <= len(s):
            result = max(result, window)
            if end <= len(s)-1:
                window += count[end] - count[beg]
            end += 1
            beg += 1
        return result
