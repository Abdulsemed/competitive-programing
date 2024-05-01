class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        curr = []
        
        for index in range(len(word)):
            curr.append(word[index])
            if word[index] == ch:
                return  "".join(curr[::-1]) + word[index+1:]
        return word