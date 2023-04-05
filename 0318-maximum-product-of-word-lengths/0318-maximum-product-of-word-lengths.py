class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr = []
        for index in range(len(words)):
            mask = 0
            size = len(words[index])
            for val in range(size):
                order = ord(words[index][val])- ord("a")
                check = 1<<order
                if check & mask != 0:
                    continue
                mask += 2**order
            words[index] = (len(words[index]),mask)
        maxim = 0
        for index in range(len(words)):
            for val in range(len(words)):
                if val == index:
                    continue
                if words[index][1] & words[val][1] == 0:
                    maxim = max(maxim, words[val][0]*words[index][0])
        return maxim
                