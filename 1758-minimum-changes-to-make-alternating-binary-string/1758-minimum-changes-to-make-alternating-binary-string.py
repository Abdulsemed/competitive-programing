class Solution:
    def counter(self,start,s):
        count = 0
        for element in s:
            if element != start:
                count += 1
            if start == "1":
                start = "0"
            else:
                start = "1"
        return count
    def minOperations(self, s: str) -> int:
        start = "1"
        
        minim = float("inf")
        minim = self.counter(start,s)
        start = "0"
        minim = min(minim, self.counter(start,s))
        return minim