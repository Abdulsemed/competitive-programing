class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        size1 = len(word1)
        size2 = len(word2)
        if size1 != size2:
            return False
        dicts1 = Counter(word1)
        dicts2 = Counter(word2)
        count = 0
        for key in dicts1:
            if key not in dicts2:
                return False
        arr1 = sorted(dicts1.values())
        arr2 = sorted(dicts2.values())
        if arr1 == arr2:
            return True
        return False