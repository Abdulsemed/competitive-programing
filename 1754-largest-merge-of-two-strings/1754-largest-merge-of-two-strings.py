class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        pointer1 = 0
        pointer2 = 0
        size1 = len(word1)
        size2 = len(word2)
        merge = []
        while pointer1 < size1 and pointer2 < size2:
            if word1[pointer1] > word2[pointer2]:
                merge.append(word1[pointer1])
                pointer1 += 1
            elif word1[pointer1] == word2[pointer2]:
                if word1[pointer1:] > word2[pointer2:]:
                    merge.append(word1[pointer1])
                    pointer1 += 1
                else:
                    merge.append(word2[pointer2])
                    pointer2 += 1
            else:
                merge.append(word2[pointer2])
                pointer2 += 1               
        merge.extend(word1[pointer1:])  
        merge.extend(word2[pointer2:])
        return ''.join(merge)