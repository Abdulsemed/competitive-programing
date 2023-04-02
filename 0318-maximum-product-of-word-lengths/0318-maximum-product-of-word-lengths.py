class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr = []
        for index in range(len(words)):
            val = set(words[index])
            arr.append((len(words[index]),val))
            words[index] = tuple(val)
        maxim = 0
        for index in range(len(words)):
            for val in range(len(words)):
                flag = True
                if val == index:
                    continue
                for j in range(len(words[val])):
                    if words[val][j] in arr[index][1]:
                        flag = False
                        break
                if flag:
                    maxim = max(maxim, arr[val][0]*arr[index][0])
        return maxim
                