class Solution:
    def myAtoi(self, s: str) -> int:
        ans = []
        pos = True
        level = 0
        flag = True
        for index in range(len(s)):
            
            if s[index].isdigit():
                ans.append(int(s[index]))
                flag = False
            elif flag and  (s[index] == "-" or s[index] == "+"):
                if not ans:
                    pos = True if s[index] == "+" else False
                else:
                    break
                flag = False
            elif s[index] ==" ":
                if flag:
                    continue
                else: break
            else:
                break
        val = 0
        for index in range(len(ans)-1,-1,-1):
            val += ans[index]*(10**(len(ans)-index-1))
        if not pos:
            val = - val
        if val >= 2**31:
            val = (2**31)-1
        if val < -2**31:
            val = -2**31
        
        return val
                