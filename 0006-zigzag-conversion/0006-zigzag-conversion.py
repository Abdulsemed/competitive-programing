class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr =[["" for index in range(1000)] for index in range(numRows)]
        flag = True
        idx = 0
        index = 0
        while idx < len(s):
            counter = 1
            for val in range(numRows):
                if flag:
                    arr[val][index] = s[idx]
                elif numRows - counter-1 != 0:
                    arr[numRows - counter-1][counter+index-1] = s[idx]
                    counter += 1
                else: break
                idx += 1
                if idx == len(s): break
            index += 1
            if not flag:
                index = counter + index -2
            flag = not flag
        ans = []
        for index in range(len(arr)):
            for val in range(len(arr[index])):
                if arr[index][val] != "":
                    ans.append(arr[index][val])
        
        return ''.join(ans)