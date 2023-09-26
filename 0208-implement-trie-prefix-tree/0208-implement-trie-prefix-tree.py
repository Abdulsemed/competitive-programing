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
    def search(self, word: str) -> bool:
        curr = self
        for letter in word:
            asci = ord(letter) - 97
            if curr.children[asci]:
                curr = curr.children[asci]
            else:
                return False
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for letter in prefix:
            asci = ord(letter) - 97
            if curr.children[asci]:
                curr = curr.children[asci]
            else:
                return False
    
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)