class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dict1 = Counter(s)
        res = []
        seen = set()
        for char in s:
            dict1[char] -= 1
            if char not in seen:
                while res and dict1[res[-1]]>0 and char < res[-1]:
                    seen.remove(res.pop())
                    
                res.append(char)
                seen.add(char)
        return "".join(res)
            