class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        commonPrefix = ""
        if len(strs)== 1:
            return strs[0]
        if len(strs[0]) == 0:
            return commonPrefix
        elif strs[0][0] != strs[-1][0]:
            return commonPrefix
        else:
            pointer = 0
            sizeOfArrays = min(len(strs[0]), len(strs[-1]))
            while strs[0][pointer] == strs[-1][pointer]:
                commonPrefix += strs[0][pointer]
                
                if pointer + 1 < sizeOfArrays:
                    pointer += 1
                else:
                    break
        
        return commonPrefix