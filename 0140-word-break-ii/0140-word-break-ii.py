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
        self.dicts = {}
        
    def search(self,index, word,curr,ans) -> bool:
        if index >= len(word):
            ans.append(" ".join(curr))
            return []
        
        if index in self.dicts:
            ans.append(' '.join(curr + self.dicts[index]))
            return self.dicts[index]
        
        cur = self.root
        
        for val in range(index,len(word)):
            asci = ord(word[val]) - 97
            
            if cur.children[asci]:
                cur = cur.children[asci]
                
            else:
                return []
            
            if cur.is_end:
                valid = self.search(val+1,word,curr+[word[index:val+1]],ans)
                if valid:
                    self.dicts[index] = [word[index:val+1]] + valid                    
                
        if index in self.dicts:      
            return self.dicts[index]  
        
        return []
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        for word in wordDict:
            self.root.insert(word)
            
        ans = []
        self.search(0,s,[],ans)
        
        return ans