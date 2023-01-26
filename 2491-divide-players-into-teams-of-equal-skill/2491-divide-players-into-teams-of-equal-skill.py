class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        arr =[]
        size = len(skill)
        left = 0 
        right = size -1
        while left < right:
            if arr and arr[-1][0]+arr[-1][1] != skill[left] + skill[right]:
                return -1
            arr.append([skill[left], skill[right]])
            left += 1
            right -= 1
        result = 0
        for element in arr:
            result += element[0]*element[1]
        return result