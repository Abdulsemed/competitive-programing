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
    def search(self, word: str, s) -> bool:
        curr = self
        index = 0
        idx = 0
        while idx < len(s) and index <  len(word):
            asci = ord(word[index]) - 97
            if curr.children[asci] == None:
                curr = curr.children[ord(s[idx]) - 97]
            else:
                curr = curr.children[asci]
                index += 1
                
            idx += 1
        return index >= len(word)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        obj = Trie()
        obj.insert(s)
        count = 0
        dicts = {}
        for word in words:
            if word in dicts:
                count += dicts[word]
            elif obj.search(word,s):
                dicts[word] = 1
                count += 1
            else:
                dicts[word] = 0
        return count