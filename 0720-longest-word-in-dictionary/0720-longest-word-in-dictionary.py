class Tier:
    def __init__(self):
        self.children = [None for index in range(26)]
        self.is_end = False
        self.is_visited = False
    def insert(self,word):
        curr =self
        for letter in word:
            asci = ord(letter) - 97
            if curr.children[asci] == None:
                curr.children[asci] = Tier()
            curr = curr.children[asci]
        curr.is_end = True
    def search(self,word):
        curr =self
        for index in range(len(word)-1):
            asci = ord(word[index]) - 97
            if curr.children[asci]:
                curr = curr.children[asci]
            else:
                return False
        val = curr.children[ord(word[-1])-97]
        if (len(word)- 1 == 1 and curr.is_end) or curr.is_visited:
            val.is_visited = True
            
        return curr.is_end and val.is_visited
            
class Solution:
    def longestWord(self, words: List[str]) -> str:
        obj = Tier()
        words.sort()
        for index in range(len(words)):
            obj.insert(words[index])
        ans = ""
        count = 1
        for index in range(1,len(words)):
            if obj.search(words[index]):
                if len(words[index]) > len(ans):
                    ans = words[index]
                elif len(words[index]) == len(ans) and words[index] < ans:
                    ans = words[index]
        if not ans and len(words[0]) == 1:
            ans = words[0]
        return ans