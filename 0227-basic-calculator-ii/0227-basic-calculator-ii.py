class Solution:
    def calc(self,stack,nums):
        op = stack.pop()
        val1 = nums.pop()  
        val2 = nums.pop()
        if op == "*":
            nums.append(val1*val2)
        elif op == "/":
            # if val1 == 0 or val2 == 0:
            #     nums.append(0)
            # else:
            nums.append(val2//val1)
        elif op == "+":
            nums.append(val2+val1)
        else:
            nums.append(val2-val1)
    def calculate(self, s: str) -> int:
        stack =[]
        nums = []
        pred = {"+":0, "-":1 ,"/": 2, "*": 2}
        index = 0
        while index < len(s):
            if s[index] == " ":
                index += 1
                continue
            if s[index] in pred:
                if stack and pred[stack[-1]] >= pred[s[index]]:
                    while stack and pred[stack[-1]] >= pred[s[index]]:
                        self.calc(stack,nums)
                
                stack.append(s[index])
                index += 1
            else:
                curr = index
                while index < len(s) and s[index] not in ["/", "*","+","-"," "] :
                    index += 1
                nums.append(int(s[curr:index]))
        while stack:
            self.calc(stack,nums)
        return nums[0]