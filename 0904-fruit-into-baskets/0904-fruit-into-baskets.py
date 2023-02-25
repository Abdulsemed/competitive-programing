class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict1 = {}
        left = 0
        right = 0
        size = len(fruits)
        maxLen = 0
        for right in range(size):
            while fruits[right] not in dict1 and len(dict1) ==2:
                dict1[fruits[left]] -= 1
                if dict1[fruits[left]] == 0:
                    del dict1[fruits[left]]
                left +=1
            dict1[fruits[right]] = 1 + dict1.get(fruits[right],0)
            maxLen = max(maxLen, sum(dict1.values()))
            
        return maxLen
                