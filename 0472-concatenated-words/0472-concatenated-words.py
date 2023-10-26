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
            obj.height += 1
            if val == len(word)-1 and obj.height > 1: return True
            if self.search(val+1, word,obj): return True
            obj.height -= 1
        return False
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        obj = Trie()
        ans = set()
        for word in words:
            obj.insert(word)
        for word in words:
            self.height = 0
            self.visited = set()
            if obj.search(0,word, self) and self.height > 1:
                ans.add(word)
                
        return list(ans)
        