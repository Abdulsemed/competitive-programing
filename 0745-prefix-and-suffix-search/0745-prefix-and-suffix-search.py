class Trie:
    def __init__(self):
        self.is_end = False
        self.index = -1
        self.children =[None for _ in range(27)]
    def insert(self,index, word: str) -> None:
        curr = self
        for letter in word:
            asci = ord(letter) - 97
            if curr.children[asci] == None:
                curr.children[asci] = Trie()
            curr = curr.children[asci]
            curr.index = index
        curr.index = index
        curr.is_end = True
    
    def search(self,curr,word):
        for letter in word:
            asci = ord(letter) - 97
            if curr.children[asci]:
                curr = curr.children[asci]
            else:
                return -1
        return curr.index
               
class WordFilter:

    def __init__(self, words: List[str]):
        self.obj = Trie()
        for index in range(len(words)):
            for val in range(len(words[index])):
                combined = words[index][val:] + "{" + words[index]
                self.obj.insert(index,combined)

    def f(self, pref: str, suff: str) -> int:
        return self.obj.search(self.obj,suff+"{" + pref)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)