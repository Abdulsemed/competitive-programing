class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    def insert(self,word):
        curr = self
        for index in range(len(word)):
            if curr.children.get(word[index], None) == None:
                curr.children[word[index]] = Trie()
            curr = curr.children[word[index]]
            if curr.is_end:
                break
        
        if not curr.is_end:
            curr.is_end = True
            return True
        return False                
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = set()
        obj = Trie()
        folder.sort()
        for fold in folder:
            value = fold.split("/")
            if obj.insert(value[1:]):
                ans.add(fold)
        return list(ans)
                
        