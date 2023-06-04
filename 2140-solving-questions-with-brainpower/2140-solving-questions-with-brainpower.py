class Solution:
    def __init__(self):
        self.dicts = {}
    def solve(self,index, questions):
        if index >= len(questions):
            return 0
        if index in self.dicts:
            return self.dicts[index]
        self.dicts[index] = max(self.solve(questions[index][1]+index+1, questions)+questions[index][0],
                                self.solve(index+1, questions))
        return self.dicts[index]  
    def mostPoints(self, questions: List[List[int]]) -> int:
        return self.solve(0, questions)