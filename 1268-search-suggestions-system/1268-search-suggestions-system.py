class Tier:
    def __init__(self):
        self.is_end = False
        self.children = [[None,[]] for _ in range(26)]
    def insert(self,word):
        curr = self
        for letter in word:
            asci = ord(letter) -97
            if curr.children[asci][0] == None:
                curr.children[asci] = [Tier(),[]]
                
            if len(curr.children[asci][1]) < 3:
                curr.children[asci][1].append(word)
            curr = curr.children[asci][0]
        curr.is_end = True
    def search(self,key,ans):
        curr = self
        flag = True
        for letter in key:
            asci = ord(letter)-97
            if flag and curr.children[asci][0]:
                ans.append(curr.children[asci][1])
                curr = curr.children[asci][0]
                
            else:
                flag = False
                ans.append([])
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        obj = Tier()
        ans = []
        for product in products:
            obj.insert(product)
        obj.search(searchWord,ans)
        return ans