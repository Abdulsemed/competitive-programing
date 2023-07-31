class Solution:
    def romanToInt(self, s: str) -> int:
        dicts = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
                 "IV":4, "IX":9, "XL":40, "XC":90, "CD":400,"CM":900
                }
        sums = dicts[s[0]]
        last = s[0]
        for index in range(1,len(s)):
            flag= False
            if s[index] in ["V", "X"] and last == "I":
                flag = True
            elif s[index] in ["L", "C"] and last == "X":
                flag = True
            elif s[index] in ["D","M"] and last == "C":
                flag = True
                
            if flag:
                sums -= dicts[last]
                sums += dicts[last+s[index]]
            else:
                sums += dicts[s[index]]
            last = s[index]
                
        return sums