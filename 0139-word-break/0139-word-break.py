class Trie:
    def __init__(self):
        self.children =[None]*(26)
        self.is_end = False
        
    def insert(self,word):
        curr = self
        for letter in word:
            asci = ord(letter) - 97
            if curr.children[asci] == None:
                curr.children[asci] = Trie()
            curr = curr.children[asci]
        curr.is_end = True
        
    def search(self,idx,word, obj):
        curr = self
        stack = []
        for index in range(idx,len(word)):
            asci = ord(word[index]) - 97
            if curr.children[asci]:
                curr = curr.children[asci]
            else:
                break
            
            if curr.is_end:
                stack.append(index)
        while stack:
            val = stack.pop()
            if (val, idx) in obj.visited:
                continue
            obj.visited.add((val,idx))
            if val == len(word)-1: return True
            if self.search(val+1, word,obj): return True
        return False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        obj = Trie()
        self.visited = set()
        for word in wordDict:
            obj.insert(word)
        if obj.search(0,s,self): 
            return True
        return False