class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        count = 0
        arr1 = list(sentence1.split(" "))
        arr2 = list(sentence2.split(" "))
        left = 0
        right = 0
        while left < len(arr1) or right < len(arr2):
            if left < len(arr1) and right < len(arr2) and arr1[left] != arr2[right]:
                if count:
                    return False
                count += 1
                currLeft = len(arr1)-1
                while currLeft > -1 and arr1[currLeft] != arr2[right]:
                    currLeft -= 1
                if currLeft == -1:
                    currRight = len(arr2)-1
                    while currRight > -1 and arr1[left] != arr2[currRight]:
                        currRight -= 1
                    if currRight == -1:
                        return False
                    right = currRight
                else:
                    left = currLeft
            elif left >= len(arr1) or right >= len(arr2):
                break
            left += 1
            right += 1
        
        if count and (left < len(arr1) or right < len(arr2)):
            return False
        
        return True