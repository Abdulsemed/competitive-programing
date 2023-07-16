class Solution:
    def __init__(self):
        self.ans = []
        self.dicts = {}
    def letterCombinations(self, digits: str) -> List[str]:
        self.dicts = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if digits:
            self.dfs(0,"",digits)
        return self.ans
    def dfs(self,index,string,digits):
        if index == len(digits)-1:
            for key in self.dicts[digits[index]]:
                self.ans.append(string+key)
            return 
        
        for key in self.dicts[digits[index]]:
            self.dfs(index+1,string+key,digits)
            
        