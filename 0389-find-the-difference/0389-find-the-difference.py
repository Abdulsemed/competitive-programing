class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dicts = {}
        dictt = {}
        dicts = self.defineDict(s, dicts)
        dictt = self.defineDict(t,dictt)
        difference = ""
        
        for elements in dictt.keys():
            if elements in dicts.keys():
                if dicts[elements] != dictt[elements]:
                    difference += elements
            else:
                difference += elements
        return difference 
        
    def defineDict(self,s,dictionary):
        for elements in s:
            dictionary[elements] = 1 + dictionary.get(elements,0)
            
        return dictionary