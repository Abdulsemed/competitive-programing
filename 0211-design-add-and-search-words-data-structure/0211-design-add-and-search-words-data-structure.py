class WordDictionary:
    def __init__(self):
        self.is_end = False
        self.children =[None for _ in range(26)]
    def addWord(self, word: str) -> None:
        curr = self
        for letter in word:
            asci = ord(letter) - 97
            if curr.children[asci] == None:
                curr.children[asci] = WordDictionary()
            curr = curr.children[asci]
        curr.is_end = True
    def dfs(self,curr,word):
        if not word:
            return curr.is_end
        for index,letter in enumerate(word):
            if letter == ".":
                for child in curr.children:
                    if child != None:
                         if (self.dfs(child,word[index+1:])):
                                return True
                return False
            else:
                asci = ord(letter) - 97
                if curr.children[asci]:
                    curr = curr.children[asci]
                    return self.dfs(curr,word[index+1:])
                else:
                     return False
    def search(self, word: str) -> bool:
        curr = self
        return self.dfs(curr,word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)