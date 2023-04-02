class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr = []
        for index in range(len(words)):
            mask = 0
            size = len(words[index])
            words[index] = tuple(set(words[index]))
            for val in range(len(words[index])):
                order = ord(words[index][val])- ord("a")
                check = 1<<order
                mask += 2**order
            arr.append((size, mask))
        maxim = 0
        for index in range(len(words)):
            for val in range(len(words)):
                flag = True
                if val == index:
                    continue
                for j in range(len(words[val])):
                    order = ord(words[val][j]) - ord("a")
                    check = 1<<order
                    if check & arr[index][1]:
                        flag = False
                        break
                if flag:
                    maxim = max(maxim, arr[val][0]*arr[index][0])
        return maxim
                