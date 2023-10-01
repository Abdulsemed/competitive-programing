class Trie:
    def __init__(self):
        self.is_end = False
        self.children =[None for _ in range(26)]
        self.count = 0
    def insert(self,count, word: str) -> None:
        curr = self
        for letter in word:
            asci = ord(letter) - 97
            if curr.children[asci] == None:
                curr.children[asci] = Trie()
            curr = curr.children[asci]
            curr.count += count
        curr.is_end = True
    def search(self, word):
        curr = self
        prefixCount = 0
        for letter in word:
            asci = ord(letter) - 97
            curr = curr.children[asci]
            prefixCount += curr.count
            
        return prefixCount
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        obj = Trie()
        arr = []
        dicts = {}
        counter = {}
        for word in words:
            counter[word] = 1 + counter.get(word,0)
        for key in counter:
            obj.insert(counter[key],key)
        for word in words:
            if word not in dicts:
                count = obj.search(word)
            else:
                count = dicts[word]
            arr.append(count)
        return arr