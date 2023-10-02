class Trie:
    def __init__(self):
        self.is_end = False
        self.children =[None for _ in range(26)]
    def insert(self, word: str) -> None:
        curr = self
        for letter in word:
            asci = ord(letter) - 97
            if curr.children[asci] == None:
                curr.children[asci] = Trie()
            curr = curr.children[asci]
        curr.is_end = True
    
class Solution:
    def __init__(self):
        self.root = Trie()
    def search(self,index, word,curr,ans) -> bool:
        if index >= len(word):
            ans.append(" ".join(curr))
        cur = self.root
        for val in range(index,len(word)):
            asci = ord(word[val]) - 97
            if cur.children[asci]:
                cur = cur.children[asci]
            else:
                return False
            if cur.is_end:
                self.search(val+1,word,curr+[word[index:val+1]],ans)
                
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        for word in wordDict:
            self.root.insert(word)
        ans = []
        self.search(0,s,[],ans)
        return ans